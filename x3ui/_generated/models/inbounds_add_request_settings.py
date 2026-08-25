from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inbounds_add_request_settings_clients_item import (
        InboundsAddRequestSettingsClientsItem,
    )


T = TypeVar("T", bound="InboundsAddRequestSettings")


@_attrs_define
class InboundsAddRequestSettings:
    """
    Attributes:
        clients (list[InboundsAddRequestSettingsClientsItem] | Unset):
        decryption (str | Unset):
        fallbacks (Any | Unset):
    """

    clients: list[InboundsAddRequestSettingsClientsItem] | Unset = UNSET
    decryption: str | Unset = UNSET
    fallbacks: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clients: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clients, Unset):
            clients = []
            for clients_item_data in self.clients:
                clients_item = clients_item_data.to_dict()
                clients.append(clients_item)

        decryption = self.decryption

        fallbacks = self.fallbacks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clients is not UNSET:
            field_dict["clients"] = clients
        if decryption is not UNSET:
            field_dict["decryption"] = decryption
        if fallbacks is not UNSET:
            field_dict["fallbacks"] = fallbacks

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.inbounds_add_request_settings_clients_item import (
            InboundsAddRequestSettingsClientsItem,
        )

        d = dict(src_dict)
        _clients = d.pop("clients", UNSET)
        clients: list[InboundsAddRequestSettingsClientsItem] | Unset = UNSET
        if _clients is not UNSET:
            clients = []
            for clients_item_data in _clients:
                clients_item = InboundsAddRequestSettingsClientsItem.from_dict(
                    clients_item_data
                )

                clients.append(clients_item)

        decryption = d.pop("decryption", UNSET)

        fallbacks = d.pop("fallbacks", UNSET)

        inbounds_add_request_settings = cls(
            clients=clients,
            decryption=decryption,
            fallbacks=fallbacks,
        )

        inbounds_add_request_settings.additional_properties = d
        return inbounds_add_request_settings

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
