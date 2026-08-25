from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="InboundsFallbacksItem")


@_attrs_define
class InboundsFallbacksItem:
    """
    Attributes:
        id (int | Unset):
        master_id (int | Unset):
        child_id (int | Unset):
        name (str | Unset):
        alpn (str | Unset):
        path (str | Unset):
        dest (str | Unset):
        xver (int | Unset):
        sort_order (int | Unset):
    """

    id: int | Unset = UNSET
    master_id: int | Unset = UNSET
    child_id: int | Unset = UNSET
    name: str | Unset = UNSET
    alpn: str | Unset = UNSET
    path: str | Unset = UNSET
    dest: str | Unset = UNSET
    xver: int | Unset = UNSET
    sort_order: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        master_id = self.master_id

        child_id = self.child_id

        name = self.name

        alpn = self.alpn

        path = self.path

        dest = self.dest

        xver = self.xver

        sort_order = self.sort_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if master_id is not UNSET:
            field_dict["masterId"] = master_id
        if child_id is not UNSET:
            field_dict["childId"] = child_id
        if name is not UNSET:
            field_dict["name"] = name
        if alpn is not UNSET:
            field_dict["alpn"] = alpn
        if path is not UNSET:
            field_dict["path"] = path
        if dest is not UNSET:
            field_dict["dest"] = dest
        if xver is not UNSET:
            field_dict["xver"] = xver
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        master_id = d.pop("masterId", UNSET)

        child_id = d.pop("childId", UNSET)

        name = d.pop("name", UNSET)

        alpn = d.pop("alpn", UNSET)

        path = d.pop("path", UNSET)

        dest = d.pop("dest", UNSET)

        xver = d.pop("xver", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        inbounds_fallbacks_item = cls(
            id=id,
            master_id=master_id,
            child_id=child_id,
            name=name,
            alpn=alpn,
            path=path,
            dest=dest,
            xver=xver,
            sort_order=sort_order,
        )

        inbounds_fallbacks_item.additional_properties = d
        return inbounds_fallbacks_item

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
