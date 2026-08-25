from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientsGroupsRenameRequest")


@_attrs_define
class ClientsGroupsRenameRequest:
    """
    Attributes:
        old_name (str | Unset):
        new_name (str | Unset):
    """

    old_name: str | Unset = UNSET
    new_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        old_name = self.old_name

        new_name = self.new_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if old_name is not UNSET:
            field_dict["oldName"] = old_name
        if new_name is not UNSET:
            field_dict["newName"] = new_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        old_name = d.pop("oldName", UNSET)

        new_name = d.pop("newName", UNSET)

        clients_groups_rename_request = cls(
            old_name=old_name,
            new_name=new_name,
        )

        clients_groups_rename_request.additional_properties = d
        return clients_groups_rename_request

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
