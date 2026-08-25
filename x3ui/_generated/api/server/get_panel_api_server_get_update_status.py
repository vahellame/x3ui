from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_panel_api_server_get_update_status_response_200 import (
    GetPanelApiServerGetUpdateStatusResponse200,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/panel/api/server/getUpdateStatus",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPanelApiServerGetUpdateStatusResponse200 | None:
    if response.status_code == 200:
        response_200 = GetPanelApiServerGetUpdateStatusResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetPanelApiServerGetUpdateStatusResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetPanelApiServerGetUpdateStatusResponse200]:
    """Report the outcome of the most recently launched panel self-update (see POST updatePanel). Compare
    the returned runId against the one updatePanel returned to tell this run apart from a stale result.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPanelApiServerGetUpdateStatusResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetPanelApiServerGetUpdateStatusResponse200 | None:
    """Report the outcome of the most recently launched panel self-update (see POST updatePanel). Compare
    the returned runId against the one updatePanel returned to tell this run apart from a stale result.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPanelApiServerGetUpdateStatusResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetPanelApiServerGetUpdateStatusResponse200]:
    """Report the outcome of the most recently launched panel self-update (see POST updatePanel). Compare
    the returned runId against the one updatePanel returned to tell this run apart from a stale result.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPanelApiServerGetUpdateStatusResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetPanelApiServerGetUpdateStatusResponse200 | None:
    """Report the outcome of the most recently launched panel self-update (see POST updatePanel). Compare
    the returned runId against the one updatePanel returned to tell this run apart from a stale result.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPanelApiServerGetUpdateStatusResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
