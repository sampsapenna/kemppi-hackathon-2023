"""Kemppi hackaton backend server."""

import typing
import hashlib
import os
import secrets
import datetime

import minio

import flask 

import flask_login


app = flask.Flask(__name__)

app.secret_key = secrets.token_bytes(64)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)


client = minio.Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False,
)


class APPUser(flask_login.UserMixin):
    def __init__(self, username, customer, password="", admin=False):
        """Initialize a new user."""
        self._customer = customer
        self._salt = secrets.token_bytes(16)
        self._admin = admin
        if admin:
            self.id = "admin"
        else:
            self.id = username
        self._hashed_password = hashlib.blake2b(
            password.encode("utf-8"),
            salt=self._salt,
        ).hexdigest()

    @property
    def is_admin(self):
        return self._admin
 
    def set_password(self, password):
        """Set password for application user."""
        self._hashed_password = hashlib.blake2b(
            password.encode("utf-8"),
            salt=self._salt,
        ).hexdigest()
    
    def check_password(self, password) -> bool:
        """Check if password is correct for this user."""
        return secrets.compare_digest(
            self._hashed_password,
            hashlib.blake2b(
                password.encode("utf-8"),
                salt=self._salt,
            ).hexdigest(),
        )

    def get_user_info(self):
        return {
            "customer": self._customer,
            "is_admin": self._admin,
        }

    def get_customer(self):
        return self._customer


admin_username = os.environ.get("SOFTWARE_MANAGER_ADMIN_USERNAME", "admin")
admin_raw_password = os.environ.get("SOFTWARE_MANAGER_ADMIN_PASSWORD", "password")


users = {
    admin_username: APPUser("admin", "admin", admin_raw_password, True)
}


@login_manager.user_loader
def load_user(user_id: str) -> typing.Optional[APPUser]:
    if user_id not in users:
        return None

    return users[user_id]


@login_manager.request_loader
def request_loader(request):
    user_id = request.form.get("username")
    if user_id not in users:
        return

    return users[user_id]


@app.route("/login", methods=["POST"])
def login():
    username = flask.request.form["username"]
    password = flask.request.form["password"]
    if username in users and users[username].check_password(password):
        flask_login.login_user(users[username])
        return flask.redirect(f"/app/{username}/{users[username].get_customer()}")
    else:
        return flask.redirect("/unauthorized")


@app.route("/app")
def get_app():
    return "OK\n"


@app.route('/api')
def get_index():
    return 'API running!\n'


@app.route("/api/admin/admin/users")
@flask_login.login_required
def list_users():
    print(flask_login.current_user.id)
    if flask_login.current_user.id != "admin":
        return
    return flask.jsonify(list(users.keys()))


@app.route("/api/admin/admin/users/<username>", methods=["GET", "PUT", "PATCH"])
@flask_login.login_required
def handler_user(username=""):
    if not flask_login.current_user.is_admin:
        return

    if flask.request.method == "GET":
        return flask.jsonify(users[username].get_user_info())
    if flask.request.method == "PATCH":
        args = flask.request.get_json()
        users[username].set_password(args["password"])
        return "OK"
    if flask.request.method == "PUT":
        args = flask.request.get_json()
        if not client.bucket_exists(args["customer"]):
            client.make_bucket(args["customer"])
        users[username] = APPUser(username, args["customer"], password=args["password"])
        return "OK"


@app.route("/logout")
@flask_login.login_required
def handle_logout():
    flask_login.logout_user()
    return flask.redirect("/")


@app.route('/api/<username>/<customer>/files')
@flask_login.login_required
def list_files(username="", customer=""):
    if not client.bucket_exists(customer):
        client.make_bucket(customer)
    files = client.list_objects(customer)
    return flask.jsonify(list(files))


@app.route(
    '/api/<username>/<customer>/files/<filename>',
    methods=["GET", "POST", "PUT", "DELETE"],
)
@flask_login.login_required
def handle_file(username="", customer="", filename=""):
    """Handle file operations."""
    if not flask_login.current_user.get_customer() == customer and not flask_login.current_user.is_admin:
        return "Forbidden, incorrect customer.", 403
    if flask.request.method == "GET":
        # Get a pre-signed link to object/file GET
        return flask.redirect(
            client.presigned_get_object(
                customer,
                filename,
                datetime.timedelta(days=1),
            ),
            307,
        )
    if flask.request.method == "PUT":
        # Get a pre-signed link to object/file PUT
        return flask.redirect(
            client.presigned_put_object(
                customer,
                filename,
                datetime.timedelta(days=1),
            ),
            307,
        )
    if flask.request.method == "POST":
        # Get a pre-signed link to object/file POST
        return "not yet implemented"
    if flask.request.method == "DELETE":
        # Delete the object from storage
        client.remove_object(
            customer,
            filename,
        )
        return "OK"


if __name__ == "__main__":
    app.run(debug=True)