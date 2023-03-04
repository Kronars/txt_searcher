from sqlalchemy import select
from sqlalchemy.orm import Session
from elasticsearch import Elasticsearch, NotFoundError

from app.db import Session, Comment, es


def search_in_es(text: str) -> list[int]:
    '''Поиск по тексту в ElasticSearch'''
    resp = es.search(index='comment', query={
        'match': {'text': text}}
        )
    
    hits = [hit['_source']['id_db'] for hit in resp.body['hits']['hits']]
    
    return hits


def search_in_db(hits: list[int]) -> list[tuple[str]]:
    '''Получение записей из БД по списку id'''
    with Session() as db:
        query = db.execute(
            select(Comment)
            .where(Comment.c.index.in_(hits))
            .order_by(Comment.c.created_date.asc())
            .limit(20)
        ).mappings().all()

    return query


def delete_in_db(id: int):
    '''Удаление из базы данных по айди.
    Успешное удаление - True
    Если запись не найдена - возвращает Fasle'''
    with Session() as db:
        code = db.query(Comment).filter_by(index=id).delete()
        db.commit()

    return True if code > 0 else False


def delete_in_es(id: int) -> True:
    '''Удаление из ElasticSearch по айди.
    Успешное удаление - True
    Если запись не найдена - возвращает Fasle'''
    try:
        es.delete(index='comment', id=id)
    except NotFoundError:
        return False
    
    return True
