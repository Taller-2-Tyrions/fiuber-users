[![codecov](https://codecov.io/gh/Taller-2-Tyrions/fiuber-users/branch/main/graph/badge.svg?token=IEH333J1IF)](https://codecov.io/gh/Taller-2-Tyrions/fiuber-users)

# Fiuber-Users
Microservicio para manejo de usuarios(pasajeros y choferes).

# Documentación
Documentación técnica: https://taller-2-tyrions.github.io/fiuber-documentation-tecnica/

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

