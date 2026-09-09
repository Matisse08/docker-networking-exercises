import os
import pymysql
from flask import Flask

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "mysql-exonet")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "motdepasse")
DB_NAME = os.getenv("DB_NAME", "demo_db")

@app.route("/")
def hello_world():
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            connect_timeout=5,
        )

        with connection.cursor() as cursor:
            cursor.execute("SELECT VERSION()")
            mysql_version = cursor.fetchone()[0]

        connection.close()

        return (
            "<h1>Hello from Flask + Docker</h1>"
            "<p>Connexion MySQL reussie.</p>"
            f"<p>Serveur MySQL : {mysql_version}</p>"
        )
    except Exception as error:
        return (
            "<h1>Hello from Flask + Docker</h1>"
            f"<p>Erreur de connexion MySQL : {error}</p>"
        ), 500

if __name__ == "__main__":
    app.run("0.0.0.0", port=5001)
