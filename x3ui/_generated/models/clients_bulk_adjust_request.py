from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientsBulkAdjustRequest")


@_attrs_define
class ClientsBulkAdjustRequest:
    """
    Attributes:
        emails (list[str] | Unset):
        add_days (int | Unset):
        add_bytes (int | Unset):
        flow (str | Unset):
    """

    emails: list[str] | Unset = UNSET
    add_days: int | Unset = UNSET
    add_bytes: int | Unset = UNSET
    flow: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        emails: list[str] | Unset = UNSET
        if not isinstance(self.emails, Unset):
            emails = self.emails

        add_days = self.add_days

        add_bytes = self.add_bytes

        flow = self.flow

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if emails is not UNSET:
            field_dict["emails"] = emails
        if add_days is not UNSET:
            field_dict["addDays"] = add_days
        if add_bytes is not UNSET:
            field_dict["addBytes"] = add_bytes
        if flow is not UNSET:
            field_dict["flow"] = flow

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        emails = cast(list[str], d.pop("emails", UNSET))

        add_days = d.pop("addDays", UNSET)

        add_bytes = d.pop("addBytes", UNSET)

        flow = d.pop("flow", UNSET)

        clients_bulk_adjust_request = cls(
            emails=emails,
            add_days=add_days,
            add_bytes=add_bytes,
            flow=flow,
        )

        clients_bulk_adjust_request.additional_properties = d
        return clients_bulk_adjust_request

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
