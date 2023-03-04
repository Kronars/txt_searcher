FROM python:3.11-alpine

RUN pip install "poetry==1.3.2"

WORKDIR /usr/src/code

COPY app .
COPY Scripts .
COPY poetry.lock .
COPY pyproject.toml .

RUN poetry config virtualenvs.create false
RUN poetry install --without dev

RUN poetry run ./Scripts/init_db.py
RUN poetry run ./Scripts/init_es.py

EXPOSE 80

ENTRYPOINT [ "poetry", "run", "uvicorn", "app.main:app", "--port 80" ]
