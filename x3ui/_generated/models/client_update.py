from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.client_traffic_reset import ClientTrafficReset
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_allowed_i_ps_by_inbound import ClientAllowedIPsByInbound
    from ..models.client_reverse import ClientReverse


T = TypeVar("T", bound="ClientUpdate")


@_attrs_define
class ClientUpdate:
    """Write shape for POST /panel/api/clients/update/{email}. The endpoint replaces the whole row, so send every field you
    want to keep.

        Attributes:
            comment (str): Client comment
            email (str): Client email identifier
            enable (bool): Whether the client is enabled
            expiry_time (int): Expiration timestamp
            limit_ip (int): IP limit for this client
            reset (int): Reset period in days
            reset_day (int): Calendar renewal day 1-31, 0 = interval mode
            reset_max (int): Max auto-renew count, 0 = unlimited
            security (str): Security method (e.g., "auto", "aes-128-gcm")
            sub_id (str): Subscription identifier
            tg_id (int): Telegram user ID for notifications
            total_gb (int): Total traffic limit in GB
            ad_tag (str | Unset):  Example: 0123456789abcdef0123456789abcdef.
            allowed_i_ps (list[str] | Unset):
            allowed_i_ps_by_inbound (ClientAllowedIPsByInbound | Unset): AllowedIPsByInbound optionally overrides AllowedIPs
                on a per-inbound
                basis, keyed by inbound id. Lets one identity attached to both
                WireGuard and AmneziaWG carry two genuinely different addresses in a
                single Create/Update call instead of the shared AllowedIPs field
                being broadcast to every attached tunnel inbound. Absent/unset for a
                given inbound id falls back to the shared AllowedIPs exactly as
                before -- fully backward compatible for callers that never set this.
            auth (str | Unset): Auth password (Hysteria)
            created_at (int | Unset): Creation timestamp
            flow (str | Unset): Flow control (XTLS)
            forwarded_ports (str | Unset): AmneziaWG per-client port-forwarding spec, e.g. "80,443,8000-8100"
            group (str | Unset): Logical grouping label
            id (str | Unset): Unique client identifier
            keep_alive (int | Unset):
            password (str | Unset): Client password
            pre_shared_key (str | Unset):
            private_key (str | Unset):
            public_key (str | Unset):
            reverse (ClientReverse | None | Unset): VLESS simple reverse proxy settings
            secret (str | Unset):  Example: ee1234567890abcdef1234567890abcd7777772e636c6f7564666c6172652e636f6d.
            traffic_reset (ClientTrafficReset | Unset): Per-client traffic reset cycle, independent of the inbound's own
                (#5497).
            traffic_reset_day (int | Unset):
            updated_at (int | Unset): Last update timestamp
            limit_hwid (int | Unset): Maximum registered devices, 0 for unlimited.
    """

    comment: str
    email: str
    enable: bool
    expiry_time: int
    limit_ip: int
    reset: int
    reset_day: int
    reset_max: int
    security: str
    sub_id: str
    tg_id: int
    total_gb: int
    ad_tag: str | Unset = UNSET
    allowed_i_ps: list[str] | Unset = UNSET
    allowed_i_ps_by_inbound: ClientAllowedIPsByInbound | Unset = UNSET
    auth: str | Unset = UNSET
    created_at: int | Unset = UNSET
    flow: str | Unset = UNSET
    forwarded_ports: str | Unset = UNSET
    group: str | Unset = UNSET
    id: str | Unset = UNSET
    keep_alive: int | Unset = UNSET
    password: str | Unset = UNSET
    pre_shared_key: str | Unset = UNSET
    private_key: str | Unset = UNSET
    public_key: str | Unset = UNSET
    reverse: ClientReverse | None | Unset = UNSET
    secret: str | Unset = UNSET
    traffic_reset: ClientTrafficReset | Unset = UNSET
    traffic_reset_day: int | Unset = UNSET
    updated_at: int | Unset = UNSET
    limit_hwid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.client_reverse import ClientReverse

        comment = self.comment

        email = self.email

        enable = self.enable

        expiry_time = self.expiry_time

        limit_ip = self.limit_ip

        reset = self.reset

        reset_day = self.reset_day

        reset_max = self.reset_max

        security = self.security

        sub_id = self.sub_id

        tg_id = self.tg_id

        total_gb = self.total_gb

        ad_tag = self.ad_tag

        allowed_i_ps: list[str] | Unset = UNSET
        if not isinstance(self.allowed_i_ps, Unset):
            allowed_i_ps = self.allowed_i_ps

        allowed_i_ps_by_inbound: dict[str, Any] | Unset = UNSET
        if not isinstance(self.allowed_i_ps_by_inbound, Unset):
            allowed_i_ps_by_inbound = self.allowed_i_ps_by_inbound.to_dict()

        auth = self.auth

        created_at = self.created_at

        flow = self.flow

        forwarded_ports = self.forwarded_ports

        group = self.group

        id = self.id

        keep_alive = self.keep_alive

        password = self.password

        pre_shared_key = self.pre_shared_key

        private_key = self.private_key

        public_key = self.public_key

        reverse: dict[str, Any] | None | Unset
        if isinstance(self.reverse, Unset):
            reverse = UNSET
        elif isinstance(self.reverse, ClientReverse):
            reverse = self.reverse.to_dict()
        else:
            reverse = self.reverse

        secret = self.secret

        traffic_reset: str | Unset = UNSET
        if not isinstance(self.traffic_reset, Unset):
            traffic_reset = self.traffic_reset.value

        traffic_reset_day = self.traffic_reset_day

        updated_at = self.updated_at

        limit_hwid = self.limit_hwid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment": comment,
                "email": email,
                "enable": enable,
                "expiryTime": expiry_time,
                "limitIp": limit_ip,
                "reset": reset,
                "resetDay": reset_day,
                "resetMax": reset_max,
                "security": security,
                "subId": sub_id,
                "tgId": tg_id,
                "totalGB": total_gb,
            }
        )
        if ad_tag is not UNSET:
            field_dict["adTag"] = ad_tag
        if allowed_i_ps is not UNSET:
            field_dict["allowedIPs"] = allowed_i_ps
        if allowed_i_ps_by_inbound is not UNSET:
            field_dict["allowedIPsByInbound"] = allowed_i_ps_by_inbound
        if auth is not UNSET:
            field_dict["auth"] = auth
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if flow is not UNSET:
            field_dict["flow"] = flow
        if forwarded_ports is not UNSET:
            field_dict["forwardedPorts"] = forwarded_ports
        if group is not UNSET:
            field_dict["group"] = group
        if id is not UNSET:
            field_dict["id"] = id
        if keep_alive is not UNSET:
            field_dict["keepAlive"] = keep_alive
        if password is not UNSET:
            field_dict["password"] = password
        if pre_shared_key is not UNSET:
            field_dict["preSharedKey"] = pre_shared_key
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key
        if reverse is not UNSET:
            field_dict["reverse"] = reverse
        if secret is not UNSET:
            field_dict["secret"] = secret
        if traffic_reset is not UNSET:
            field_dict["trafficReset"] = traffic_reset
        if traffic_reset_day is not UNSET:
            field_dict["trafficResetDay"] = traffic_reset_day
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if limit_hwid is not UNSET:
            field_dict["limitHwid"] = limit_hwid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_allowed_i_ps_by_inbound import ClientAllowedIPsByInbound
        from ..models.client_reverse import ClientReverse

        d = dict(src_dict)
        comment = d.pop("comment")

        email = d.pop("email")

        enable = d.pop("enable")

        expiry_time = d.pop("expiryTime")

        limit_ip = d.pop("limitIp")

        reset = d.pop("reset")

        reset_day = d.pop("resetDay")

        reset_max = d.pop("resetMax")

        security = d.pop("security")

        sub_id = d.pop("subId")

        tg_id = d.pop("tgId")

        total_gb = d.pop("totalGB")

        ad_tag = d.pop("adTag", UNSET)

        allowed_i_ps = cast(list[str], d.pop("allowedIPs", UNSET))

        _allowed_i_ps_by_inbound = d.pop("allowedIPsByInbound", UNSET)
        allowed_i_ps_by_inbound: ClientAllowedIPsByInbound | Unset
        if isinstance(_allowed_i_ps_by_inbound, Unset):
            allowed_i_ps_by_inbound = UNSET
        else:
            allowed_i_ps_by_inbound = ClientAllowedIPsByInbound.from_dict(
                _allowed_i_ps_by_inbound
            )

        auth = d.pop("auth", UNSET)

        created_at = d.pop("created_at", UNSET)

        flow = d.pop("flow", UNSET)

        forwarded_ports = d.pop("forwardedPorts", UNSET)

        group = d.pop("group", UNSET)

        id = d.pop("id", UNSET)

        keep_alive = d.pop("keepAlive", UNSET)

        password = d.pop("password", UNSET)

        pre_shared_key = d.pop("preSharedKey", UNSET)

        private_key = d.pop("privateKey", UNSET)

        public_key = d.pop("publicKey", UNSET)

        def _parse_reverse(data: object) -> ClientReverse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reverse_type_1 = ClientReverse.from_dict(data)

                return reverse_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ClientReverse | None | Unset, data)

        reverse = _parse_reverse(d.pop("reverse", UNSET))

        secret = d.pop("secret", UNSET)

        _traffic_reset = d.pop("trafficReset", UNSET)
        traffic_reset: ClientTrafficReset | Unset
        if isinstance(_traffic_reset, Unset):
            traffic_reset = UNSET
        else:
            traffic_reset = ClientTrafficReset(_traffic_reset)

        traffic_reset_day = d.pop("trafficResetDay", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        limit_hwid = d.pop("limitHwid", UNSET)

        client_update = cls(
            comment=comment,
            email=email,
            enable=enable,
            expiry_time=expiry_time,
            limit_ip=limit_ip,
            reset=reset,
            reset_day=reset_day,
            reset_max=reset_max,
            security=security,
            sub_id=sub_id,
            tg_id=tg_id,
            total_gb=total_gb,
            ad_tag=ad_tag,
            allowed_i_ps=allowed_i_ps,
            allowed_i_ps_by_inbound=allowed_i_ps_by_inbound,
            auth=auth,
            created_at=created_at,
            flow=flow,
            forwarded_ports=forwarded_ports,
            group=group,
            id=id,
            keep_alive=keep_alive,
            password=password,
            pre_shared_key=pre_shared_key,
            private_key=private_key,
            public_key=public_key,
            reverse=reverse,
            secret=secret,
            traffic_reset=traffic_reset,
            traffic_reset_day=traffic_reset_day,
            updated_at=updated_at,
            limit_hwid=limit_hwid,
        )

        client_update.additional_properties = d
        return client_update

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
