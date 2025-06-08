# Dockerfile

FROM python:3.12-slim

# ENV
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Dépendances système (Pillow + psycopg2 + CORS + collectstatic, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Créer un répertoire de travail
WORKDIR /app

# Copier les fichiers
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copier tout le code
COPY . .

# Exposer le port
EXPOSE 8000

# Commande par défaut
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
