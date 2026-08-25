from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientsListItemTraffic")


@_attrs_define
class ClientsListItemTraffic:
    """
    Attributes:
        up (int | Unset):
        down (int | Unset):
        enable (bool | Unset):
    """

    up: int | Unset = UNSET
    down: int | Unset = UNSET
    enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        up = self.up

        down = self.down

        enable = self.enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if up is not UNSET:
            field_dict["up"] = up
        if down is not UNSET:
            field_dict["down"] = down
        if enable is not UNSET:
            field_dict["enable"] = enable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        up = d.pop("up", UNSET)

        down = d.pop("down", UNSET)

        enable = d.pop("enable", UNSET)

        clients_list_item_traffic = cls(
            up=up,
            down=down,
            enable=enable,
        )

        clients_list_item_traffic.additional_properties = d
        return clients_list_item_traffic

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
