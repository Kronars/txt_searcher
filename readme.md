


# Тестовое задание для стажера Python

Необходимо написать очень простой поисковик по текстам документов. Данные хранятся в БД по желанию, поисковый индекс в эластике. 

Ссылка на тестовый массив данных: [[csv](https://disk.yandex.ru/d/HF1iDIN7DXqNVQ)]

### Структура БД:

- `id` - уникальный для каждого документа;
- `rubrics` - массив рубрик;
- `text` - текст документа;
- `created_date` - дата создания документа.

### Структура Индекса:

- `iD` - id из базы;
- `text` - текст из структуры БД.

## Необходимые методы

- сервис должен принимать на вход произвольный текстовый запрос, искать по тексту документа в индексе и возвращать первые 20 документов со всем полями БД, упорядоченные по дате создания;
- удалять документ из БД и индекса по полю  `id`.

## Технические требования:

- любой python фреймворк кроме Django и DRF;
- `README` с гайдом по поднятию;
- `docs.json` - документация к сервису в формате openapi.

## Программа максимум:

- функциональные тесты;
- сервис работает в Docker;
- асинхронные вызовы.