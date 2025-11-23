# Estructura de archivos para GitHub
# 1. Dockerfile
# 2. fly.toml
# 3. .github/workflows/deploy.yml
# 4. Carpeta 'canales/' con tus 4 archivos Kolibri

# ---------------------
# Dockerfile
# ---------------------
FROM python:3.11-slim

RUN apt-get update && apt-get install -y build-essential libsqlite3-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install kolibri

EXPOSE 8080

CMD ["kolibri", "start", "--foreground", "--port=8080"]

# ---------------------
# fly.toml
# ---------------------
app = "kolibri-demo"
primary_region = "iad"

[env]
  PYTHONUNBUFFERED = "1"

[[services]]
  internal_port = 8080
  protocol = "tcp"

  [[services.ports]]
    port = 80

[mounts]
  source="kolibri_data"
  destination="/root/.kolibri"

# ---------------------
# GitHub Actions workflow (.github/workflows/deploy.yml)
# ---------------------
name: Deploy Kolibri to Fly.io

on:
  push:
    branches: ["main"]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Install Flyctl
        uses: superfly/flyctl-actions/setup-flyctl@master

      - name: Deploy to Fly.io
        run: flyctl deploy --remote-only
        env:
          FLY_API_TOKEN: ${{ secrets.FLY_API_TOKEN }}

# ---------------------
# Carpeta 'canales/'
# ---------------------
# Coloca aquí tus 4 archivos de Kolibri.
# Ejemplo:
# canales/leccion1.zip
# canales/leccion2.zip
# canales/leccion3.zip
# canales/leccion