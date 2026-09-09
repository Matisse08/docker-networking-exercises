# Flask dans Docker

## Construire l'image

```bash
docker build -t flask-web-demo .
```

## Lancer le serveur

```bash
docker run -d --name flask-web -p 5001:5001 flask-web-demo
```

Application disponible sur :

http://localhost:5001

## Voir les logs

```bash
docker logs flask-web
```

## Arrêter et supprimer le conteneur

```bash
docker stop flask-web
docker rm flask-web
```
