from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_panel_api_hosts_set_enable_group_id_body import (
    PostPanelApiHostsSetEnableGroupIdBody,
)
from ...models.post_panel_api_hosts_set_enable_group_id_response_200 import (
    PostPanelApiHostsSetEnableGroupIdResponse200,
)
from ...types import Response


def _get_kwargs(
    group_id: str,
    *,
    body: PostPanelApiHostsSetEnableGroupIdBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/panel/api/hosts/setEnable/{group_id}".format(
            group_id=quote(str(group_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostPanelApiHostsSetEnableGroupIdResponse200 | None:
    if response.status_code == 200:
        response_200 = PostPanelApiHostsSetEnableGroupIdResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostPanelApiHostsSetEnableGroupIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiHostsSetEnableGroupIdBody,
) -> Response[PostPanelApiHostsSetEnableGroupIdResponse200]:
    """Enable or disable a host group.

    Args:
        group_id (str):
        body (PostPanelApiHostsSetEnableGroupIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPanelApiHostsSetEnableGroupIdResponse200]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiHostsSetEnableGroupIdBody,
) -> PostPanelApiHostsSetEnableGroupIdResponse200 | None:
    """Enable or disable a host group.

    Args:
        group_id (str):
        body (PostPanelApiHostsSetEnableGroupIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPanelApiHostsSetEnableGroupIdResponse200
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiHostsSetEnableGroupIdBody,
) -> Response[PostPanelApiHostsSetEnableGroupIdResponse200]:
    """Enable or disable a host group.

    Args:
        group_id (str):
        body (PostPanelApiHostsSetEnableGroupIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPanelApiHostsSetEnableGroupIdResponse200]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiHostsSetEnableGroupIdBody,
) -> PostPanelApiHostsSetEnableGroupIdResponse200 | None:
    """Enable or disable a host group.

    Args:
        group_id (str):
        body (PostPanelApiHostsSetEnableGroupIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPanelApiHostsSetEnableGroupIdResponse200
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            body=body,
        )
    ).parsed
