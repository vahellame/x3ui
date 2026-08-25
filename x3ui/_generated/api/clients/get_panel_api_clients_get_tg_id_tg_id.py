from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_panel_api_clients_get_tg_id_tg_id_response_200 import (
    GetPanelApiClientsGetTgIdTgIdResponse200,
)
from ...types import Response


def _get_kwargs(
    tg_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/panel/api/clients/get/tgId/{tg_id}".format(
            tg_id=quote(str(tg_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPanelApiClientsGetTgIdTgIdResponse200 | None:
    if response.status_code == 200:
        response_200 = GetPanelApiClientsGetTgIdTgIdResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetPanelApiClientsGetTgIdTgIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tg_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetPanelApiClientsGetTgIdTgIdResponse200]:
    """Fetch clients by Telegram user ID. Returns an array since multiple clients can share the same
    Telegram ID.

    Args:
        tg_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPanelApiClientsGetTgIdTgIdResponse200]
    """

    kwargs = _get_kwargs(
        tg_id=tg_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tg_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetPanelApiClientsGetTgIdTgIdResponse200 | None:
    """Fetch clients by Telegram user ID. Returns an array since multiple clients can share the same
    Telegram ID.

    Args:
        tg_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPanelApiClientsGetTgIdTgIdResponse200
    """

    return sync_detailed(
        tg_id=tg_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tg_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetPanelApiClientsGetTgIdTgIdResponse200]:
    """Fetch clients by Telegram user ID. Returns an array since multiple clients can share the same
    Telegram ID.

    Args:
        tg_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPanelApiClientsGetTgIdTgIdResponse200]
    """

    kwargs = _get_kwargs(
        tg_id=tg_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tg_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> GetPanelApiClientsGetTgIdTgIdResponse200 | None:
    """Fetch clients by Telegram user ID. Returns an array since multiple clients can share the same
    Telegram ID.

    Args:
        tg_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPanelApiClientsGetTgIdTgIdResponse200
    """

    return (
        await asyncio_detailed(
            tg_id=tg_id,
            client=client,
        )
    ).parsed
