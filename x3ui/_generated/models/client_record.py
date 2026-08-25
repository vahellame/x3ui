from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="ClientRecord")


@_attrs_define
class ClientRecord:
    """
    Attributes:
        ad_tag (str):
        allowed_i_ps (str):
        auth (str):
        comment (str):
        created_at (int):
        email (str):
        enable (bool):
        expiry_time (int):
        flow (str):
        forwarded_ports (str):
        group (str):
        id (int):
        keep_alive (int):
        limit_hwid (int):
        limit_ip (int):
        password (str):
        pre_shared_key (str):
        private_key (str):
        public_key (str):
        reset (int):
        reset_day (int):
        reset_max (int):
        reverse (Any):
        secret (str):
        security (str):
        sub_id (str):
        tg_id (int):
        total_gb (int):
        traffic_reset (str):
        traffic_reset_day (int):
        updated_at (int):
        uuid (str):
    """

    ad_tag: str
    allowed_i_ps: str
    auth: str
    comment: str
    created_at: int
    email: str
    enable: bool
    expiry_time: int
    flow: str
    forwarded_ports: str
    group: str
    id: int
    keep_alive: int
    limit_hwid: int
    limit_ip: int
    password: str
    pre_shared_key: str
    private_key: str
    public_key: str
    reset: int
    reset_day: int
    reset_max: int
    reverse: Any
    secret: str
    security: str
    sub_id: str
    tg_id: int
    total_gb: int
    traffic_reset: str
    traffic_reset_day: int
    updated_at: int
    uuid: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ad_tag = self.ad_tag

        allowed_i_ps = self.allowed_i_ps

        auth = self.auth

        comment = self.comment

        created_at = self.created_at

        email = self.email

        enable = self.enable

        expiry_time = self.expiry_time

        flow = self.flow

        forwarded_ports = self.forwarded_ports

        group = self.group

        id = self.id

        keep_alive = self.keep_alive

        limit_hwid = self.limit_hwid

        limit_ip = self.limit_ip

        password = self.password

        pre_shared_key = self.pre_shared_key

        private_key = self.private_key

        public_key = self.public_key

        reset = self.reset

        reset_day = self.reset_day

        reset_max = self.reset_max

        reverse = self.reverse

        secret = self.secret

        security = self.security

        sub_id = self.sub_id

        tg_id = self.tg_id

        total_gb = self.total_gb

        traffic_reset = self.traffic_reset

        traffic_reset_day = self.traffic_reset_day

        updated_at = self.updated_at

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "adTag": ad_tag,
                "allowedIPs": allowed_i_ps,
                "auth": auth,
                "comment": comment,
                "createdAt": created_at,
                "email": email,
                "enable": enable,
                "expiryTime": expiry_time,
                "flow": flow,
                "forwardedPorts": forwarded_ports,
                "group": group,
                "id": id,
                "keepAlive": keep_alive,
                "limitHwid": limit_hwid,
                "limitIp": limit_ip,
                "password": password,
                "preSharedKey": pre_shared_key,
                "privateKey": private_key,
                "publicKey": public_key,
                "reset": reset,
                "resetDay": reset_day,
                "resetMax": reset_max,
                "reverse": reverse,
                "secret": secret,
                "security": security,
                "subId": sub_id,
                "tgId": tg_id,
                "totalGB": total_gb,
                "trafficReset": traffic_reset,
                "trafficResetDay": traffic_reset_day,
                "updatedAt": updated_at,
                "uuid": uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ad_tag = d.pop("adTag")

        allowed_i_ps = d.pop("allowedIPs")

        auth = d.pop("auth")

        comment = d.pop("comment")

        created_at = d.pop("createdAt")

        email = d.pop("email")

        enable = d.pop("enable")

        expiry_time = d.pop("expiryTime")

        flow = d.pop("flow")

        forwarded_ports = d.pop("forwardedPorts")

        group = d.pop("group")

        id = d.pop("id")

        keep_alive = d.pop("keepAlive")

        limit_hwid = d.pop("limitHwid")

        limit_ip = d.pop("limitIp")

        password = d.pop("password")

        pre_shared_key = d.pop("preSharedKey")

        private_key = d.pop("privateKey")

        public_key = d.pop("publicKey")

        reset = d.pop("reset")

        reset_day = d.pop("resetDay")

        reset_max = d.pop("resetMax")

        reverse = d.pop("reverse")

        secret = d.pop("secret")

        security = d.pop("security")

        sub_id = d.pop("subId")

        tg_id = d.pop("tgId")

        total_gb = d.pop("totalGB")

        traffic_reset = d.pop("trafficReset")

        traffic_reset_day = d.pop("trafficResetDay")

        updated_at = d.pop("updatedAt")

        uuid = d.pop("uuid")

        client_record = cls(
            ad_tag=ad_tag,
            allowed_i_ps=allowed_i_ps,
            auth=auth,
            comment=comment,
            created_at=created_at,
            email=email,
            enable=enable,
            expiry_time=expiry_time,
            flow=flow,
            forwarded_ports=forwarded_ports,
            group=group,
            id=id,
            keep_alive=keep_alive,
            limit_hwid=limit_hwid,
            limit_ip=limit_ip,
            password=password,
            pre_shared_key=pre_shared_key,
            private_key=private_key,
            public_key=public_key,
            reset=reset,
            reset_day=reset_day,
            reset_max=reset_max,
            reverse=reverse,
            secret=secret,
            security=security,
            sub_id=sub_id,
            tg_id=tg_id,
            total_gb=total_gb,
            traffic_reset=traffic_reset,
            traffic_reset_day=traffic_reset_day,
            updated_at=updated_at,
            uuid=uuid,
        )

        client_record.additional_properties = d
        return client_record

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
