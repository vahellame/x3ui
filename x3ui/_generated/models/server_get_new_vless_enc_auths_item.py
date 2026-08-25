from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerGetNewVlessEncAuthsItem")


@_attrs_define
class ServerGetNewVlessEncAuthsItem:
    """
    Attributes:
        id (int | Unset):
        label (str | Unset):
        encryption (str | Unset):
        decryption (str | Unset):
    """

    id: int | Unset = UNSET
    label: str | Unset = UNSET
    encryption: str | Unset = UNSET
    decryption: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        encryption = self.encryption

        decryption = self.decryption

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if encryption is not UNSET:
            field_dict["encryption"] = encryption
        if decryption is not UNSET:
            field_dict["decryption"] = decryption

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        encryption = d.pop("encryption", UNSET)

        decryption = d.pop("decryption", UNSET)

        server_get_new_vless_enc_auths_item = cls(
            id=id,
            label=label,
            encryption=encryption,
            decryption=decryption,
        )

        server_get_new_vless_enc_auths_item.additional_properties = d
        return server_get_new_vless_enc_auths_item

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
