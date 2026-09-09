import os
from flask import Flask, jsonify

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "dev")

@app.get("/")
def index():
    return jsonify({
        "service": "docker-networking-exercises",
        "version": VERSION,
        "status": "ok"
    })

@app.get("/health")
def health():
    # Ici on pourrait vérifier la DB, etc.
    return jsonify({
        "status": "healthy",
        "version": VERSION
    }), 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    app.run("0.0.0.0", port=port)
