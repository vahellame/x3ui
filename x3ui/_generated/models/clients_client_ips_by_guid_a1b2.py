from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clients_client_ips_by_guid_a1b2_user_1_item import (
        ClientsClientIpsByGuidA1B2User1Item,
    )


T = TypeVar("T", bound="ClientsClientIpsByGuidA1B2")


@_attrs_define
class ClientsClientIpsByGuidA1B2:
    """
    Attributes:
        user1 (list[ClientsClientIpsByGuidA1B2User1Item] | Unset):
    """

    user1: list[ClientsClientIpsByGuidA1B2User1Item] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user1: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user1, Unset):
            user1 = []
            for user1_item_data in self.user1:
                user1_item = user1_item_data.to_dict()
                user1.append(user1_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user1 is not UNSET:
            field_dict["user1"] = user1

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.clients_client_ips_by_guid_a1b2_user_1_item import (
            ClientsClientIpsByGuidA1B2User1Item,
        )

        d = dict(src_dict)
        _user1 = d.pop("user1", UNSET)
        user1: list[ClientsClientIpsByGuidA1B2User1Item] | Unset = UNSET
        if _user1 is not UNSET:
            user1 = []
            for user1_item_data in _user1:
                user1_item = ClientsClientIpsByGuidA1B2User1Item.from_dict(
                    user1_item_data
                )

                user1.append(user1_item)

        clients_client_ips_by_guid_a1b2 = cls(
            user1=user1,
        )

        clients_client_ips_by_guid_a1b2.additional_properties = d
        return clients_client_ips_by_guid_a1b2

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
