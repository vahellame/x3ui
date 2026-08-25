# x3ui
[![PyPI](https://img.shields.io/pypi/v/x3ui)](https://pypi.org/project/x3ui/)
[![Python](https://img.shields.io/pypi/pyversions/x3ui)](https://pypi.org/project/x3ui/)
[![CI](https://github.com/vahellame/x3ui/actions/workflows/ci.yml/badge.svg)](https://github.com/vahellame/x3ui/actions/workflows/ci.yml)
[![License](https://img.shields.io/pypi/l/x3ui)](https://github.com/vahellame/x3ui/blob/main/LICENSE)

[English](README.md)

Автоматизация панели 3x-ui на Python. Выдавать пользователей, продлевать подписки, смотреть расход трафика, чистить просроченные аккаунты — не заходя в веб-интерфейс.

Неофициальный проект, с разработчиками [3x-ui](https://github.com/MHSanaei/3x-ui) не связан.

```
pip install x3ui
```

## Подключение

```python
from x3ui import Panel

panel = Panel("https://panel.example.com:2053/yourpath")
panel.login("admin", "your-password")
```

URL — ровно тот, что вы вводите в браузере, вместе с портом и секретным путём панели.

Для всего, что работает без присмотра, лучше API-токен — создайте его в Settings → Security → API Token:

```python
panel = Panel("https://panel.example.com:2053/yourpath", token="...")
```

Токен даёт полные права администратора. Не держите его в коде — читайте из переменных окружения.

## Выдать пользователя

```python
from datetime import timedelta

panel.clients.add(
    "alice",
    inbound_ids=[3],
    total_gb=100,
    expires=timedelta(days=30),
    limit_ip=3,
)

for link in panel.clients.links("alice"):
    print(link)
```

Имя — то, по чему вы сами узнаёте пользователя. Панель называет это поле «email», но настоящий адрес там не обязателен.

Трафик задаётся в гигабайтах, срок — через `timedelta` от текущего момента или через `datetime`. Не указали — значит без ограничения. UUID, пароли и ключи панель генерирует сама.

`links()` возвращает ссылки для подключения по всем инбаундам пользователя — именно их вы ему отправляете. Если нужна ссылка на подписку, используйте `subId`:

```python
panel.clients.sub_links(panel.clients.get("alice").client.sub_id)
```

Не знаете ID своих инбаундов — посмотрите список:

```python
for inbound in panel.inbounds.list():
    print(inbound.id, inbound.remark, inbound.protocol, inbound.port)
```

## Продлить и пополнить

```python
panel.clients.extend(["alice", "bob"], days=30, gigabytes=100)
```

Работает с любым числом пользователей за раз и принимает отрицательные значения, если нужно наоборот забрать время или трафик. Тех, у кого срок или трафик безлимитный, метод не трогает — продление не превращает безлимит в ограничение.

Если пользователь исчерпал лимит и был автоматически отключён, продление включит его обратно.

Обнулить счётчик вместо пополнения:

```python
panel.clients.reset_traffic("alice")
panel.clients.bulk_reset_traffic(["alice", "bob"])
```

## Посмотреть расход

```python
usage = panel.clients.traffic("alice")
print(usage.up, usage.down, usage.total, usage.expiry_time)
```

`up` и `down` — израсходованные байты, `total` — квота (`0` означает безлимит).

Кто сейчас на связи:

```python
print(panel.clients.online())
```

С каких адресов подключается пользователь:

```python
print(panel.clients.ips("alice"))
```

Все сразу — для дашборда или отчёта:

```python
for client in panel.clients.list():
    used = client.traffic.up + client.traffic.down
    print(client.email, used, client.enable)
```

## Изменить и отозвать

```python
panel.clients.update("alice", limit_ip=1000, limit_hwid=10)
panel.clients.update("alice", password="new-secret", auth="new-secret")
panel.clients.update("alice", enable=False)
```

Меняются только переданные поля, остальное остаётся как было. Смена секрета делает старые ссылки пользователя нерабочими — отправьте ему новые из `links()`.

Отключить одного или сразу многих:

```python
panel.clients.bulk_disable(["alice", "bob"])
panel.clients.bulk_enable(["alice"])

panel.clients.delete("alice")
panel.clients.bulk_delete(["alice", "bob"], keep_traffic=True)
```

`keep_traffic` сохраняет записи учёта после удаления пользователя — это важно, если вы по ним выставляете счета.

Перенести пользователя между инбаундами, не пересоздавая:

```python
panel.clients.attach("alice", [7, 9])
panel.clients.detach("alice", [3])
```

## Уборка

```python
print(panel.clients.delete_depleted())
print(panel.clients.delete_orphans())
```

Первый метод удаляет всех, у кого кончился трафик или истёк срок, второй — тех, кто остался без инбаундов после их удаления. Оба необратимы и возвращают количество удалённых.

## Сервер и Xray

```python
status = panel.server.status()
print(status.cpu, status.mem.current, status.xray.state)

panel.server.restart_xray()
```

## Когда что-то пошло не так

```python
from x3ui import NotAuthenticated, X3uiError

try:
    panel.clients.add("alice", inbound_ids=[3])
except X3uiError as error:
    print(error.message)
```

`X3uiError` несёт то же сообщение, которое показала бы сама панель, — «email already in use», «port already in use» и подобные. `NotAuthenticated` возникает, когда сессия истекла: залогиньтесь заново и повторите. Проблемы со связью приходят как `httpx.TimeoutException`.

## Скрипты по расписанию

```python
import os
from datetime import datetime, timedelta, timezone

from x3ui import Panel

deadline = (datetime.now(timezone.utc) + timedelta(days=3)).timestamp() * 1000

with Panel(os.environ["PANEL_URL"], token=os.environ["PANEL_TOKEN"]) as panel:
    expiring = [
        client.email
        for client in panel.clients.list()
        if 0 < client.expiry_time < deadline
    ]
    if expiring:
        panel.clients.extend(expiring, days=30)
```

В качестве контекстного менеджера `Panel` закрывает соединение на выходе. Токену не нужен ни вызов логина, ни сессия, которая может протухнуть, — как раз то, что нужно для cron.

Самоподписанный сертификат на панели? Передайте `verify_ssl=False`. Медленный сервер? Передайте `timeout=60`.

## Всё остальное

Методы выше закрывают повседневные задачи. Ноды, хосты, бэкапы, конфиг Xray и остальные 186 эндпоинтов панели тоже доступны:

```python
from x3ui._generated.api.nodes import get_panel_api_nodes_list

print(get_panel_api_nodes_list.sync(client=panel.raw).obj)
```

Требуется Python 3.10 или новее. Заметки для разработки и инструкция по регенерации под свою панель — в [CONTRIBUTING.md](CONTRIBUTING.md).

## Лицензия

MIT
