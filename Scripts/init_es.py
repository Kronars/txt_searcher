from elasticsearch import Elasticsearch
from sqlalchemy import create_engine, MetaData

from sqlalchemy import Table, select
from sqlalchemy.orm import Session


print('Подключение к БД')
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/txt_search')

metadata = MetaData()

Comment = Table('comment', metadata, autoload_with=engine)  # , schema='comment_schema')

# * Получение полей id и text
with Session(engine) as db:
    query = db.execute(select(Comment.c['index', 'text']))

db_data = query.all()


print('Подключение к ES')
es = Elasticsearch('http://localhost:9200')

print('Выгрузка данных БД в ES индекс')
for row in db_data:
    doc = {
        'id_db': row[0],
        'text': row[1]
    }
    es.index(index='comment', id=row[0], document=doc)

    if row[0] % 100 == 0: print(f'[Info] Выгружено {row[0] + 100} записей')

print('Создан индекс comment, записи из БД успешно выгружены в ES')
