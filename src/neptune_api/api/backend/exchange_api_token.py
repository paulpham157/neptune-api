from http import HTTPStatus
from typing import (
    Any,
    Dict,
    Optional,
    Union,
    cast,
)

import httpx

from ... import errors
from ...client import (
    AuthenticatedClient,
    Client,
)
from ...models.error import Error
from ...models.neptune_oauth_token import NeptuneOauthToken
from ...types import Response


def _get_kwargs(
    *,
    x_neptune_api_token: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["X-Neptune-Api-Token"] = x_neptune_api_token

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/backend/v1/authorization/oauth-token",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Error, NeptuneOauthToken]]:
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.REQUEST_TIMEOUT:
        response_408 = cast(Any, None)
        return response_408
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(Any, None)
        return response_422
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.OK:
        response_200 = NeptuneOauthToken.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Error, NeptuneOauthToken]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    x_neptune_api_token: str,
) -> Response[Union[Any, Error, NeptuneOauthToken]]:
    """Exchange Neptune API token with OAuth 2.0 JWT

    Args:
        x_neptune_api_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, NeptuneOauthToken]]
    """

    kwargs = _get_kwargs(
        x_neptune_api_token=x_neptune_api_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    x_neptune_api_token: str,
) -> Optional[Union[Any, Error, NeptuneOauthToken]]:
    """Exchange Neptune API token with OAuth 2.0 JWT

    Args:
        x_neptune_api_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, NeptuneOauthToken]
    """

    return sync_detailed(
        client=client,
        x_neptune_api_token=x_neptune_api_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    x_neptune_api_token: str,
) -> Response[Union[Any, Error, NeptuneOauthToken]]:
    """Exchange Neptune API token with OAuth 2.0 JWT

    Args:
        x_neptune_api_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, NeptuneOauthToken]]
    """

    kwargs = _get_kwargs(
        x_neptune_api_token=x_neptune_api_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    x_neptune_api_token: str,
) -> Optional[Union[Any, Error, NeptuneOauthToken]]:
    """Exchange Neptune API token with OAuth 2.0 JWT

    Args:
        x_neptune_api_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, NeptuneOauthToken]
    """

    return (
        await asyncio_detailed(
            client=client,
            x_neptune_api_token=x_neptune_api_token,
        )
    ).parsed
