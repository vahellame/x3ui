from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientsHwidsItem")


@_attrs_define
class ClientsHwidsItem:
    """
    Attributes:
        id (int | Unset):
        first_seen (int | Unset):
        last_seen (int | Unset):
        user_agent (str | Unset):
        device_os (str | Unset):
        os_version (str | Unset):
        device_model (str | Unset):
    """

    id: int | Unset = UNSET
    first_seen: int | Unset = UNSET
    last_seen: int | Unset = UNSET
    user_agent: str | Unset = UNSET
    device_os: str | Unset = UNSET
    os_version: str | Unset = UNSET
    device_model: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        first_seen = self.first_seen

        last_seen = self.last_seen

        user_agent = self.user_agent

        device_os = self.device_os

        os_version = self.os_version

        device_model = self.device_model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if first_seen is not UNSET:
            field_dict["firstSeen"] = first_seen
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if user_agent is not UNSET:
            field_dict["userAgent"] = user_agent
        if device_os is not UNSET:
            field_dict["deviceOs"] = device_os
        if os_version is not UNSET:
            field_dict["osVersion"] = os_version
        if device_model is not UNSET:
            field_dict["deviceModel"] = device_model

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        first_seen = d.pop("firstSeen", UNSET)

        last_seen = d.pop("lastSeen", UNSET)

        user_agent = d.pop("userAgent", UNSET)

        device_os = d.pop("deviceOs", UNSET)

        os_version = d.pop("osVersion", UNSET)

        device_model = d.pop("deviceModel", UNSET)

        clients_hwids_item = cls(
            id=id,
            first_seen=first_seen,
            last_seen=last_seen,
            user_agent=user_agent,
            device_os=device_os,
            os_version=os_version,
            device_model=device_model,
        )

        clients_hwids_item.additional_properties = d
        return clients_hwids_item

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
