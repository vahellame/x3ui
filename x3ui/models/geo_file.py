from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="GeoFile")


@_attrs_define
class GeoFile:
    """GeoFile describes one .dat database found in the asset directory.

    Attributes:
        categories (int):  Example: 1043.
        kind (str):  Example: site.
        modified_at (int):  Example: 1769558400000.
        name (str):  Example: geosite.dat.
        size (int):  Example: 1467392.
        error (str | Unset):
    """

    categories: int
    kind: str
    modified_at: int
    name: str
    size: int
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        categories = self.categories

        kind = self.kind

        modified_at = self.modified_at

        name = self.name

        size = self.size

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "categories": categories,
                "kind": kind,
                "modifiedAt": modified_at,
                "name": name,
                "size": size,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        categories = d.pop("categories")

        kind = d.pop("kind")

        modified_at = d.pop("modifiedAt")

        name = d.pop("name")

        size = d.pop("size")

        error = d.pop("error", UNSET)

        geo_file = cls(
            categories=categories,
            kind=kind,
            modified_at=modified_at,
            name=name,
            size=size,
            error=error,
        )

        geo_file.additional_properties = d
        return geo_file

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
