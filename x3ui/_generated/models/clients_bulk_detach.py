from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientsBulkDetach")


@_attrs_define
class ClientsBulkDetach:
    """
    Attributes:
        detached (list[str] | Unset):
        skipped (Any | Unset):
        errors (Any | Unset):
    """

    detached: list[str] | Unset = UNSET
    skipped: Any | Unset = UNSET
    errors: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detached: list[str] | Unset = UNSET
        if not isinstance(self.detached, Unset):
            detached = self.detached

        skipped = self.skipped

        errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if detached is not UNSET:
            field_dict["detached"] = detached
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        detached = cast(list[str], d.pop("detached", UNSET))

        skipped = d.pop("skipped", UNSET)

        errors = d.pop("errors", UNSET)

        clients_bulk_detach = cls(
            detached=detached,
            skipped=skipped,
            errors=errors,
        )

        clients_bulk_detach.additional_properties = d
        return clients_bulk_detach

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
