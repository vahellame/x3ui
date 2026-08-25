from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="InboundsPushClientTrafficsRequestTrafficsItem")


@_attrs_define
class InboundsPushClientTrafficsRequestTrafficsItem:
    """
    Attributes:
        email (str | Unset):
        up (int | Unset):
        down (int | Unset):
    """

    email: str | Unset = UNSET
    up: int | Unset = UNSET
    down: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        up = self.up

        down = self.down

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if up is not UNSET:
            field_dict["up"] = up
        if down is not UNSET:
            field_dict["down"] = down

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        up = d.pop("up", UNSET)

        down = d.pop("down", UNSET)

        inbounds_push_client_traffics_request_traffics_item = cls(
            email=email,
            up=up,
            down=down,
        )

        inbounds_push_client_traffics_request_traffics_item.additional_properties = d
        return inbounds_push_client_traffics_request_traffics_item

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
