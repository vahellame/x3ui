from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_get_new_vless_enc_auths_item import (
        ServerGetNewVlessEncAuthsItem,
    )


T = TypeVar("T", bound="ServerGetNewVlessEnc")


@_attrs_define
class ServerGetNewVlessEnc:
    """
    Attributes:
        auths (list[ServerGetNewVlessEncAuthsItem] | Unset):
    """

    auths: list[ServerGetNewVlessEncAuthsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auths: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.auths, Unset):
            auths = []
            for auths_item_data in self.auths:
                auths_item = auths_item_data.to_dict()
                auths.append(auths_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auths is not UNSET:
            field_dict["auths"] = auths

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.server_get_new_vless_enc_auths_item import (
            ServerGetNewVlessEncAuthsItem,
        )

        d = dict(src_dict)
        _auths = d.pop("auths", UNSET)
        auths: list[ServerGetNewVlessEncAuthsItem] | Unset = UNSET
        if _auths is not UNSET:
            auths = []
            for auths_item_data in _auths:
                auths_item = ServerGetNewVlessEncAuthsItem.from_dict(auths_item_data)

                auths.append(auths_item)

        server_get_new_vless_enc = cls(
            auths=auths,
        )

        server_get_new_vless_enc.additional_properties = d
        return server_get_new_vless_enc

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
