from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerStatusLoad")


@_attrs_define
class ServerStatusLoad:
    """
    Attributes:
        load1 (float | Unset):
        load5 (float | Unset):
        load15 (float | Unset):
    """

    load1: float | Unset = UNSET
    load5: float | Unset = UNSET
    load15: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        load1 = self.load1

        load5 = self.load5

        load15 = self.load15

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if load1 is not UNSET:
            field_dict["load1"] = load1
        if load5 is not UNSET:
            field_dict["load5"] = load5
        if load15 is not UNSET:
            field_dict["load15"] = load15

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        load1 = d.pop("load1", UNSET)

        load5 = d.pop("load5", UNSET)

        load15 = d.pop("load15", UNSET)

        server_status_load = cls(
            load1=load1,
            load5=load5,
            load15=load15,
        )

        server_status_load.additional_properties = d
        return server_status_load

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
