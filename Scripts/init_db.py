import pandas as pd

from sqlalchemy import Text, DateTime, ARRAY, String
from sqlalchemy_utils import database_exists, create_database


db_url = 'postgresql://postgres:postgres@localhost/txt_search'


def process_csv():
    '''Обработка .csv'''
    df = pd.read_csv('Scripts\posts.csv')
    df.rubrics = df.rubrics.apply(eval)
    return df


def load_to_db(df, db_url, engine):
    if database_exists(db_url):
        print('База данных txt_search уже существует')
    else:
        create_database(db_url)
        print("База данных txt_search была создана")

    df.to_sql('comment', engine, if_exists='replace',
            dtype={
        'text': Text,
        'created_date': DateTime,
        'rubrics': ARRAY(String(20))}
        )

    print('Данные из posts.csv выгружены в БД')


def fill_db(engine):
    df = process_csv()
    load_to_db(df, db_url, engine)


if __name__ == '__main__':
    fill_db()
