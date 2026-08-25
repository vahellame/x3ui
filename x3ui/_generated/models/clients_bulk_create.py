from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clients_bulk_create_skipped_item import ClientsBulkCreateSkippedItem


T = TypeVar("T", bound="ClientsBulkCreate")


@_attrs_define
class ClientsBulkCreate:
    """
    Attributes:
        created (int | Unset):
        skipped (list[ClientsBulkCreateSkippedItem] | Unset):
    """

    created: int | Unset = UNSET
    skipped: list[ClientsBulkCreateSkippedItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        skipped: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skipped, Unset):
            skipped = []
            for skipped_item_data in self.skipped:
                skipped_item = skipped_item_data.to_dict()
                skipped.append(skipped_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if skipped is not UNSET:
            field_dict["skipped"] = skipped

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.clients_bulk_create_skipped_item import (
            ClientsBulkCreateSkippedItem,
        )

        d = dict(src_dict)
        created = d.pop("created", UNSET)

        _skipped = d.pop("skipped", UNSET)
        skipped: list[ClientsBulkCreateSkippedItem] | Unset = UNSET
        if _skipped is not UNSET:
            skipped = []
            for skipped_item_data in _skipped:
                skipped_item = ClientsBulkCreateSkippedItem.from_dict(skipped_item_data)

                skipped.append(skipped_item)

        clients_bulk_create = cls(
            created=created,
            skipped=skipped,
        )

        clients_bulk_create.additional_properties = d
        return clients_bulk_create

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
