# Effective Mobile DevOps Test

## Запуск

```bash
docker compose up -d --build
```
Ожидаемый вывод: "Hello from Effective Mobile!"

## Архитектура

Client → nginx (80) → backend (8080),
    где 
    - nginx принимает HTTP-запросы
    - nginx делает реверспрокси на backend
    - backend даёт ответы

## Используемые технологии (библиотеки)
- Docker (Compose)
- Nginx
- Python (Flask/http.server)

## Как запускать

```
docker compose up -d --build
curl http://localhost
```