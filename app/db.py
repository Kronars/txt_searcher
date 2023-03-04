from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

# Таблица "public.comment"
#    Столбец    |             Тип             |
# --------------+-----------------------------+
#  index        | bigint                      |
#  text         | text                        |
#  created_date | timestamp without time zone |
#  rubrics      | character varying(20)[]     |

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/txt_search')

metadata = MetaData()

Comment = Table('comment', metadata, autoload_with=engine)

Session = sessionmaker(bind=engine)
