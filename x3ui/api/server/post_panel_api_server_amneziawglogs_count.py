from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_panel_api_server_amneziawglogs_count_body import (
    PostPanelApiServerAmneziawglogsCountBody,
)
from ...models.post_panel_api_server_amneziawglogs_count_response_200 import (
    PostPanelApiServerAmneziawglogsCountResponse200,
)
from ...types import Response


def _get_kwargs(
    count: int,
    *,
    body: PostPanelApiServerAmneziawglogsCountBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/panel/api/server/amneziawglogs/{count}".format(
            count=quote(str(count), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostPanelApiServerAmneziawglogsCountResponse200 | None:
    if response.status_code == 200:
        response_200 = PostPanelApiServerAmneziawglogsCountResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostPanelApiServerAmneziawglogsCountResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    count: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiServerAmneziawglogsCountBody,
) -> Response[PostPanelApiServerAmneziawglogsCountResponse200]:
    """Return live AmneziaWG peer activity (handshake, endpoint, transfer) plus the panel’s own AmneziaWG
    event lines.

    Args:
        count (int):
        body (PostPanelApiServerAmneziawglogsCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPanelApiServerAmneziawglogsCountResponse200]
    """

    kwargs = _get_kwargs(
        count=count,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    count: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiServerAmneziawglogsCountBody,
) -> PostPanelApiServerAmneziawglogsCountResponse200 | None:
    """Return live AmneziaWG peer activity (handshake, endpoint, transfer) plus the panel’s own AmneziaWG
    event lines.

    Args:
        count (int):
        body (PostPanelApiServerAmneziawglogsCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPanelApiServerAmneziawglogsCountResponse200
    """

    return sync_detailed(
        count=count,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    count: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiServerAmneziawglogsCountBody,
) -> Response[PostPanelApiServerAmneziawglogsCountResponse200]:
    """Return live AmneziaWG peer activity (handshake, endpoint, transfer) plus the panel’s own AmneziaWG
    event lines.

    Args:
        count (int):
        body (PostPanelApiServerAmneziawglogsCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPanelApiServerAmneziawglogsCountResponse200]
    """

    kwargs = _get_kwargs(
        count=count,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    count: int,
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiServerAmneziawglogsCountBody,
) -> PostPanelApiServerAmneziawglogsCountResponse200 | None:
    """Return live AmneziaWG peer activity (handshake, endpoint, transfer) plus the panel’s own AmneziaWG
    event lines.

    Args:
        count (int):
        body (PostPanelApiServerAmneziawglogsCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPanelApiServerAmneziawglogsCountResponse200
    """

    return (
        await asyncio_detailed(
            count=count,
            client=client,
            body=body,
        )
    ).parsed
