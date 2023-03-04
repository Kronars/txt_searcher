from fastapi import FastAPI
from fastapi import HTTPException

from app import crud
from app.crud import es
from app.schemes import TextSearch, TextFound

app = FastAPI()


@app.on_event('shutdown')
def shutdown():
    es.close()

@app.get('/search')
def search(text: TextSearch) -> TextFound:
    '''Поиск по переданному тексту и получение 20 записей отсортированных по дате создания.
    Если ничего не найдено возвращает - {'result': 'nothing found'}'''
    db_id = crud.search_in_es(text.text)

    if db_id.__len__() == 0:
        return {'result': 'nothing found'}
    
    full_fields = crud.search_in_db(db_id)

    return TextFound(founded=full_fields)


@app.delete('/delete/{id}') # TODO: При двух быстрых запросах вернёт успех, выяснить
def delete(id: int):
    '''Полное удаление - из бд и из ElasticSearch.
    При успехе возвращает - 
    Если записи не было в бд или es - возвращает 404'''
    if not crud.delete_in_db(id) and not crud.delete_in_es(id):
        raise HTTPException(status_code=404, detail="Item not found")

    return {'result': f'successfully deleted'}
