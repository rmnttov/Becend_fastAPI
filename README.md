# Becend_fastAPI

## Запуск бэка

```shell
poetry run uvicorn src.main:app --reload
```

## Запуск миграций

Генерация миграции:
```shell
poetry run alembic revision --autogenerate -m "название_миграции"
```

## Запуск фронта

Просто открыть **index.html**.
