from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_panel_api_openapi_json_response_200 import (
    GetPanelApiOpenapiJsonResponse200,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/panel/api/openapi.json",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPanelApiOpenapiJsonResponse200 | None:
    if response.status_code == 200:
        response_200 = GetPanelApiOpenapiJsonResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetPanelApiOpenapiJsonResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetPanelApiOpenapiJsonResponse200]:
    """Serve this API description as an OpenAPI 3 document — the same file that powers the API Docs page.
    Requires a session or Bearer token like the rest of /panel/api. Useful for generating clients or
    importing into API tooling.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPanelApiOpenapiJsonResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetPanelApiOpenapiJsonResponse200 | None:
    """Serve this API description as an OpenAPI 3 document — the same file that powers the API Docs page.
    Requires a session or Bearer token like the rest of /panel/api. Useful for generating clients or
    importing into API tooling.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPanelApiOpenapiJsonResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetPanelApiOpenapiJsonResponse200]:
    """Serve this API description as an OpenAPI 3 document — the same file that powers the API Docs page.
    Requires a session or Bearer token like the rest of /panel/api. Useful for generating clients or
    importing into API tooling.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPanelApiOpenapiJsonResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetPanelApiOpenapiJsonResponse200 | None:
    """Serve this API description as an OpenAPI 3 document — the same file that powers the API Docs page.
    Requires a session or Bearer token like the rest of /panel/api. Useful for generating clients or
    importing into API tooling.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPanelApiOpenapiJsonResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
