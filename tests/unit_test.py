from random import random

import pytest
from elasticsearch import Elasticsearch
from sqlalchemy.orm import Session

from app.crud import (
    search_in_es, 
    search_in_db, 
    delete_in_es, 
    delete_in_db
    )


@pytest.mark.parametrize(
        ('search_text', 'expected_respose'),
        (
            ('собака', [722, 146, 1047]),
            ('asdasdddas', [])
        )
)
def test_search_in_es(search_text, expected_respose):

    response = search_in_es(search_text)

    assert set(response) == set(expected_respose)


def test_search_in_db():

    response = search_in_db([722, 146, 1047])

    assert len(response) == 3


def test_delete_in_es():
    '''Дважды пытается удалить случайную запись из индекса.
    Удаляет случайную, что бы при перезапуске, тест не падал при попытке удалить уже удалённый объект'''

    rand_id = int(random() * 1500)

    deletion_1 = delete_in_es(id=rand_id)
    assert deletion_1

    deletion_2 = delete_in_es(id=rand_id)
    assert not deletion_2


def test_delete_in_db():
    '''Дважды пытается удалить случайную запись из базы данных.
    Удаляет случайную, что бы при перезапуске, тест не падал при попытке удалить уже удалённый объект'''

    rand_id = int(random() * 1500)

    deletion_1 = delete_in_db(id=rand_id)
    assert deletion_1

    deletion_2 = delete_in_db(id=rand_id)
    assert not deletion_2
