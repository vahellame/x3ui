from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_panel_api_setting_factory_defaults_response_200 import (
    PostPanelApiSettingFactoryDefaultsResponse200,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/panel/api/setting/factoryDefaults",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostPanelApiSettingFactoryDefaultsResponse200 | None:
    if response.status_code == 200:
        response_200 = PostPanelApiSettingFactoryDefaultsResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostPanelApiSettingFactoryDefaultsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[PostPanelApiSettingFactoryDefaultsResponse200]:
    """Return the shipped (factory) default value per browser-safe setting key, so clients can tell a
    stored value apart from the default it would fall back to. Per-install material (secret, panelGuid,
    mTLS keys) and credential fields are never included.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPanelApiSettingFactoryDefaultsResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> PostPanelApiSettingFactoryDefaultsResponse200 | None:
    """Return the shipped (factory) default value per browser-safe setting key, so clients can tell a
    stored value apart from the default it would fall back to. Per-install material (secret, panelGuid,
    mTLS keys) and credential fields are never included.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPanelApiSettingFactoryDefaultsResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[PostPanelApiSettingFactoryDefaultsResponse200]:
    """Return the shipped (factory) default value per browser-safe setting key, so clients can tell a
    stored value apart from the default it would fall back to. Per-install material (secret, panelGuid,
    mTLS keys) and credential fields are never included.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPanelApiSettingFactoryDefaultsResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> PostPanelApiSettingFactoryDefaultsResponse200 | None:
    """Return the shipped (factory) default value per browser-safe setting key, so clients can tell a
    stored value apart from the default it would fall back to. Per-install material (secret, panelGuid,
    mTLS keys) and credential fields are never included.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPanelApiSettingFactoryDefaultsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
