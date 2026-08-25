from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientsBulkAttachRequest")


@_attrs_define
class ClientsBulkAttachRequest:
    """
    Attributes:
        emails (list[str] | Unset):
        inbound_ids (list[int] | Unset):
    """

    emails: list[str] | Unset = UNSET
    inbound_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        emails: list[str] | Unset = UNSET
        if not isinstance(self.emails, Unset):
            emails = self.emails

        inbound_ids: list[int] | Unset = UNSET
        if not isinstance(self.inbound_ids, Unset):
            inbound_ids = self.inbound_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if emails is not UNSET:
            field_dict["emails"] = emails
        if inbound_ids is not UNSET:
            field_dict["inboundIds"] = inbound_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        emails = cast(list[str], d.pop("emails", UNSET))

        inbound_ids = cast(list[int], d.pop("inboundIds", UNSET))

        clients_bulk_attach_request = cls(
            emails=emails,
            inbound_ids=inbound_ids,
        )

        clients_bulk_attach_request.additional_properties = d
        return clients_bulk_attach_request

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
