from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from elasticsearch import Elasticsearch

from Scripts.init_db import fill_db
from Scripts.init_es import fill_es

# Таблица "public.comment"
#    Столбец    |             Тип             |
# --------------+-----------------------------+
#  index        | bigint                      |
#  text         | text                        |
#  created_date | timestamp without time zone |
#  rubrics      | character varying(20)[]     |

es = Elasticsearch('http://localhost:9200')

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/txt_search')
metadata = MetaData()
Session = sessionmaker(bind=engine)

fill_db(engine) # Загрузить из csv в бд

Comment = Table('comment', metadata, autoload_with=engine)

fill_es(Comment, Session, es)
