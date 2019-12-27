```
# Dockerfile
FROM python:3

RUN pip3 install flask

# build custom image from Dockerfile
# -t = image tag
# . indicates path to Dockerfile
docker build \
    -t python_flask \
    .

# -it = run cmd line interpreter in container
# -v = mount current host directory to container folder: /src
# --rm = remove container after cmd is finished running
docker run \
    --rm \
    -it \
    -v $(pwd):/src \
    python_flask

# find container name
docker container ls
# or
docker ps

# -p = share host port 8080 to container port 80
# -d = start container in background process
docker run \
    --rm \
    -d \
    -v $(pwd):/usr/share/nginx/html \
    -p 8080:80 \
    nginx:latest

# web browser: localhost:8080

# stop daemon process and docker container
docker stop container_name

# access container and run cmd
docker exec -it container_name /bin/bash
```
