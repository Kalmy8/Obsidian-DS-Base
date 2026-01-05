---
type: note
status: done
tags: []
sources:
-
authors:
-
---

### 2-hour Docker lesson plan (with demos and exercises)

- Objective: Student understands images vs containers, writes efficient Dockerfiles with caching, explores containers via shell, uses Docker Compose and ports, and persists data with volumes.

1) General idea: images vs containers, why Docker (15 min)
- Concepts
 - Image: immutable template with your app and dependencies.
 - Container: runtime instance of an image (isolated process with its own FS, networking, PID namespace).
 - Why: consistency, portability, isolation, fast startup, reproducible builds.
- Demo (3–4 min)
 - Pull and run a simple image:
---
 ```bash
 docker pull nginx:alpine
 docker run --rm -d -p 8080:80 --name web nginx:alpine
 docker ps
 curl http://localhost:8080
 ```
- Key references
 - Docker overview: https://docs.docker.com/get-started/overview/

2) Dockerfiles, caching, CMD/ENTRYPOINT, COPY (30 min)
- Core instructions and best practices
 - FROM, WORKDIR, COPY, RUN, EXPOSE, ENV, CMD, ENTRYPOINT.
 - Caching: each instruction creates a layer; place least-changing steps first; use `.dockerignore`; combine related RUN steps; pin versions.
 - COPY vs ADD: prefer COPY; use ADD only for local tar auto-extract. Don’t use ADD to fetch URLs; use curl/wget in RUN.
 - CMD vs ENTRYPOINT:
 - ENTRYPOINT defines the executable; CMD supplies default args.
 - Exec form is preferred: `ENTRYPOINT ["python", "-m", "app"]` and `CMD ["--port","8000"]`.
- Demo (8–10 min)
 - Minimal app (e.g., Python/Node or use your repo’s `Dockerfile`):
 ```dockerfile
 FROM python:3.12-slim
 WORKDIR /app
 COPY requirements.txt .
 RUN pip install --no-cache-dir -r requirements.txt
 COPY . .
 EXPOSE 8000
 ENTRYPOINT ["python"]
 CMD ["-m", "http.server", "8000"]
 ```
 - Build twice to show caching:
 ```bash
 docker build -t demo:v1 .
 docker build -t demo:v1 .
 ```
 - Show `.dockerignore` effect.
- Notes to mention
 - Multi-stage builds to shrink images.
 - BuildKit tips (optional): `RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt` with DOCKER_BUILDKIT=1.
- Key references
 - Dockerfile best practices: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
 - COPY vs ADD: https://docs.docker.com/reference/dockerfile/#add

3) Attach via shell, explore the container (15 min)
- Concepts
 - `docker exec -it` opens a shell in a running container; `docker attach` ties to the main process I/O (often not what you want).
 - Use `bash` or `sh` depending on base image (Alpine -> `sh`).
- Demo (5–7 min)
 ```bash
 docker run -d --name demo -p 8000:8000 demo:v1
 docker exec -it demo sh
 uname -a
 cat /etc/os-release
 ps aux
 env
 ls -la /app
 exit
 ```
- Useful commands
 - `docker logs demo`, `docker inspect demo`, `docker top demo`, `docker stop demo && docker rm demo`.
- Reference
 - Exec vs attach: https://docs.docker.com/reference/cli/docker/container/exec/

4) Docker Compose, ports, networking (25 min)
- Concepts
 - Define multi-container apps in `docker-compose.yml` (v2 uses `docker compose` command).
 - Default network, service name DNS, port mapping `HOST:CONTAINER`.
- Demo (8–10 min)
 ```yaml
 # docker-compose.yml
 services:
 web:
 image: nginx:alpine
 ports:
 - "8080:80"
 depends_on:
 - api
 api:
 image: demo:v1
 environment:
 APP_ENV: "dev"
 ```
 ```bash
 docker compose up -d
 docker compose ps
 curl http://localhost:8080
 docker compose down
 ```
- Tips
 - Use `.env` for configuration; `healthcheck`, `restart`, `depends_on` (note: not a readiness gate).
- References
 - Compose docs: https://docs.docker.com/compose/
 - Compose file reference: https://docs.docker.com/compose/compose-file/

5) Volume mounting and persistence (20 min)
- Concepts
 - Bind mounts: host path -> container path (great for dev).
 - Named volumes: managed by Docker, portable between containers, good for data.
- Demos (choose one quick)
 - Bind mount (Windows PowerShell):
 ```bash
 docker run --rm -d --name web -p 8080:80 -v ${PWD}:/usr/share/nginx/html nginx:alpine
 ```
 Edit a local `index.html` and refresh browser to show live changes.
 - Named volume:
 ```bash
 docker volume create web_data
 docker run --rm -d -p 8080:80 -v web_data:/usr/share/nginx/html nginx:alpine
 docker volume ls
 docker volume inspect web_data
 ```
- Compose with volumes
 ```yaml
 services:
 web:
 image: nginx:alpine
 volumes:
 - web-data:/usr/share/nginx/html
 volumes:
 web-data:
 ```
- References
 - Use volumes: https://docs.docker.com/storage/volumes/
 - Bind mounts: https://docs.docker.com/storage/bind-mounts/

6) Quick wrap-up and Q&A (15 min)
- Recap: images vs containers, caching and Dockerfile hygiene, `exec` for shell, Compose basics, volumes for data.
- Optional advanced teasers (if time): multi-stage builds, healthchecks, slim images, scanning with `docker scout`.

Suggested pacing (sum ~120 min)
- 15 min: Core concepts + first run
- 30 min: Dockerfile + caching + CMD/ENTRYPOINT + COPY/ADD
- 15 min: Shell inside container
- 25 min: Compose + ports/networking
- 20 min: Volumes (bind + named)
- 15 min: Q&A buffer (integrate where needed)

Cheat-sheet commands to share
- Images/containers
 ```bash
 docker images
 docker ps -a
 docker run -d --name NAME -p HOST:CONT IMAGE[:TAG]
 docker stop NAME && docker rm NAME
 docker rmi IMAGE
 ```
- Build
 ```bash
 docker build -t NAME:TAG .
 DOCKER_BUILDKIT=1 docker build -t NAME:TAG .
 ```
- Shell and logs
 ```bash
 docker exec -it NAME sh
 docker logs -f NAME
 docker inspect NAME
 ```
- Compose
 ```bash
 docker compose up -d
 docker compose down -v
 docker compose logs -f
 docker compose ps
 ```

Notes for Windows delivery
- Prefer `${PWD}` in PowerShell for bind mounts; if path issues arise, consider WSL2 and mounting paths from the Linux side.
- Use `sh` for Alpine images; `bash` may not exist.

Summary
- Clear, demo-first path from images/containers → efficient Dockerfiles → interactive container debugging → multi-service orchestration with Compose → data persistence via volumes.
- Includes correct distinctions: COPY vs ADD, CMD vs ENTRYPOINT, exec vs attach, bind mounts vs named volumes.
- Linked to official docs for all core topics.