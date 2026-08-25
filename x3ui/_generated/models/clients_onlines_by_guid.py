from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientsOnlinesByGuid")


@_attrs_define
class ClientsOnlinesByGuid:
    """
    Attributes:
        a1b2 (list[str] | Unset):
        c3d4 (list[str] | Unset):
    """

    a1b2: list[str] | Unset = UNSET
    c3d4: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        a1b2: list[str] | Unset = UNSET
        if not isinstance(self.a1b2, Unset):
            a1b2 = self.a1b2

        c3d4: list[str] | Unset = UNSET
        if not isinstance(self.c3d4, Unset):
            c3d4 = self.c3d4

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if a1b2 is not UNSET:
            field_dict["a1b2-..."] = a1b2
        if c3d4 is not UNSET:
            field_dict["c3d4-..."] = c3d4

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        a1b2 = cast(list[str], d.pop("a1b2-...", UNSET))

        c3d4 = cast(list[str], d.pop("c3d4-...", UNSET))

        clients_onlines_by_guid = cls(
            a1b2=a1b2,
            c3d4=c3d4,
        )

        clients_onlines_by_guid.additional_properties = d
        return clients_onlines_by_guid

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
