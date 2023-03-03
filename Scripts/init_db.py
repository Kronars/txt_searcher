import sys, os
from pathlib import Path

import pandas as pd

from sqlalchemy import create_engine, MetaData
from sqlalchemy import Text, DateTime, ARRAY, String

from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, create_database


# * Обработка .csv
cwd = Path(sys.argv[0]).parent
os.chdir(cwd)

df = pd.read_csv('posts.csv')

df.rubrics = df.rubrics.apply(eval)


# * Выгрузка в бд
db_url = 'postgresql://postgres:postgres@localhost/txt_search'
conn_url = 'postgresql+psycopg2://postgres:postgres@localhost/txt_search'

if database_exists(db_url):
    print('База данных txt_search уже существует')
else:
    create_database(db_url)
    print("База данных txt_search была создана")

engine = create_engine(conn_url)
metadata = MetaData()

with Session(engine) as db:
    df.to_sql('comment', engine, if_exists='replace',
            dtype={
        'text': Text,
        'created_date': DateTime,
        'rubrics': ARRAY(String(20))}
        )

    print('Данные из posts.csv выгружены в БД')
