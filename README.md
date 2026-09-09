# Docker Networking Exercises

Mini-projet Docker : une application Flask se connecte à MySQL depuis deux conteneurs distincts.

## Architecture

- `flask-web` : application web Flask, publiée sur `http://localhost:5001`
- `mysql-exonet` : serveur MySQL
- `exonet` : réseau Docker user-defined bridge partagé par les deux conteneurs

L'application Flask joint MySQL avec le hostname Docker `mysql-exonet`.

## Lancement

Créer le réseau :

```bash
docker network create exonet
```

Démarrer MySQL :

```bash
docker run -d \
  --name mysql-exonet \
  --platform linux/amd64 \
  --network exonet \
  -e MYSQL_ROOT_PASSWORD=motdepasse \
  -e MYSQL_DATABASE=demo_db \
  mysql:5.7
```

Construire Flask :

```bash
cd flask-web
docker build -t flask-mysql-demo .
```

Démarrer Flask :

```bash
docker run -d \
  --name flask-web \
  --network exonet \
  -p 5001:5001 \
  -e DB_HOST=mysql-exonet \
  -e DB_USER=root \
  -e DB_PASSWORD=motdepasse \
  -e DB_NAME=demo_db \
  flask-mysql-demo
```

## Vérification

Ouvrir `http://localhost:5001`. La page doit indiquer que la connexion MySQL a réussi.

## Arrêt

```bash
docker stop flask-web mysql-exonet
docker rm flask-web mysql-exonet
docker network rm exonet
```
