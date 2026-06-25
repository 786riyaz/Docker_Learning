# 🐳 Docker – Complete Notes & Command Reference (GitHub Ready)

---

## 🔁 Steps to Create a Docker Container

Docker install  
⇒ Docker File Creation  
⇒ Docker Image Creation  
⇒ Docker Containers  

---

## 🧱 Docker Basic Commands Cheat Sheet

### 🔹 1. System Information

| Command | Description |
|------|-------------|
| docker --version | Shows the installed Docker version. |
| docker info | Displays detailed information about Docker installation (containers, images, storage driver, etc.). |
| docker system df | Shows disk usage by Docker objects (images, containers, volumes). |
| docker system prune | Removes all stopped containers, unused networks, and dangling images. |

---

## 📄 Docker File

Simple text file with instruction to build docker image

---

## 🐳 2. Docker Images

Single file with all the dependencies and libraries to run the program

| Command | Description |
|------|-------------|
| docker images | Lists all images available locally. |
| docker pull `<image>` | Downloads an image from Docker Hub (e.g., docker pull ubuntu). |
| docker rmi `<image_id>` | Removes one or more images. |
| docker image ls | Lists all images (same as docker images). |
| docker image inspect `<image>` | Shows detailed metadata for an image. |
| docker build -t `<name>:<tag>` . | Builds an image from a Dockerfile in the current directory. |

### Image Build Commands

```bash
docker build .
docker build -t <Image tag> .
docker build -t <Repository Name>:<Tag Name> .
docker rmi <Repository Name>:<Tag Name>
docker tag <old name>:<tag> <new name>:<tag>
````

---

## 📦 3. Docker Containers

| Command                                        | Description                                                  |
| ---------------------------------------------- | ------------------------------------------------------------ |
| docker ps                                      | Lists running containers.                                    |
| docker ps -a                                   | Lists all containers (including stopped ones).               |
| docker run `<image>`                           | Creates and starts a new container from an image.            |
| docker run -it `<image>`                       | Runs a container in interactive mode (with terminal access). |
| docker run -d `<image>`                        | Runs a container in detached (background) mode.              |
| docker run -p 8080:80 `<image>`                | Maps container port 80 to host port 8080.                    |
| docker run --name `<container_name>` `<image>` | Runs a container with a custom name.                         |
| docker start `<container_id>`                  | Starts a stopped container.                                  |
| docker stop `<container_id>`                   | Stops a running container.                                   |
| docker restart `<container_id>`                | Restarts a container.                                        |
| docker rm `<container_id>`                     | Removes a stopped container.                                 |
| docker exec -it `<container_id>` bash          | Opens an interactive shell inside a running container.       |
| docker logs `<container_id>`                   | Displays logs from a container.                              |
| docker inspect `<container_id>`                | Shows detailed info about a container.                       |

### Container Run Examples

```bash
docker run <Image ID>
docker run <Image Tag>
docker run -t <Image Name>
docker run -t node
docker run -p <Main Machine Port>:<Container Port> <Image ID>
docker run -p <Main Machine Port>:<Container Port> <Image Tag>
docker run -d -p <Main Machine Port>:<Container Port> <Image ID>
docker run -d -p <Main Machine Port>:<Container Port> <Image Tag>
docker run -p 3000:5000 -e PORT=5000 express-server
docker run -p 3000:5000 --env PORT=5000 express-server
docker run -d --rm -p <Main Machine Port>:<Container Port> <Image ID>
docker run -d --rm -p <Main Machine Port>:<Container Port> <Image Tag>
docker run -d --rm --name "<Container Name>" -p <Main Machine Port>:<Container Port> <Image ID>
docker run -d --rm --name "<Container Name>" -p <Main Machine Port>:<Container Port> <Image Tag>
```

### Container Management

```bash
docker container ls
docker container ls -a
docker rm <Container Name>

docker start <Container Name>
docker stop <Container Name>
```

### Execute Commands Inside Container

```bash
docker exec <Container Name> <Command>
docker exec ubuntu_container ls
docker exec -it <Container Name> <Command>
docker exec -it ubuntu_container bash
```

---

## 🧭 4. Docker Volumes (Storage)

| Command                        | Description                         |
| ------------------------------ | ----------------------------------- |
| docker volume ls               | Lists all volumes.                  |
| docker volume create `<name>`  | Creates a new volume.               |
| docker volume inspect `<name>` | Shows details of a specific volume. |
| docker volume rm `<name>`      | Removes a volume.                   |
| docker volume prune            | Removes unused volumes.             |

```bash
docker volume create myvolume
```

---

## 🌐 5. Docker Networks

| Command                                             | Description                             |
| --------------------------------------------------- | --------------------------------------- |
| docker network ls                                   | Lists all Docker networks.              |
| docker network create `<name>`                      | Creates a new network.                  |
| docker network inspect `<name>`                     | Shows details about a specific network. |
| docker network connect `<network>` `<container>`    | Connects a container to a network.      |
| docker network disconnect `<network>` `<container>` | Disconnects a container from a network. |
| docker network rm `<name>`                          | Removes a network.                      |

### Network Examples

```bash
docker network create <Network Name>
docker network ls
docker run -d --env MYSQL_ROOT_PASSWORD="root" --env MYSQL_DATABASE="amazon" --name mysql_container mysql
docker run -d --env MYSQL_ROOT_PASSWORD="root" --env MYSQL_DATABASE="amazon" --name mysql_container --network my-net mysql
docker build -t connect_database .
docker run -it --rm --network my-net connect_database

