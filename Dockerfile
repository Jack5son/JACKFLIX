FROM debian:11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    gcc \
    g++ \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd -r django && useradd -r -g django django

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/staticfiles /app/media

RUN chown -R django:django /app && \
    chmod +x manage.py

USER django

EXPOSE 8000

# Comando para executar a aplicação
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
