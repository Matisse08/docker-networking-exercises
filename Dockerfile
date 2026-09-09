FROM python:3.12-slim

WORKDIR /app

# Installation des dépendances de l'app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code
COPY app/app.py .

ENV PORT=8080
EXPOSE 8080

CMD ["python", "app.py"]
