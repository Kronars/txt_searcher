import os
from elasticsearch import Elasticsearch, NotFoundError


def deinit_all():
    db_del = os.system(
        'psql -d txt_search -c "DROP TABLE comment;"'
    )

    if db_del:
        print('База данных уже была удалена')
    else:
        print('База данных успешно удалена')


    es = Elasticsearch('http://localhost:9200')

    try:
        es.options().indices.delete(index='comment')
        print('Индекс в ES успешно удалён')
    except NotFoundError:
        print('Индекс в ES был уже удалён')
    finally:
        es.close()


if __name__ == '__main__':
    deinit_all()
