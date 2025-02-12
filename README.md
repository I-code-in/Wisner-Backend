# Wisner
## Levantar Local
* Instalar Python 3.11
* Crear entorno virtual
''' Consola
python -m venv venv
'''
* Arctivar entorno virtual
''' Consola
.\venv\Scripts\activate
'''
* Instalar poetry (Windows)
''' Consola
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
'''
* Instalar dependencias
```console
poetry install
```
## Manejo de BD con DBEAVER

## nueva migracion
'''console
docker-compose exec backend poetry run alembic revision -m "001_create_products"
'''

'''console
docker-compose exec backend poetry run alembic down -1
'''
