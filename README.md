# x3ui
[![PyPI](https://img.shields.io/pypi/v/x3ui)](https://pypi.org/project/x3ui/)
[![Python](https://img.shields.io/pypi/pyversions/x3ui)](https://pypi.org/project/x3ui/)
[![CI](https://github.com/vahellame/x3ui/actions/workflows/ci.yml/badge.svg)](https://github.com/vahellame/x3ui/actions/workflows/ci.yml)
[![License](https://img.shields.io/pypi/l/x3ui)](https://github.com/vahellame/x3ui/blob/main/LICENSE)

Typed Python client for the 3x-ui panel API, generated from OpenAPI.

Unofficial project. Not affiliated with the [3x-ui](https://github.com/MHSanaei/3x-ui) developers.

## Installation

```
pip install x3ui
```

Requires Python 3.9+.

## Quick start

```python
from x3ui import AuthenticatedClient
from x3ui.api.inbounds import get_panel_api_inbounds_list

client = AuthenticatedClient(base_url="https://panel.example.com:2053", token="YOUR_API_TOKEN")

result = get_panel_api_inbounds_list.sync(client=client)
print(result.success, result.obj)
```

Base URL must include the port and the panel's base path if you configured one, for example `https://panel.example.com:2053/mypath`.

## Authentication

The panel supports two schemes.

### API token (recommended)

Create a token in the panel UI under Settings, or through the API, then pass it to `AuthenticatedClient`. Requests are sent with an `Authorization: Bearer <token>` header.

```python
from x3ui import AuthenticatedClient

client = AuthenticatedClient(base_url="https://panel.example.com:2053", token="YOUR_API_TOKEN")
```

Creating a token programmatically:

```python
from x3ui.api.api_tokens import post_panel_api_setting_api_tokens_create
from x3ui.models.post_panel_api_setting_api_tokens_create_body import PostPanelApiSettingApiTokensCreateBody

body = PostPanelApiSettingApiTokensCreateBody(name="automation", scope="admin", expires_at=0)
result = post_panel_api_setting_api_tokens_create.sync(client=client, body=body)
```

`expires_at` is a Unix timestamp; `0` means no expiry.

### Session cookie

```python
from x3ui import Client
from x3ui.api.authentication import post_login
from x3ui.models.post_login_body import PostLoginBody

client = Client(base_url="https://panel.example.com:2053")

response = post_login.sync_detailed(
    client=client,
    body=PostLoginBody(username="admin", password="admin", two_factor_code=""),
)

client = client.with_cookies({"3x-ui": response.cookies.get("3x-ui")})
```

Pass an empty string as `two_factor_code` when 2FA is disabled. The session cookie is not stored automatically: `Client` is immutable, so `with_cookies` returns a new instance that you need to keep and reuse.

## Common operations

### List all clients

```python
from x3ui.api.clients import get_panel_api_clients_list

result = get_panel_api_clients_list.sync(client=client)
```

For large panels use `get_panel_api_clients_list_paged` instead.

### Look up a client by email

```python
from x3ui.api.clients import get_panel_api_clients_get_email

result = get_panel_api_clients_get_email.sync("user@example.com", client=client)
```

The email is the client identifier in 3x-ui, not a real address.

### Get traffic for a client

```python
from x3ui.api.clients import get_panel_api_clients_traffic_email

result = get_panel_api_clients_traffic_email.sync("user@example.com", client=client)
```

### Get subscription links for a client

```python
from x3ui.api.clients import get_panel_api_clients_links_email

result = get_panel_api_clients_links_email.sync("user@example.com", client=client)
```

### Reset a client's traffic counter

```python
from x3ui.api.clients import post_panel_api_clients_reset_traffic_email

result = post_panel_api_clients_reset_traffic_email.sync("user@example.com", client=client)
```

### Delete a client

```python
from x3ui.api.clients import post_panel_api_clients_del_email

result = post_panel_api_clients_del_email.sync("user@example.com", client=client, keep_traffic=0)
```

Pass `keep_traffic=1` to keep the accumulated traffic statistics after removal.

### List clients that are currently online

```python
from x3ui.api.clients import post_panel_api_clients_onlines

result = post_panel_api_clients_onlines.sync(client=client)
```

### Get a single inbound

```python
from x3ui.api.inbounds import get_panel_api_inbounds_get_id

result = get_panel_api_inbounds_get_id.sync(1, client=client)
```

### Server status

```python
from x3ui.api.server import get_panel_api_server_status

result = get_panel_api_server_status.sync(client=client)
```

Returns CPU, memory, uptime, network counters and Xray state.

## Async usage

Every endpoint module exposes `asyncio` and `asyncio_detailed` alongside the sync variants. Import them under an alias to avoid shadowing the standard library module:

```python
import asyncio as aio

from x3ui import AuthenticatedClient
from x3ui.api.clients import get_panel_api_clients_list

async def main():
    client = AuthenticatedClient(base_url="https://panel.example.com:2053", token="YOUR_API_TOKEN")
    result = await get_panel_api_clients_list.asyncio(client=client)
    print(result.obj)

aio.run(main())
```

## Detailed responses

The plain `sync` and `asyncio` functions return the parsed model, or `None` when the status code is undocumented. Use the `_detailed` variants when you need the status code, headers or raw bytes:

```python
from x3ui.api.server import get_panel_api_server_status

response = get_panel_api_server_status.sync_detailed(client=client)

print(response.status_code)
print(response.headers)
print(response.parsed)
print(response.content)
```

## Error handling

By default, undocumented status codes yield `None`. To raise instead:

```python
client = AuthenticatedClient(
    base_url="https://panel.example.com:2053",
    token="YOUR_API_TOKEN",
    raise_on_unexpected_status=True,
)
```

The raised exception is `x3ui.errors.UnexpectedStatus`, which carries `status_code` and `content`. Network timeouts surface as `httpx.TimeoutException`.

## Client configuration

```python
import httpx

client = AuthenticatedClient(
    base_url="https://panel.example.com:2053",
    token="YOUR_API_TOKEN",
    timeout=httpx.Timeout(30.0),
    verify_ssl=False,
    follow_redirects=True,
    headers={"User-Agent": "my-bot/1.0"},
)
```

`verify_ssl=False` disables certificate verification. Only use it against panels with self-signed certificates, never in production. To pin a custom CA, pass a path to the certificate file instead.

For anything not exposed directly, reach the underlying httpx client:

```python
raw = client.get_httpx_client()
```

## Endpoint groups

Endpoints live under `x3ui.api.<group>`, mirroring the tags in the specification:

| Group | Contents |
| --- | --- |
| `authentication` | login, logout, CSRF token, 2FA |
| `clients` | CRUD, traffic, groups, IP limits, HWIDs, bulk operations |
| `inbounds` | CRUD, enable/disable, fallbacks, traffic resets, import/export |
| `server` | status, Xray control, certificates, metrics, database |
| `settings` | panel settings |
| `xray_settings` | Xray core configuration |
| `nodes` | multi-node management |
| `hosts` | host entries |
| `backup` | backup and restore |
| `api_tokens` | token management |
| `subscription_server` | subscription service |
| `subscription_balancers` | subscription balancers |
| `web_socket` | websocket endpoints |

Module names follow the pattern `<method>_<path>`, so `POST /panel/api/clients/add` becomes `x3ui.api.clients.post_panel_api_clients_add`.

## Known limitations

Response payloads arrive as `{success, msg, obj}` where `obj` is typed `Any`, because the upstream specification does not describe it. You get typed envelopes but untyped payloads.

Some request bodies are empty models for the same reason. Where a body model has no fields, the corresponding operation cannot be fully expressed through this client yet.

Do not run Python from inside the installed package directory. The package contains a `types.py` module that shadows the standard library `types` and causes a circular import.

## Regenerating

The client is generated from `openapi.json` in this repository:

```
pip install openapi-python-client
openapi-python-client generate --path openapi.json --meta none --output-path x3ui --overwrite
```

Generated against 3x-ui version X.Y.Z. Endpoints may differ on other panel versions.

## Contributing

Improvements to `openapi.json` are the most valuable contribution: adding `operationId` values produces readable function names, and describing `obj` schemas makes responses properly typed. Open an issue or a pull request.

## License

MIT
