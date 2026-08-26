# x3ui
[![PyPI](https://img.shields.io/pypi/v/x3ui)](https://pypi.org/project/x3ui/)
[![Python](https://img.shields.io/pypi/pyversions/x3ui)](https://pypi.org/project/x3ui/)
[![CI](https://github.com/vahellame/x3ui/actions/workflows/ci.yml/badge.svg)](https://github.com/vahellame/x3ui/actions/workflows/ci.yml)
[![License](https://img.shields.io/pypi/l/x3ui)](https://github.com/vahellame/x3ui/blob/main/LICENSE)

[English](README.md)

Python-клиент к API панели 3x-ui. Неофициальный, с разработчиками [3x-ui](https://github.com/MHSanaei/3x-ui) не связан.

```
pip install x3ui
```

## Использование

```python
from datetime import timedelta

from x3ui import Panel

panel = Panel("https://panel.example.com:2053/yourpath", token="...")

panel.clients.add("alice", inbound_ids=[3], total_gb=100, expires=timedelta(days=30))
print(panel.clients.links("alice"))
```

## Подключение

```python
panel = Panel(url, token="...")

panel = Panel(url).login("admin", "password")
panel = Panel(url).login("admin", "password", two_factor_code="123456")
```

`url` включает порт и базовый путь панели. Дополнительные аргументы: `verify_ssl`, `timeout` и всё остальное, что принимает `httpx.Client`.

`Panel` работает как контекстный менеджер и закрывает соединение на выходе.

## Клиенты

```python
panel.clients.list()
panel.clients.get("alice")
panel.clients.traffic("alice")
panel.clients.links("alice")
panel.clients.sub_links("subid")
panel.clients.online()
panel.clients.ips("alice")
```

```python
panel.clients.add(
    "alice",
    inbound_ids=[3, 5],
    total_gb=100,
    expires=timedelta(days=30),
    limit_ip=3,
    limit_hwid=10,
)
```

`total_gb` — гигабайты, `expires` принимает `timedelta`, `datetime` или Unix-миллисекунды. Без них — безлимит. Секреты генерирует панель.

```python
panel.clients.update("alice", uuid="...", password="...", auth="...")
panel.clients.update("alice", limit_ip=1000, limit_hwid=10)
panel.clients.update("alice", total_gb=200, expires=timedelta(days=90))
panel.clients.update("alice", enable=False, new_email="alice-2")
```

`update` читает текущую запись и отправляет обратно с заменёнными полями — эндпоинт панели перезаписывает строку целиком.

```python
panel.clients.delete("alice", keep_traffic=True)
panel.clients.reset_traffic("alice")
panel.clients.attach("alice", [7, 9])
panel.clients.detach("alice", [3])
```

### Пачкой

```python
panel.clients.extend(["alice", "bob"], days=30, gigabytes=100)
panel.clients.bulk_enable([...])
panel.clients.bulk_disable([...])
panel.clients.bulk_delete([...], keep_traffic=False)
panel.clients.bulk_reset_traffic([...])
panel.clients.delete_depleted()
panel.clients.delete_orphans()
```

`extend` принимает отрицательные значения и пропускает клиентов, у которых по изменяемому полю нет лимита.

## Инбаунды

```python
panel.inbounds.list()
panel.inbounds.get(3)
panel.inbounds.set_enable(3, False)
panel.inbounds.reset_traffic(3)
```

## Сервер

```python
panel.server.status()
panel.server.new_uuid()
panel.server.restart_xray()
```

## Ошибки

```python
from x3ui import NotAuthenticated, X3uiError

try:
    panel.clients.add("alice", inbound_ids=[3])
except NotAuthenticated:
    ...
except X3uiError as error:
    print(error.operation, error.message)
```

`X3uiError` несёт сообщение самой панели. Проблемы транспорта приходят исключениями `httpx`.

## Всё остальное

Панель отдаёт 186 эндпоинтов, ярлыки выше покрывают ходовые. Остальные сгенерированы и принимают `panel.raw` как клиент:

```python
from x3ui._generated.api.nodes import get_panel_api_nodes_list

get_panel_api_nodes_list.sync(client=panel.raw)
```

У каждого есть вариант `asyncio`. Конверт `{success, msg, obj}` они отдают как есть.

## Заметки

Что панель считает в байтах, остаётся байтами: `traffic()` возвращает `up`, `down`, `total`, где `0` — безлимит. Метки времени — Unix-миллисекунды.

`email` — идентификатор клиента, не обязательно адрес.

Python 3.10+. Сгенерировано под 3x-ui 3.x. Регенерация описана в [CONTRIBUTING.md](CONTRIBUTING.md).

## Лицензия

MIT
