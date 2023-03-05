import time
from sqlalchemy import select


def process_db(Comment, Session):
    # * Получение полей id и text
    with Session() as db:
        query = db.execute(select(Comment.c['index', 'text']))

    db_data = query.all()

    return db_data


def process_es(db_data, es):
    print('Выгрузка данных БД в ES индекс')
    for row in db_data:
        doc = {
            'id_db': row[0],
            'text': row[1]
        }
        es.index(index='comment', id=row[0], document=doc)

        if row[0] % 100 == 0: print(f'[Info] {time.ctime()} Выгружено {row[0] + 100} записей')

    print('Создан индекс comment, записи из БД успешно выгружены в ES')


def fill_es(Comment, Session, es):
    data = process_db(Comment, Session)
    process_es(data, es)
