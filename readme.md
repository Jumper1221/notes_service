# Notes REST API

REST API сервис для управления текстовыми заметками. Реализована возможность добавлять, изменять и удалять заметки. Также мы можем получит все сохраненные заметки

## 📋 Содержание

- [Стек технологий](#-стек-технологий)
- [Запуск проекта](#-запуск-проекта)
- [API Endpoints](#-api-endpoints)
- [Примеры запросов (cURL)](#примеры-запросов-curl)
- [Миграции](#-миграции)
- [Переменные окружения](#-переменные-окружения)

## 🛠 Стек технологий

- Python 3.11
- Django 4.2
- Django REST Framework
- PostgreSQL 16
- Docker + Docker Compose

## 🚀 Запуск проекта

### Требования:

- Docker 20.10+
- Docker Compose 2.20+

1. Клонировать репозиторий:

```bash
git clone https://github.com/Jumper1221/notes_service
cd notes_service
```

2. Запустить сервисы:

```bash
docker-compose up --build
```

Сервисы будут доступны:

API: http://localhost:8000

PGAdmin: http://localhost:5050

PostgreSQL: порт 5432

## 📡 API Endpoints

Доступные эндпоинты:

| Метод  | URL            | Действие               |
| ------ | -------------- | ---------------------- |
| POST   | `/notes/`      | Создать заметку        |
| GET    | `/notes/`      | Получить все заметки   |
| GET    | `/notes/{id}/` | Получить заметку по ID |
| PUT    | `/notes/{id}/` | Обновить заметку       |
| DELETE | `/notes/{id}/` | Удалить заметку        |

### Примеры запросов (cURL)

#### Создание новой заметки:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"title": "Моя заметка"}' http://localhost:8000/notes
```

#### Получить список всех заметок:

```bash
curl http://localhost:8000/notes/
```

#### Получить одну заметку:

```bash
curl http://localhost:8000/notes/e945eddb-459f-4c46-8503-1dab3478365f
```

#### Обновить заметку:

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"title": "Новый заголовок"}' http://localhost:8000/notes/e945eddb-459f-4c46-8503-1dab3478365f
```

#### Удалить заметку:

```bash
curl -X DELETE http://localhost:8000/notes/e945eddb-459f-4c46-8503-1dab3478365f
```

#### Пример ответа:

```
{
    "id": "4cd0c458-0054-4fd8-9a5e-6d3c0afdedb8",
    "title": "Вторая заметка",
    "content": "описание",
    "created_at": "2025-04-10T17:30:53.870362Z",
    "updated_at": "2025-04-10T17:30:53.870380Z"
}
```

Тело запроса:

```json
{
  "title": "Hello",
  "content": "Description"
}
```

## Обработка ошибок

**400 Bad Request**: Невалидные данные (например, пустой title).

**404 Not Found**: Заметка с указанным ID не существует.

**500 Internal Server Error**: Внутренняя ошибка сервера.

## 📦 Миграции

Миграции и фикстуры применяются автоматически при старте контейнера

## 🔧 Переменные окружения

Настройки в .env файле:

```ini
DEBUG=0
SECRET_KEY=your-secret-key
DB_ENGINE=django.db.backends.postgresql

POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_DB=notes_db
POSTGRES_USER=your-user
POSTGRES_PASSWORD=your-password
```

## 📌 Примечания

- UUID используется в качестве первичного ключа
- Для теста в базу добавлена одна заметка с определенным uuid для удобства тестирования
