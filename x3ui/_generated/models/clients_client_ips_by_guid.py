from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clients_client_ips_by_guid_a1b2 import ClientsClientIpsByGuidA1B2


T = TypeVar("T", bound="ClientsClientIpsByGuid")


@_attrs_define
class ClientsClientIpsByGuid:
    """
    Attributes:
        a1b2 (ClientsClientIpsByGuidA1B2 | Unset):
    """

    a1b2: ClientsClientIpsByGuidA1B2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        a1b2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.a1b2, Unset):
            a1b2 = self.a1b2.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if a1b2 is not UNSET:
            field_dict["a1b2-..."] = a1b2

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.clients_client_ips_by_guid_a1b2 import ClientsClientIpsByGuidA1B2

        d = dict(src_dict)
        _a1b2 = d.pop("a1b2-...", UNSET)
        a1b2: ClientsClientIpsByGuidA1B2 | Unset
        if isinstance(_a1b2, Unset):
            a1b2 = UNSET
        else:
            a1b2 = ClientsClientIpsByGuidA1B2.from_dict(_a1b2)

        clients_client_ips_by_guid = cls(
            a1b2=a1b2,
        )

        clients_client_ips_by_guid.additional_properties = d
        return clients_client_ips_by_guid

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
