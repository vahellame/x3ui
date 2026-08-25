from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_panel_api_xray_geodata_entries_response_200 import (
    GetPanelApiXrayGeodataEntriesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    file: str,
    code: str,
    q: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["file"] = file

    params["code"] = code

    params["q"] = q

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/panel/api/xray/geodata/entries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPanelApiXrayGeodataEntriesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetPanelApiXrayGeodataEntriesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetPanelApiXrayGeodataEntriesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    file: str,
    code: str,
    q: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[GetPanelApiXrayGeodataEntriesResponse200]:
    """One page of the rules inside a category — domain rules typed as domain/full/keyword/regexp for
    geosite databases, CIDRs for geoip ones.

    Args:
        file (str):
        code (str):
        q (str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPanelApiXrayGeodataEntriesResponse200]
    """

    kwargs = _get_kwargs(
        file=file,
        code=code,
        q=q,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    file: str,
    code: str,
    q: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> GetPanelApiXrayGeodataEntriesResponse200 | None:
    """One page of the rules inside a category — domain rules typed as domain/full/keyword/regexp for
    geosite databases, CIDRs for geoip ones.

    Args:
        file (str):
        code (str):
        q (str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPanelApiXrayGeodataEntriesResponse200
    """

    return sync_detailed(
        client=client,
        file=file,
        code=code,
        q=q,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    file: str,
    code: str,
    q: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[GetPanelApiXrayGeodataEntriesResponse200]:
    """One page of the rules inside a category — domain rules typed as domain/full/keyword/regexp for
    geosite databases, CIDRs for geoip ones.

    Args:
        file (str):
        code (str):
        q (str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPanelApiXrayGeodataEntriesResponse200]
    """

    kwargs = _get_kwargs(
        file=file,
        code=code,
        q=q,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    file: str,
    code: str,
    q: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> GetPanelApiXrayGeodataEntriesResponse200 | None:
    """One page of the rules inside a category — domain rules typed as domain/full/keyword/regexp for
    geosite databases, CIDRs for geoip ones.

    Args:
        file (str):
        code (str):
        q (str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPanelApiXrayGeodataEntriesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            file=file,
            code=code,
            q=q,
            offset=offset,
            limit=limit,
        )
    ).parsed
