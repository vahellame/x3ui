from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientsBulkAttach")


@_attrs_define
class ClientsBulkAttach:
    """
    Attributes:
        attached (list[str] | Unset):
        skipped (list[str] | Unset):
        errors (Any | Unset):
    """

    attached: list[str] | Unset = UNSET
    skipped: list[str] | Unset = UNSET
    errors: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attached: list[str] | Unset = UNSET
        if not isinstance(self.attached, Unset):
            attached = self.attached

        skipped: list[str] | Unset = UNSET
        if not isinstance(self.skipped, Unset):
            skipped = self.skipped

        errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attached is not UNSET:
            field_dict["attached"] = attached
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        attached = cast(list[str], d.pop("attached", UNSET))

        skipped = cast(list[str], d.pop("skipped", UNSET))

        errors = d.pop("errors", UNSET)

        clients_bulk_attach = cls(
            attached=attached,
            skipped=skipped,
            errors=errors,
        )

        clients_bulk_attach.additional_properties = d
        return clients_bulk_attach

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
