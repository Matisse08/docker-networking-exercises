# Docker Networking Exercises - CI/CD

Application Flask conteneurisée, déployée automatiquement sur une VM Azure avec GitHub Actions.

## Application

L’application expose deux endpoints :

- `GET /` : retourne les informations du service.
- `GET /health` : retourne l’état de santé de l’application.

L’application écoute sur le port `8080` dans le conteneur.

## Lancement local

Construire l’image :

```bash
docker build -t docker-networking-exercises .
```

Démarrer le conteneur :

```bash
docker run --rm -p 8080:8080 docker-networking-exercises
```

Tester :

```bash
curl http://localhost:8080/health
```

## Tests

### Tests unitaires

Les tests unitaires utilisent `pytest` :

```bash
cd app
pip install -r requirements.txt
pip install pytest
pytest
```

### Tests E2E

Les tests E2E vérifient l’application lancée dans Docker, notamment :

- la disponibilité via `GET /health` ;
- la réponse de `GET /`.

Ils sont exécutés automatiquement dans GitHub Actions.

## Pipeline CI/CD

Chaque `git push` sur la branche `main` déclenche automatiquement le workflow GitHub Actions :

1. Exécution des tests unitaires.
2. Exécution des tests E2E.
3. Build de l’image Docker.
4. Push de l’image sur Docker Hub :
   `matisse1/docker-networking-exercises`.
5. Connexion SSH à la VM Azure.
6. Pull de l’image Docker Hub.
7. Redéploiement du conteneur.
8. Vérification automatique de `GET /health`.

Le build, le push et le déploiement ne sont exécutés que si les tests unitaires et E2E réussissent.

## Déploiement Azure

La VM Azure utilise un port distinct pour éviter tout conflit sur une VM partagée :

```text
Port VM : 8081
Port conteneur : 8080
Conteneur : matisse-docker-networking
```

Le déploiement est idempotent. À chaque exécution, GitHub Actions supprime uniquement l’ancien conteneur `matisse-docker-networking`, puis démarre une nouvelle version avec le même nom :

```bash
docker rm -f matisse-docker-networking || true

docker run -d \
  --name matisse-docker-networking \
  --restart unless-stopped \
  -p 8081:8080 \
  matisse1/docker-networking-exercises:latest
```

La pipeline vérifie automatiquement l’application sur la VM avec :

```bash
curl --fail http://localhost:8081/health
```

URL publique prévue :

```text
http://20.56.74.49:8081/health
```

> L’accès externe au port `8081` dépend de la règle réseau Azure de la VM partagée. Le déploiement et le healthcheck local sur la VM sont validés par GitHub Actions.

## Secrets GitHub utilisés

Les informations sensibles ne sont pas stockées dans le dépôt. Le workflow utilise les GitHub Secrets suivants :

```text
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
VM_HOST
VM_USER
VM_SSH_PRIVATE_KEY
```
