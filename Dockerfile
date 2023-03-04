FROM python:3.11.0-alpine

RUN pip install --upgrade pip
RUN pip install "poetry==1.3.2"

WORKDIR /usr/src/code

COPY app ./app
COPY Scripts ./Scripts
COPY requirements.txt .
COPY pyproject.toml poetry.lock ./

# Зависимости psycopg2 которые должны быть в requirements -_-
RUN apk add --no-cache postgresql-dev \
    gcc python3-dev python3 \
    musl-dev gfortran 

# RUN pip install -r requirements.txt

RUN poetry config virtualenvs.create false && \
    poetry install --without dev

EXPOSE 80

ENTRYPOINT [ "python", "uvicorn", "app.main:app", "--port 80" ]
