## Building

1. Crear el archivo firebasekey.json en el root del proyecto
2. Crear el archivo .env basandose en .env_example
3. Correr:

```bash
docker build -f dev.Dockerfile  -t dev_users .
docker run dev_users
```
## Run Tests

```bash
python3 -m pytest tests/
```

a
