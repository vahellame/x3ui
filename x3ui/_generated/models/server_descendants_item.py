from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerDescendantsItem")


@_attrs_define
class ServerDescendantsItem:
    """
    Attributes:
        guid (str | Unset):
        parent_guid (str | Unset):
        name (str | Unset):
        address (str | Unset):
        status (str | Unset):
    """

    guid: str | Unset = UNSET
    parent_guid: str | Unset = UNSET
    name: str | Unset = UNSET
    address: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        guid = self.guid

        parent_guid = self.parent_guid

        name = self.name

        address = self.address

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guid is not UNSET:
            field_dict["guid"] = guid
        if parent_guid is not UNSET:
            field_dict["parentGuid"] = parent_guid
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        guid = d.pop("guid", UNSET)

        parent_guid = d.pop("parentGuid", UNSET)

        name = d.pop("name", UNSET)

        address = d.pop("address", UNSET)

        status = d.pop("status", UNSET)

        server_descendants_item = cls(
            guid=guid,
            parent_guid=parent_guid,
            name=name,
            address=address,
            status=status,
        )

        server_descendants_item.additional_properties = d
        return server_descendants_item

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
