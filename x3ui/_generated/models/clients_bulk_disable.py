from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clients_bulk_disable_skipped_item import ClientsBulkDisableSkippedItem


T = TypeVar("T", bound="ClientsBulkDisable")


@_attrs_define
class ClientsBulkDisable:
    """
    Attributes:
        changed (int | Unset):
        skipped (list[ClientsBulkDisableSkippedItem] | Unset):
    """

    changed: int | Unset = UNSET
    skipped: list[ClientsBulkDisableSkippedItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        changed = self.changed

        skipped: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skipped, Unset):
            skipped = []
            for skipped_item_data in self.skipped:
                skipped_item = skipped_item_data.to_dict()
                skipped.append(skipped_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if changed is not UNSET:
            field_dict["changed"] = changed
        if skipped is not UNSET:
            field_dict["skipped"] = skipped

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.clients_bulk_disable_skipped_item import (
            ClientsBulkDisableSkippedItem,
        )

        d = dict(src_dict)
        changed = d.pop("changed", UNSET)

        _skipped = d.pop("skipped", UNSET)
        skipped: list[ClientsBulkDisableSkippedItem] | Unset = UNSET
        if _skipped is not UNSET:
            skipped = []
            for skipped_item_data in _skipped:
                skipped_item = ClientsBulkDisableSkippedItem.from_dict(
                    skipped_item_data
                )

                skipped.append(skipped_item)

        clients_bulk_disable = cls(
            changed=changed,
            skipped=skipped,
        )

        clients_bulk_disable.additional_properties = d
        return clients_bulk_disable

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
