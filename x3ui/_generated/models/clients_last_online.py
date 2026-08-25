from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientsLastOnline")


@_attrs_define
class ClientsLastOnline:
    """
    Attributes:
        user1 (int | Unset):
        user2 (int | Unset):
    """

    user1: int | Unset = UNSET
    user2: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user1 = self.user1

        user2 = self.user2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user1 is not UNSET:
            field_dict["user1"] = user1
        if user2 is not UNSET:
            field_dict["user2"] = user2

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        user1 = d.pop("user1", UNSET)

        user2 = d.pop("user2", UNSET)

        clients_last_online = cls(
            user1=user1,
            user2=user2,
        )

        clients_last_online.additional_properties = d
        return clients_last_online

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
