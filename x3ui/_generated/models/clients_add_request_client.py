from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientsAddRequestClient")


@_attrs_define
class ClientsAddRequestClient:
    """
    Attributes:
        email (str | Unset):
        total_gb (int | Unset):
        expiry_time (int | Unset):
        tg_id (int | Unset):
        limit_ip (int | Unset):
        limit_hwid (int | Unset):
        enable (bool | Unset):
    """

    email: str | Unset = UNSET
    total_gb: int | Unset = UNSET
    expiry_time: int | Unset = UNSET
    tg_id: int | Unset = UNSET
    limit_ip: int | Unset = UNSET
    limit_hwid: int | Unset = UNSET
    enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        total_gb = self.total_gb

        expiry_time = self.expiry_time

        tg_id = self.tg_id

        limit_ip = self.limit_ip

        limit_hwid = self.limit_hwid

        enable = self.enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if total_gb is not UNSET:
            field_dict["totalGB"] = total_gb
        if expiry_time is not UNSET:
            field_dict["expiryTime"] = expiry_time
        if tg_id is not UNSET:
            field_dict["tgId"] = tg_id
        if limit_ip is not UNSET:
            field_dict["limitIp"] = limit_ip
        if limit_hwid is not UNSET:
            field_dict["limitHwid"] = limit_hwid
        if enable is not UNSET:
            field_dict["enable"] = enable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        total_gb = d.pop("totalGB", UNSET)

        expiry_time = d.pop("expiryTime", UNSET)

        tg_id = d.pop("tgId", UNSET)

        limit_ip = d.pop("limitIp", UNSET)

        limit_hwid = d.pop("limitHwid", UNSET)

        enable = d.pop("enable", UNSET)

        clients_add_request_client = cls(
            email=email,
            total_gb=total_gb,
            expiry_time=expiry_time,
            tg_id=tg_id,
            limit_ip=limit_ip,
            limit_hwid=limit_hwid,
            enable=enable,
        )

        clients_add_request_client.additional_properties = d
        return clients_add_request_client

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
