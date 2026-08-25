from __future__ import annotations

from typing import Any

from ._generated import AuthenticatedClient, Client
from ._generated.api.authentication import get_csrf_token, post_login, post_logout
from ._generated.api.clients import (
    get_panel_api_clients_get_email,
    get_panel_api_clients_links_email,
    get_panel_api_clients_list,
    get_panel_api_clients_sub_links_sub_id,
    get_panel_api_clients_traffic_email,
    post_panel_api_clients_add,
    post_panel_api_clients_del_email,
    post_panel_api_clients_email_attach,
    post_panel_api_clients_email_detach,
    post_panel_api_clients_ips_email,
    post_panel_api_clients_onlines,
    post_panel_api_clients_reset_traffic_email,
    post_panel_api_clients_update_email,
)
from ._generated.api.inbounds import (
    get_panel_api_inbounds_get_id,
    get_panel_api_inbounds_list,
    post_panel_api_inbounds_id_reset_traffic,
    post_panel_api_inbounds_set_enable_id,
)
from ._generated.api.server import (
    get_panel_api_server_get_new_uuid,
    get_panel_api_server_status,
    post_panel_api_server_restart_xray_service,
)
from ._generated.models.post_login_body import PostLoginBody
from ._generated.models.clients_add_request import ClientsAddRequest
from ._generated.models.clients_add_request_client import ClientsAddRequestClient
from ._generated.models.clients_attach_request import ClientsAttachRequest
from ._generated.models.clients_detach_request import ClientsDetachRequest
from ._generated.models.clients_update_request import ClientsUpdateRequest
from ._generated.models.inbounds_set_enable_request import InboundsSetEnableRequest
from ._generated.types import UNSET, Unset


class X3uiError(RuntimeError):
    """The panel accepted the request but reported success=false."""

    def __init__(self, message: str, operation: str = "") -> None:
        self.message = message
        self.operation = operation
        super().__init__(f"{operation}: {message}" if operation else message)


class NotAuthenticated(X3uiError):
    """No credentials were supplied, or the session has expired."""


def _unwrap(response: Any, operation: str) -> Any:
    if response is None:
        raise X3uiError("panel returned an undocumented response", operation)
    success = getattr(response, "success", UNSET)
    if success is False:
        message = getattr(response, "msg", UNSET)
        text = message if isinstance(message, str) and message else "request rejected"
        if "login" in text.lower() or "auth" in text.lower():
            raise NotAuthenticated(text, operation)
        raise X3uiError(text, operation)
    obj = getattr(response, "obj", UNSET)
    return None if isinstance(obj, Unset) else obj


def _clean(values: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in values.items() if value is not None}


class _Inbounds:
    def __init__(self, panel: "Panel") -> None:
        self._panel = panel

    def list(self) -> Any:
        return _unwrap(
            get_panel_api_inbounds_list.sync(client=self._panel.raw), "inbounds.list"
        )

    def get(self, inbound_id: int) -> Any:
        return _unwrap(
            get_panel_api_inbounds_get_id.sync(inbound_id, client=self._panel.raw),
            "inbounds.get",
        )

    def set_enable(self, inbound_id: int, enable: bool) -> Any:
        return _unwrap(
            post_panel_api_inbounds_set_enable_id.sync(
                inbound_id,
                client=self._panel.raw,
                body=InboundsSetEnableRequest(enable=enable),
            ),
            "inbounds.set_enable",
        )

    def reset_traffic(self, inbound_id: int) -> Any:
        return _unwrap(
            post_panel_api_inbounds_id_reset_traffic.sync(
                inbound_id, client=self._panel.raw
            ),
            "inbounds.reset_traffic",
        )


