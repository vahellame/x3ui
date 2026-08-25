from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_panel_api_clients_add_body import PostPanelApiClientsAddBody
from ...models.post_panel_api_clients_add_response_200 import (
    PostPanelApiClientsAddResponse200,
)
from ...types import Response


def _get_kwargs(
    *,
    body: PostPanelApiClientsAddBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/panel/api/clients/add",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostPanelApiClientsAddResponse200 | None:
    if response.status_code == 200:
        response_200 = PostPanelApiClientsAddResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostPanelApiClientsAddResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiClientsAddBody,
) -> Response[PostPanelApiClientsAddResponse200]:
    """Create a new client and attach it to one or more inbounds in a single call. Body is JSON. Per-
    protocol secrets are generated server-side when omitted, so callers can send only the universal
    fields.

     Fields the server fills in when they are omitted — a valid value sent by the caller is never
    overwritten. Re-adding an email that already exists, with its stored `subId`, reuses the stored
    `id`, `password`, `auth` and `secret` instead of minting new ones, so the identity stays in sync
    across its inbounds.

    - **VLESS / VMess** — `id`, a fresh UUID
    - **Trojan** — `password`
    - **Shadowsocks** — `password`. On a `2022-blake3-*` inbound a supplied password that does not
    base64-decode to the key length of the cipher (16 or 32 bytes) is replaced by a generated key and
    the call still succeeds, so read the client back if you did not let the server pick. Legacy ciphers
    keep any non-empty password
    - **Hysteria** — `auth`
    - **mtproto** — `secret`, a FakeTLS secret derived from the fronting domain of the inbound, or from
    `www.cloudflare.com` when it has none
    - **WireGuard** — `privateKey` and `publicKey` when both are blank, or `publicKey` alone when only a
    `privateKey` was sent, plus `allowedIPs`: one free `/32` taken from the /24 the existing peers of
    that inbound already sit in, or from `10.0.0.0/24` when it has none

    Accepted on the same body but never generated: `preSharedKey` and `keepAlive` (WireGuard), `adTag`
    (mtproto).

    WireGuard is the only one of these that can fail. Allocation widens the search to the containing /16
    before giving up with `wireguard: no free address available in <scope>`, and an `allowedIPs`
    supplied by the caller is validated instead of allocated: `wireguard: allowedIPs entry already used
    by another client: <address>` when a different client of that same inbound already holds it. The
    check is per inbound, so the same address on two different inbounds is accepted. The same validation
    runs on POST /panel/api/clients/{email}/attach, where a client that already carries an address
    brings it along.

    Args:
        body (PostPanelApiClientsAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPanelApiClientsAddResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiClientsAddBody,
) -> PostPanelApiClientsAddResponse200 | None:
    """Create a new client and attach it to one or more inbounds in a single call. Body is JSON. Per-
    protocol secrets are generated server-side when omitted, so callers can send only the universal
    fields.

     Fields the server fills in when they are omitted — a valid value sent by the caller is never
    overwritten. Re-adding an email that already exists, with its stored `subId`, reuses the stored
    `id`, `password`, `auth` and `secret` instead of minting new ones, so the identity stays in sync
    across its inbounds.

    - **VLESS / VMess** — `id`, a fresh UUID
    - **Trojan** — `password`
    - **Shadowsocks** — `password`. On a `2022-blake3-*` inbound a supplied password that does not
    base64-decode to the key length of the cipher (16 or 32 bytes) is replaced by a generated key and
    the call still succeeds, so read the client back if you did not let the server pick. Legacy ciphers
    keep any non-empty password
    - **Hysteria** — `auth`
    - **mtproto** — `secret`, a FakeTLS secret derived from the fronting domain of the inbound, or from
    `www.cloudflare.com` when it has none
    - **WireGuard** — `privateKey` and `publicKey` when both are blank, or `publicKey` alone when only a
    `privateKey` was sent, plus `allowedIPs`: one free `/32` taken from the /24 the existing peers of
    that inbound already sit in, or from `10.0.0.0/24` when it has none

    Accepted on the same body but never generated: `preSharedKey` and `keepAlive` (WireGuard), `adTag`
    (mtproto).

    WireGuard is the only one of these that can fail. Allocation widens the search to the containing /16
    before giving up with `wireguard: no free address available in <scope>`, and an `allowedIPs`
    supplied by the caller is validated instead of allocated: `wireguard: allowedIPs entry already used
    by another client: <address>` when a different client of that same inbound already holds it. The
    check is per inbound, so the same address on two different inbounds is accepted. The same validation
    runs on POST /panel/api/clients/{email}/attach, where a client that already carries an address
    brings it along.

    Args:
        body (PostPanelApiClientsAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPanelApiClientsAddResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiClientsAddBody,
) -> Response[PostPanelApiClientsAddResponse200]:
    """Create a new client and attach it to one or more inbounds in a single call. Body is JSON. Per-
    protocol secrets are generated server-side when omitted, so callers can send only the universal
    fields.

     Fields the server fills in when they are omitted — a valid value sent by the caller is never
    overwritten. Re-adding an email that already exists, with its stored `subId`, reuses the stored
    `id`, `password`, `auth` and `secret` instead of minting new ones, so the identity stays in sync
    across its inbounds.

    - **VLESS / VMess** — `id`, a fresh UUID
    - **Trojan** — `password`
    - **Shadowsocks** — `password`. On a `2022-blake3-*` inbound a supplied password that does not
    base64-decode to the key length of the cipher (16 or 32 bytes) is replaced by a generated key and
    the call still succeeds, so read the client back if you did not let the server pick. Legacy ciphers
    keep any non-empty password
    - **Hysteria** — `auth`
    - **mtproto** — `secret`, a FakeTLS secret derived from the fronting domain of the inbound, or from
    `www.cloudflare.com` when it has none
    - **WireGuard** — `privateKey` and `publicKey` when both are blank, or `publicKey` alone when only a
    `privateKey` was sent, plus `allowedIPs`: one free `/32` taken from the /24 the existing peers of
    that inbound already sit in, or from `10.0.0.0/24` when it has none

    Accepted on the same body but never generated: `preSharedKey` and `keepAlive` (WireGuard), `adTag`
    (mtproto).

    WireGuard is the only one of these that can fail. Allocation widens the search to the containing /16
    before giving up with `wireguard: no free address available in <scope>`, and an `allowedIPs`
    supplied by the caller is validated instead of allocated: `wireguard: allowedIPs entry already used
    by another client: <address>` when a different client of that same inbound already holds it. The
    check is per inbound, so the same address on two different inbounds is accepted. The same validation
    runs on POST /panel/api/clients/{email}/attach, where a client that already carries an address
    brings it along.

    Args:
        body (PostPanelApiClientsAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPanelApiClientsAddResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiClientsAddBody,
) -> PostPanelApiClientsAddResponse200 | None:
    """Create a new client and attach it to one or more inbounds in a single call. Body is JSON. Per-
    protocol secrets are generated server-side when omitted, so callers can send only the universal
    fields.

     Fields the server fills in when they are omitted — a valid value sent by the caller is never
    overwritten. Re-adding an email that already exists, with its stored `subId`, reuses the stored
    `id`, `password`, `auth` and `secret` instead of minting new ones, so the identity stays in sync
    across its inbounds.

    - **VLESS / VMess** — `id`, a fresh UUID
    - **Trojan** — `password`
    - **Shadowsocks** — `password`. On a `2022-blake3-*` inbound a supplied password that does not
    base64-decode to the key length of the cipher (16 or 32 bytes) is replaced by a generated key and
    the call still succeeds, so read the client back if you did not let the server pick. Legacy ciphers
    keep any non-empty password
    - **Hysteria** — `auth`
    - **mtproto** — `secret`, a FakeTLS secret derived from the fronting domain of the inbound, or from
    `www.cloudflare.com` when it has none
    - **WireGuard** — `privateKey` and `publicKey` when both are blank, or `publicKey` alone when only a
    `privateKey` was sent, plus `allowedIPs`: one free `/32` taken from the /24 the existing peers of
    that inbound already sit in, or from `10.0.0.0/24` when it has none

    Accepted on the same body but never generated: `preSharedKey` and `keepAlive` (WireGuard), `adTag`
    (mtproto).

    WireGuard is the only one of these that can fail. Allocation widens the search to the containing /16
    before giving up with `wireguard: no free address available in <scope>`, and an `allowedIPs`
    supplied by the caller is validated instead of allocated: `wireguard: allowedIPs entry already used
    by another client: <address>` when a different client of that same inbound already holds it. The
    check is per inbound, so the same address on two different inbounds is accepted. The same validation
    runs on POST /panel/api/clients/{email}/attach, where a client that already carries an address
    brings it along.

    Args:
        body (PostPanelApiClientsAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPanelApiClientsAddResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
