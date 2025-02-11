# Usar una imagen base de Python
FROM python:3.11.3

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Copiar archivos del proyecto
COPY pyproject.toml poetry.lock ./

# Instalar las dependencias del proyecto
RUN poetry install --no-root

# Copiar el resto del código
COPY . .

# Comando para ejecutar la aplicación
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]