docker exec -it mysql_container bash
mysql -u root -p
Enter Password
Show Databases

docker inspect mysql_container
docker start -ai connect_database
```

---

## 🧰 6. Docker Compose (Multi-Container Setup)

Configuration file to manage multiple containers running on same machine

| Command              | Description                                                |
| -------------------- | ---------------------------------------------------------- |
| docker-compose up    | Starts all services defined in docker-compose.yml.         |
| docker-compose up -d | Starts all services in detached mode.                      |
| docker-compose down  | Stops and removes all services and networks created by up. |
| docker-compose ps    | Lists containers managed by Compose.                       |
| docker-compose logs  | Shows logs from all containers.                            |
| docker-compose build | Builds or rebuilds services.                               |

```bash
docker compose -f filename.yaml up
docker compose -f filename.yaml up -d
docker compose -f filename.yml down
```

---

## 🧹 7. Docker Cleanup Commands

| Command                | Description                                                        |
| ---------------------- | ------------------------------------------------------------------ |
| docker container prune | Removes all stopped containers.                                    |
| docker image prune     | Removes unused images.                                             |
| docker network prune   | Removes unused networks.                                           |
| docker system prune -a | Removes all unused containers, images, and networks (⚠️ careful!). |

---

## 🧩 8. Dockerfile Related

```bash
docker build -t myapp:1.0 .
docker tag myapp:1.0 myrepo/myapp:latest
docker push myrepo/myapp:latest
```

---

## ⚙️ 9. Docker Login & Registry

| Command                    | Description                           |
| -------------------------- | ------------------------------------- |
| docker login               | Logs in to Docker Hub or registry.    |
| docker logout              | Logs out from Docker Hub or registry. |
| docker search `<image>`    | Searches for an image on Docker Hub.  |
| docker push `<repo/image>` | Pushes an image to Docker Hub.        |
| docker pull `<repo/image>` | Pulls an image from Docker Hub.       |

```bash
docker push <remote repo>:<tag>
```

---

## 🔗 Bind Mount

```bash
docker run -it --rm -v myvolume:/username/ username_app
docker run -v E:\Docker\Python\server_names.txt:/servername/server_names.txt server_name

docker run -d \
  -v /home/riyaz/myfolder:/usr/share/nginx/html \
  nginx
```

---

## 📦 Importing and Exporting Docker Image and Container

### Export / Save Docker IMAGE

```bash
docker save -o myapp.tar myapp:latest
```

### Export Docker CONTAINER

```bash
docker export my_container -o my_container.tar
```

### Save to Specific Folder

```bash
Windows :: docker save -o "C:\Users\YourName\Desktop\myapp.tar" myapp:latest
Linux :: docker save -o ~/Downloads/myapp.tar myapp:latest
```

### Verify Exported Image

```bash
docker load -i myapp.tar
```

---

## 🐬 MySQL Container Running

```bash
docker run --name mysql_container mysql
docker run --env MYSQL_ROOT_PASSWORD="root" --name mysql_container mysql
docker run --env MYSQL_ROOT_PASSWORD="root" --env MYSQL_DATABASE="amazon" --name mysql_container mysql
```

---

## 📄 .dockerignore

---

## ❤️ Health Check in Docker Compose

---

## 🖼️ IMAGES

```bash
docker images
docker rmi <image_name>
docker image prune
docker build -t <image_name>:<version> .
docker build -t <image_name>:<version> . -no-cache
```

---

## 📦 CONTAINER

```bash
docker ps -a
docker ps
docker run <image_name>
docker run -d <image_name>
docker run --name <container_name> <image_name>
docker run -p<host_port>:<container_port> <image_name>
docker run -e <var_name>=<var_value> <container_name>
docker start|stop <container_name>
docker inspect <container_name>
docker rm <container_name>
```

---

## 🛠️ TROUBLESHOOT

```bash
docker logs <container_name>
docker exec -it <container_name> /bin/bash
docker exec -it <container_name> sh
```

---

## ☁️ DOCKER HUB

```bash
docker pull <image_name>
docker push <username>/<image_name>
docker login -u <image_name>
docker login
docker logout
docker search <image_name>
```

---

## 📦 VOLUMES

```bash
docker volume ls
docker volume create <volume_name>
docker volume rm <volume_name>
docker run --volume <volume_name>:<mount_path>
docker run --mount type=volume,src=<volume_name>,dest=<mount_path>
docker run --volume <mount_path>
docker run --volume <host_path>:<container_path>
docker run --mount type=bind,src=<host_path>,dest=<container_path>
docker volume prune
```

---

## 🌐 NETWORK

```bash
docker network ls
docker network create <network_name>
docker network rm <network_name>
docker network prune
```