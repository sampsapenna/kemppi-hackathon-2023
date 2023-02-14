### Kemppi Hackathon 2023 entry

### Development
Service requires a suitable S3 API to be available, default values are provided
for a dockerized deployment of [Minio](https://hub.docker.com/r/minio/minio)

Deploy minio on your development machine with the following command:
```
docker run -p 9000:9000 -p 9001:9001 \
  quay.io/minio/minio server /data --console-address ":9001"
```

Note that the default docker image doesn't provide data retention, all
files will be lost when the container is shut down.

#### Frontend development
The frontend has its own build instructions under `hackathon-frontend/README.md`

The frontend needs to be build before starting up the backend.

#### Backend development
Before starting the backend, install the required dependencies with:
```bash
pip install -r requirements.txt
```

The backend can be ran with the following commands:
```bash
cd hackathon_backend
python3 server.py
```

Make sure that the symbolic link to the frontend static folder hasn't broken when
cloning the repository.

The backend will be under the address `localhost:5000` by default. New users can
be registered at will, but they will not have a matching customer attached to them
before creating one on the Admin view.

Default admin credentials are:
```
username: admin
password: password
```

These can be changed with the following environment variables:
```
SOFTWARE_MANAGER_ADMIN_USERNAME
SOFTWARE_MANAGER_ADMIN_PASSWORD
```
