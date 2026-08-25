from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="GeoCategory")


@_attrs_define
class GeoCategory:
    """GeoCategory is one code inside a database, such as geosite's "google".

    Attributes:
        attributes (list[str]):  Example: ['ads', 'cn'].
        code (str):  Example: google.
        entries (int):  Example: 1284.
    """

    attributes: list[str]
    code: str
    entries: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes = self.attributes

        code = self.code

        entries = self.entries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
                "code": code,
                "entries": entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        attributes = cast(list[str], d.pop("attributes"))

        code = d.pop("code")

        entries = d.pop("entries")

        geo_category = cls(
            attributes=attributes,
            code=code,
            entries=entries,
        )

        geo_category.additional_properties = d
        return geo_category

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
