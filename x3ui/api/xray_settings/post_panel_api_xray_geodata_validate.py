from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_panel_api_xray_geodata_validate_body import (
    PostPanelApiXrayGeodataValidateBody,
)
from ...models.post_panel_api_xray_geodata_validate_response_200 import (
    PostPanelApiXrayGeodataValidateResponse200,
)
from ...types import Response


def _get_kwargs(
    *,
    body: PostPanelApiXrayGeodataValidateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/panel/api/xray/geodata/validate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostPanelApiXrayGeodataValidateResponse200 | None:
    if response.status_code == 200:
        response_200 = PostPanelApiXrayGeodataValidateResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostPanelApiXrayGeodataValidateResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiXrayGeodataValidateBody,
) -> Response[PostPanelApiXrayGeodataValidateResponse200]:
    """Check routing tokens against the databases on disk and return only the ones that do not resolve.
    Plain domains and CIDRs are ignored. Each issue carries a reason: syntax, fileMissing or
    categoryMissing.

    Args:
        body (PostPanelApiXrayGeodataValidateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPanelApiXrayGeodataValidateResponse200]
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
    body: PostPanelApiXrayGeodataValidateBody,
) -> PostPanelApiXrayGeodataValidateResponse200 | None:
    """Check routing tokens against the databases on disk and return only the ones that do not resolve.
    Plain domains and CIDRs are ignored. Each issue carries a reason: syntax, fileMissing or
    categoryMissing.

    Args:
        body (PostPanelApiXrayGeodataValidateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPanelApiXrayGeodataValidateResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiXrayGeodataValidateBody,
) -> Response[PostPanelApiXrayGeodataValidateResponse200]:
    """Check routing tokens against the databases on disk and return only the ones that do not resolve.
    Plain domains and CIDRs are ignored. Each issue carries a reason: syntax, fileMissing or
    categoryMissing.

    Args:
        body (PostPanelApiXrayGeodataValidateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPanelApiXrayGeodataValidateResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostPanelApiXrayGeodataValidateBody,
) -> PostPanelApiXrayGeodataValidateResponse200 | None:
    """Check routing tokens against the databases on disk and return only the ones that do not resolve.
    Plain domains and CIDRs are ignored. Each issue carries a reason: syntax, fileMissing or
    categoryMissing.

    Args:
        body (PostPanelApiXrayGeodataValidateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPanelApiXrayGeodataValidateResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
