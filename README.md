# Wisner
## Levantar Local
* Instalar Python 3.11
* Crear entorno virtual
'''console
python -m venv venv
'''
* Arctivar entorno virtual
'''console
.\venv\Scripts\activate
'''
* Arctivar entorno virtual Linux
'''console
sourcer .\venv\bin\activate
'''
* Instalar poetry (Windows)
'''console
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
'''
* Instalar poetry (Linux)
'''console
pip install -U pip setuptools
pip install poetry
'''
* Instalar dependencias
'''console
poetry install
'''

* Levantar local
'''console
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000
'''
## Manejo de BD con DBEAVER

## nueva migracion
'''console
docker-compose exec backend poetry run alembic revision -m "001_create_products"
'''

## actualizar manualmente
'''console
docker-compose exec backend poetry run alembic upgrade head
'''

## bajar una version
'''console
docker-compose exec backend poetry run alembic downgrade -1
'''

## historial de versiones
'''console
docker-compose exec backend poetry run alembic history
'''

## bajar una version especifica
'''console
docker-compose exec backend poetry run alembic down <codigo>
''''

## Levantar con docker
'''console
docker compose up -d --build
'''