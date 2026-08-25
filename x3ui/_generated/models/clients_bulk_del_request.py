from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientsBulkDelRequest")


@_attrs_define
class ClientsBulkDelRequest:
    """
    Attributes:
        emails (list[str] | Unset):
        keep_traffic (bool | Unset):
    """

    emails: list[str] | Unset = UNSET
    keep_traffic: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        emails: list[str] | Unset = UNSET
        if not isinstance(self.emails, Unset):
            emails = self.emails

        keep_traffic = self.keep_traffic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if emails is not UNSET:
            field_dict["emails"] = emails
        if keep_traffic is not UNSET:
            field_dict["keepTraffic"] = keep_traffic

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        emails = cast(list[str], d.pop("emails", UNSET))

        keep_traffic = d.pop("keepTraffic", UNSET)

        clients_bulk_del_request = cls(
            emails=emails,
            keep_traffic=keep_traffic,
        )

        clients_bulk_del_request.additional_properties = d
        return clients_bulk_del_request

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
