Below is a **clean, well-structured Markdown file** created from your content.
**No information has been removed or altered**—only organized, formatted, and standardized for revision and documentation use.

---

# 🐳 Docker Complete Notes & Command Cheat Sheet

---

## 🔁 Steps to Create a Docker Container

```
Docker Install
   ⇒ Dockerfile Creation
      ⇒ Docker Image Creation
         ⇒ Docker Container
```

---

## 🧱 Docker Basics

### 📄 Dockerfile

* A **simple text file**
* Contains **instructions to build a Docker image**
* Defines base image, dependencies, commands, ports, etc.

---

## 🧱 Docker Basic Commands Cheat Sheet

### 🔹 1. System Information

| Command               | Description                                                                |
| --------------------- | -------------------------------------------------------------------------- |
| `docker --version`    | Shows the installed Docker version.                                        |
| `docker info`         | Displays Docker installation details (containers, images, storage driver). |
| `docker system df`    | Shows disk usage by Docker objects.                                        |
| `docker system prune` | Removes stopped containers, unused networks, dangling images.              |

---

## 🐳 2. Docker Images

> A **single file** that contains all dependencies and libraries required to run a program.

### Image Commands

| Command                          | Description                          |
| -------------------------------- | ------------------------------------ |
| `docker images`                  | Lists all local images.              |
| `docker image ls`                | Same as `docker images`.             |
| `docker pull <image>`            | Downloads image from Docker Hub.     |
| `docker rmi <image_id>`          | Removes an image.                    |
| `docker image inspect <image>`   | Shows detailed metadata of an image. |
| `docker build -t <name>:<tag> .` | Builds image from Dockerfile.        |

### Image Build & Tag Examples

```bash
docker build .
docker build -t <ImageTag> .
docker build -t <RepositoryName>:<TagName> .
docker rmi <RepositoryName>:<TagName>
docker tag <old_name>:<tag> <new_name>:<tag>
```

---

## 📦 3. Docker Containers

### Container Commands

| Command                            | Description                   |
| ---------------------------------- | ----------------------------- |
| `docker ps`                        | Lists running containers.     |
| `docker ps -a`                     | Lists all containers.         |
| `docker run <image>`               | Creates & starts a container. |
| `docker run -it <image>`           | Interactive mode.             |
| `docker run -d <image>`            | Detached mode.                |
| `docker run -p 8080:80 <image>`    | Port mapping.                 |
| `docker run --name <name> <image>` | Run with custom name.         |
| `docker start <container_id>`      | Start stopped container.      |
| `docker stop <container_id>`       | Stop running container.       |
| `docker restart <container_id>`    | Restart container.            |
| `docker rm <container_id>`         | Remove container.             |
| `docker exec -it <id> bash`        | Access container shell.       |
| `docker logs <container_id>`       | View logs.                    |
| `docker inspect <container_id>`    | Inspect container details.    |

### Container Run Variations

```bash
docker run <ImageID>
docker run <ImageTag>
docker run -t node
docker run -p <HostPort>:<ContainerPort> <Image>
docker run -d -p <HostPort>:<ContainerPort> <Image>
docker run -p 3000:5000 -e PORT=5000 express-server
docker run -d --rm --name "<ContainerName>" -p <HostPort>:<ContainerPort> <Image>
```

### Container Management

```bash
docker container ls
docker container ls -a
docker rm <ContainerName>
docker start <ContainerName>
docker stop <ContainerName>
```

### Execute Commands Inside Container

```bash
docker exec <ContainerName> <Command>
docker exec -it <ContainerName> bash
```

---

## 🧭 4. Docker Volumes (Storage)

| Command                        | Description            |
| ------------------------------ | ---------------------- |
| `docker volume ls`             | Lists all volumes.     |
| `docker volume create <name>`  | Creates volume.        |
| `docker volume inspect <name>` | Inspect volume.        |
| `docker volume rm <name>`      | Remove volume.         |
| `docker volume prune`          | Remove unused volumes. |

```bash
docker volume create myvolume
```

---

## 🌐 5. Docker Networks

| Command                                       | Description           |
| --------------------------------------------- | --------------------- |
| `docker network ls`                           | Lists networks.       |
| `docker network create <name>`                | Create network.       |
| `docker network inspect <name>`               | Inspect network.      |
| `docker network connect <net> <container>`    | Connect container.    |
| `docker network disconnect <net> <container>` | Disconnect container. |
| `docker network rm <name>`                    | Remove network.       |

