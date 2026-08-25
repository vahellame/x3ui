from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientsClientIpsByGuidA1B2User1Item")


@_attrs_define
class ClientsClientIpsByGuidA1B2User1Item:
    """
    Attributes:
        ip (str | Unset):
        timestamp (int | Unset):
    """

    ip: str | Unset = UNSET
    timestamp: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip = self.ip

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ip is not UNSET:
            field_dict["ip"] = ip
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ip = d.pop("ip", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        clients_client_ips_by_guid_a1b2_user_1_item = cls(
            ip=ip,
            timestamp=timestamp,
        )

        clients_client_ips_by_guid_a1b2_user_1_item.additional_properties = d
        return clients_client_ips_by_guid_a1b2_user_1_item

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
