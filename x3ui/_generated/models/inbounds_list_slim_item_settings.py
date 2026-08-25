from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inbounds_list_slim_item_settings_clients_item import (
        InboundsListSlimItemSettingsClientsItem,
    )


T = TypeVar("T", bound="InboundsListSlimItemSettings")


@_attrs_define
class InboundsListSlimItemSettings:
    """
    Attributes:
        clients (list[InboundsListSlimItemSettingsClientsItem] | Unset):
        decryption (str | Unset):
    """

    clients: list[InboundsListSlimItemSettingsClientsItem] | Unset = UNSET
    decryption: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clients: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clients, Unset):
            clients = []
            for clients_item_data in self.clients:
                clients_item = clients_item_data.to_dict()
                clients.append(clients_item)

        decryption = self.decryption

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clients is not UNSET:
            field_dict["clients"] = clients
        if decryption is not UNSET:
            field_dict["decryption"] = decryption

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.inbounds_list_slim_item_settings_clients_item import (
            InboundsListSlimItemSettingsClientsItem,
        )

        d = dict(src_dict)
        _clients = d.pop("clients", UNSET)
        clients: list[InboundsListSlimItemSettingsClientsItem] | Unset = UNSET
        if _clients is not UNSET:
            clients = []
            for clients_item_data in _clients:
                clients_item = InboundsListSlimItemSettingsClientsItem.from_dict(
                    clients_item_data
                )

                clients.append(clients_item)

        decryption = d.pop("decryption", UNSET)

        inbounds_list_slim_item_settings = cls(
            clients=clients,
            decryption=decryption,
        )

        inbounds_list_slim_item_settings.additional_properties = d
        return inbounds_list_slim_item_settings

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
