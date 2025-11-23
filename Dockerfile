FROM python:3.11-slim

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y build-essential libsqlite3-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Instalar Kolibri
RUN pip install kolibri

EXPOSE 8080

CMD ["kolibri", "start", "--foreground", "--port=8080"]
