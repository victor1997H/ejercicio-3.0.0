# ejercicio:3.0.0

Aplicación básica de lista de tareas desarrollada en Python.

## Ejecutar localmente

```bash
pip install -r requirements.txt
python app.py
```

## Ejecutar pruebas

```bash
pytest
```

## Docker

Construir imagen:

```bash
docker build -t ejercicio:3.0.0 .
```

Ejecutar contenedor:

```bash
docker run ejercicio:3.0.0
```

## CI/CD

El proyecto utiliza GitHub Actions para:

- Instalar dependencias
- Ejecutar pruebas
- Ejecutar la aplicación
- Construir imagen Docker
- Publicar imagen en GitHub Container Registry