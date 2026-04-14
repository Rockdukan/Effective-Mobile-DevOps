#### Запуск
```bash
docker compose up -d --build
```

#### Проверка
```bash
curl http://localhost
curl http://localhost/health
```

#### Схема работы
```text
client -> http://localhost:80 -> nginx -> backend:8080 (docker network)
```