from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="InboundsSubSortIndexRequest")


@_attrs_define
class InboundsSubSortIndexRequest:
    """
    Attributes:
        sub_sort_index (int | Unset):
    """

    sub_sort_index: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sub_sort_index = self.sub_sort_index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sub_sort_index is not UNSET:
            field_dict["subSortIndex"] = sub_sort_index

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        sub_sort_index = d.pop("subSortIndex", UNSET)

        inbounds_sub_sort_index_request = cls(
            sub_sort_index=sub_sort_index,
        )

        inbounds_sub_sort_index_request.additional_properties = d
        return inbounds_sub_sort_index_request

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
