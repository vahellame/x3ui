from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientsExportItemClient")


@_attrs_define
class ClientsExportItemClient:
    """
    Attributes:
        email (str | Unset):
        id (str | Unset):
        total_gb (int | Unset):
        expiry_time (int | Unset):
        limit_hwid (int | Unset):
        enable (bool | Unset):
        sub_id (str | Unset):
    """

    email: str | Unset = UNSET
    id: str | Unset = UNSET
    total_gb: int | Unset = UNSET
    expiry_time: int | Unset = UNSET
    limit_hwid: int | Unset = UNSET
    enable: bool | Unset = UNSET
    sub_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        id = self.id

        total_gb = self.total_gb

        expiry_time = self.expiry_time

        limit_hwid = self.limit_hwid

        enable = self.enable

        sub_id = self.sub_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if id is not UNSET:
            field_dict["id"] = id
        if total_gb is not UNSET:
            field_dict["totalGB"] = total_gb
        if expiry_time is not UNSET:
            field_dict["expiryTime"] = expiry_time
        if limit_hwid is not UNSET:
            field_dict["limitHwid"] = limit_hwid
        if enable is not UNSET:
            field_dict["enable"] = enable
        if sub_id is not UNSET:
            field_dict["subId"] = sub_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        id = d.pop("id", UNSET)

        total_gb = d.pop("totalGB", UNSET)

        expiry_time = d.pop("expiryTime", UNSET)

        limit_hwid = d.pop("limitHwid", UNSET)

        enable = d.pop("enable", UNSET)

        sub_id = d.pop("subId", UNSET)

        clients_export_item_client = cls(
            email=email,
            id=id,
            total_gb=total_gb,
            expiry_time=expiry_time,
            limit_hwid=limit_hwid,
            enable=enable,
            sub_id=sub_id,
        )

        clients_export_item_client.additional_properties = d
        return clients_export_item_client

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