### Network Example

```bash
docker network create my-net
docker run -d --env MYSQL_ROOT_PASSWORD="root" --env MYSQL_DATABASE="amazon" \
--name mysql_container --network my-net mysql

docker build -t connect_database .
docker run -it --rm --network my-net connect_database
```

---

## 🧰 6. Docker Compose (Multi-Container Setup)

> Used to manage **multiple containers on the same machine**.

| Command                | Description             |
| ---------------------- | ----------------------- |
| `docker-compose up`    | Start services.         |
| `docker-compose up -d` | Start in detached mode. |
| `docker-compose down`  | Stop & remove services. |
| `docker-compose ps`    | List running services.  |
| `docker-compose logs`  | View logs.              |
| `docker-compose build` | Build services.         |

```bash
docker compose -f filename.yaml up
docker compose -f filename.yaml up -d
docker compose -f filename.yml down
```

---

## 🧹 7. Docker Cleanup Commands

| Command                  | Description                              |
| ------------------------ | ---------------------------------------- |
| `docker container prune` | Remove stopped containers.               |
| `docker image prune`     | Remove unused images.                    |
| `docker network prune`   | Remove unused networks.                  |
| `docker system prune -a` | Remove all unused Docker resources (⚠️). |

---

## 🧩 8. Dockerfile Related

```bash
docker build -t myapp:1.0 .
docker tag myapp:1.0 myrepo/myapp:latest
docker push myrepo/myapp:latest
```

---

## ⚙️ 9. Docker Login & Registry

| Command               | Description          |
| --------------------- | -------------------- |
| `docker login`        | Login to Docker Hub. |
| `docker logout`       | Logout.              |
| `docker search <img>` | Search image.        |
| `docker pull <img>`   | Pull image.          |
| `docker push <img>`   | Push image.          |

---

## 🔗 Bind Mounts

```bash
docker run -it --rm -v myvolume:/username/ username_app
docker run -v E:\Docker\Python\server_names.txt:/servername/server_names.txt server_name
docker run -d -v /home/riyaz/myfolder:/usr/share/nginx/html nginx
```

---

## 📦 Importing & Exporting Images and Containers

### Export Image

```bash
docker save -o myapp.tar myapp:latest
```

### Export Container

```bash
docker export my_container -o my_container.tar
```

### Load Image

```bash
docker load -i myapp.tar
```

---

## 🐬 MySQL Container Examples

```bash
docker run --name mysql_container mysql
docker run --env MYSQL_ROOT_PASSWORD="root" --name mysql_container mysql
docker run --env MYSQL_ROOT_PASSWORD="root" --env MYSQL_DATABASE="amazon" \
--name mysql_container mysql
```

---

## 📄 .dockerignore

* Prevents unnecessary files from being copied into Docker image.
* Improves build performance.

---

## ❤️ Health Check in Docker Compose

* Used to verify container/service health.
* Prevents dependent services from starting too early.

---

## 📌 IMAGES – Summary

```bash
docker images
docker rmi <image_name>
docker image prune
docker build -t <image_name>:<version> .
docker build -t <image_name>:<version> . --no-cache
```

---

## 📌 CONTAINERS – Summary

```bash
docker ps
docker ps -a
docker run <image>
docker run -d <image>
docker run --name <container> <image>
docker run -p <host>:<container> <image>
docker start|stop <container>
docker inspect <container>
docker rm <container>
```

---

## 🛠️ TROUBLESHOOTING

```bash
docker logs <container>
docker exec -it <container> bash
docker exec -it <container> sh
```

---

## ☁️ DOCKER HUB

```bash
docker pull <image>
docker push <username>/<image>
docker login
docker logout
docker search <image>
```

---

## 📦 VOLUMES – Summary

```bash
docker volume ls
docker volume create <volume>
docker volume rm <volume>
docker volume prune
docker run --mount type=volume,src=<vol>,dest=<path>
docker run --mount type=bind,src=<host>,dest=<container>
```

---

## 🌐 NETWORK – Summary

```bash
docker network ls
docker network create <network>
docker network rm <network>
docker network prune
```

---

✅ **This Markdown file is complete, structured, and revision-ready.**
If you want, I can also:

* Convert this into **PDF**
* Create **interview Q&A**
* Add **Dockerfile & Compose examples**
* Optimize for **DevOps interviews**
