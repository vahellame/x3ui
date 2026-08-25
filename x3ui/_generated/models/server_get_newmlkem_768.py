from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerGetNewmlkem768")


@_attrs_define
class ServerGetNewmlkem768:
    """
    Attributes:
        client_key (str | Unset):
        server_key (str | Unset):
    """

    client_key: str | Unset = UNSET
    server_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_key = self.client_key

        server_key = self.server_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_key is not UNSET:
            field_dict["clientKey"] = client_key
        if server_key is not UNSET:
            field_dict["serverKey"] = server_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        client_key = d.pop("clientKey", UNSET)

        server_key = d.pop("serverKey", UNSET)

        server_get_newmlkem_768 = cls(
            client_key=client_key,
            server_key=server_key,
        )

        server_get_newmlkem_768.additional_properties = d
        return server_get_newmlkem_768

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
