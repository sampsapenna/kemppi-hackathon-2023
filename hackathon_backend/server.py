"""Kemppi hackaton backend server."""
import flask 
import minio
import hashlib
import os
from flask import Flask, request, render_template, send_from_directory


client = minio.Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
)


app = flask.Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/')
def files():
    return 'files'


app = flask(__name__)

# Käytetään tässä väliaikaista tietokantaa esimerkin helpottamiseksi
users = {
    "user1": hashlib.sha256("password1".encode()).hexdigest(),
    "user2": hashlib.sha256("password2".encode()).hexdigest(),
    "user3": hashlib.sha256("password3".encode()).hexdigest()
}

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = hashlib.sha256(request.form["password"].encode()).hexdigest()
    if username in users and users[username] == password:
        return "Login successful"
    else:
        return "Login failed"

if __name__ == "__main__":
    app.run(debug=True)

    app = Flask(__name__)

# Määrittelee tiedostojen tallennuspaikan
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Tarkistaa, onko tallennuskansio olemassa, ja luo sen tarvittaessa
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def index():
    return render_template("file_upload.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    # Ladataan tiedosto
    file = request.files["file"]
    if file:
        # Tallennetaan tiedosto tallennuskansioon
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))
        return "Tiedoston lataaminen onnistui"
    else:
        return "Tiedoston lataaminen epäonnistui"

@app.route("/download/<filename>")
def download_file(filename):
    # Lähetetään tiedosto käyttäjälle
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=True)