class _Clients:
    def __init__(self, panel: "Panel") -> None:
        self._panel = panel

    def list(self) -> Any:
        return _unwrap(
            get_panel_api_clients_list.sync(client=self._panel.raw), "clients.list"
        )

    def get(self, email: str) -> Any:
        return _unwrap(
            get_panel_api_clients_get_email.sync(email, client=self._panel.raw),
            "clients.get",
        )

    def traffic(self, email: str) -> Any:
        return _unwrap(
            get_panel_api_clients_traffic_email.sync(email, client=self._panel.raw),
            "clients.traffic",
        )

    def links(self, email: str) -> Any:
        return _unwrap(
            get_panel_api_clients_links_email.sync(email, client=self._panel.raw),
            "clients.links",
        )

    def sub_links(self, sub_id: str) -> Any:
        return _unwrap(
            get_panel_api_clients_sub_links_sub_id.sync(
                sub_id, client=self._panel.raw
            ),
            "clients.sub_links",
        )

    def online(self) -> list[str]:
        result = _unwrap(
            post_panel_api_clients_onlines.sync(client=self._panel.raw),
            "clients.online",
        )
        return result or []

    def ips(self, email: str) -> Any:
        return _unwrap(
            post_panel_api_clients_ips_email.sync(email, client=self._panel.raw),
            "clients.ips",
        )

    def add(
        self,
        email: str,
        inbound_ids: list[int],
        *,
        total_gb: int | None = None,
        expiry_time: int | None = None,
        limit_ip: int | None = None,
        limit_hwid: int | None = None,
        tg_id: int | None = None,
        enable: bool = True,
    ) -> Any:
        body = ClientsAddRequest(
            client=ClientsAddRequestClient(
                **_clean(
                    {
                        "email": email,
                        "total_gb": total_gb,
                        "expiry_time": expiry_time,
                        "limit_ip": limit_ip,
                        "limit_hwid": limit_hwid,
                        "tg_id": tg_id,
                        "enable": enable,
                    }
                )
            ),
            inbound_ids=inbound_ids,
        )
        return _unwrap(
            post_panel_api_clients_add.sync(client=self._panel.raw, body=body),
            "clients.add",
        )

    def update(
        self,
        email: str,
        *,
        new_email: str | None = None,
        total_gb: int | None = None,
        expiry_time: int | None = None,
        limit_hwid: int | None = None,
        tg_id: int | None = None,
        enable: bool | None = None,
    ) -> Any:
        body = ClientsUpdateRequest(
            **_clean(
                {
                    "email": new_email or email,
                    "total_gb": total_gb,
                    "expiry_time": expiry_time,
                    "limit_hwid": limit_hwid,
                    "tg_id": tg_id,
                    "enable": enable,
                }
            )
        )
        return _unwrap(
            post_panel_api_clients_update_email.sync(
                email, client=self._panel.raw, body=body
            ),
            "clients.update",
        )

    def delete(self, email: str, *, keep_traffic: bool = False) -> Any:
        return _unwrap(
            post_panel_api_clients_del_email.sync(
                email, client=self._panel.raw, keep_traffic=1 if keep_traffic else 0
            ),
            "clients.delete",
        )

    def reset_traffic(self, email: str) -> Any:
        return _unwrap(
            post_panel_api_clients_reset_traffic_email.sync(
                email, client=self._panel.raw
            ),
            "clients.reset_traffic",
        )

    def attach(self, email: str, inbound_ids: list[int]) -> Any:
        return _unwrap(
            post_panel_api_clients_email_attach.sync(
                email,
                client=self._panel.raw,
                body=ClientsAttachRequest(inbound_ids=inbound_ids),
            ),
            "clients.attach",
        )

    def detach(self, email: str, inbound_ids: list[int]) -> Any:
        return _unwrap(
            post_panel_api_clients_email_detach.sync(
                email,
                client=self._panel.raw,
                body=ClientsDetachRequest(inbound_ids=inbound_ids),
            ),
            "clients.detach",
        )


class _Server:
    def __init__(self, panel: "Panel") -> None:
        self._panel = panel

    def status(self) -> Any:
        return _unwrap(
            get_panel_api_server_status.sync(client=self._panel.raw), "server.status"
        )

    def new_uuid(self) -> Any:
        return _unwrap(
            get_panel_api_server_get_new_uuid.sync(client=self._panel.raw),
            "server.new_uuid",
        )

    def restart_xray(self) -> Any:
        return _unwrap(
            post_panel_api_server_restart_xray_service.sync(client=self._panel.raw),
            "server.restart_xray",
        )


class Panel:
    """High-level client for a 3x-ui panel.

    Pass ``token`` for API-token authentication, or call :meth:`login` with the
    panel admin credentials. Both modes share the same interface.

        panel = Panel("https://panel.example.com:2053", token="...")
        panel = Panel("https://panel.example.com:2053").login("admin", "admin")

    Every method returns the payload the panel put in ``obj``, or raises
    :class:`X3uiError` when the panel reports a failure.
    """

    def __init__(
        self,
        base_url: str,
        *,
        token: str | None = None,
        verify_ssl: bool = True,
        timeout: float | None = 30.0,
        **httpx_args: Any,
    ) -> None:
        import httpx

        common: dict[str, Any] = {
            "base_url": base_url.rstrip("/"),
            "verify_ssl": verify_ssl,
            "timeout": httpx.Timeout(timeout) if timeout else None,
            "follow_redirects": True,
        }
        if httpx_args:
            common["httpx_args"] = httpx_args

        if token:
            self._client: Client = AuthenticatedClient(token=token, **common)
        else:
            self._client = Client(**common)

        self.inbounds = _Inbounds(self)
        self.clients = _Clients(self)
        self.server = _Server(self)

    @property
    def raw(self) -> Client:
        """The underlying generated client, for endpoints this facade does not wrap."""
        return self._client

    def login(
        self, username: str, password: str, two_factor_code: str = ""
    ) -> "Panel":
        """Authenticate with panel credentials and keep the session.

        Fetches a CSRF token first: the panel rejects unauthenticated POSTs,
        including the login request itself, with 403 when the header is absent.
        """
        token = _unwrap(get_csrf_token.sync(client=self._client), "csrf_token")
        if not isinstance(token, str) or not token:
            raise X3uiError("panel did not return a CSRF token", "csrf_token")
        self._client.get_httpx_client().headers["X-CSRF-Token"] = token

        _unwrap(
            post_login.sync(
                client=self._client,
                body=PostLoginBody(
                    username=username,
                    password=password,
                    two_factor_code=two_factor_code,
                ),
            ),
            "login",
        )
        return self

    def logout(self) -> None:
        _unwrap(post_logout.sync(client=self._client), "logout")

    def close(self) -> None:
        self._client.get_httpx_client().close()

    def __enter__(self) -> "Panel":
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()
