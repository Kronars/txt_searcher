import os
import csv
import psycopg2
from urllib.parse import urlparse

from sqlalchemy_utils import database_exists, create_database, drop_database

DB_URL = os.getenv('DB_URL')
host = urlparse(DB_URL).netloc.split('@')[1]


def process_csv():
    '''Обработка .csv'''
    with open('Scripts/posts.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)    # Пропуск первой строчки с названиями столбцов

        data = []
        for row in reader:
            row[2] = eval(row[2])
            data.append(tuple(row))
    
    return data


def create_table(cur):
    cur.execute('''
CREATE TABLE comment (
	index SERIAL PRIMARY KEY, 
	text TEXT, 
	created_date TIMESTAMP WITHOUT TIME ZONE, 
	rubrics VARCHAR(20)[]
)''')


def insert_all(cur, rows):
    for row in rows:
        cur.execute('INSERT INTO comment(text, created_date, rubrics) \
                    VALUES (%s, %s, %s)', row)


def load_to_db(rows):
    if database_exists(DB_URL):
        print('База данных txt_search уже существует')
        return None
        # drop_database(DB_URL)
        # create_database(DB_URL)
    else:
        create_database(DB_URL)
        print("База данных txt_search была создана")

    conn = psycopg2.connect(user='postgres', dbname='txt_search', 
                        host=host, password='postgres')
    conn.autocommit = True

    cur = conn.cursor()

    with conn:
        with conn.cursor() as cur:
            create_table(cur)
            insert_all(cur, rows)


    print('Данные из posts.csv выгружены в БД')


def fill_db():
    rows = process_csv()
    load_to_db(rows)


if __name__ == '__main__':
    fill_db()
