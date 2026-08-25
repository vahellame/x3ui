from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inbounds_fallbacks_request_fallbacks_item import (
        InboundsFallbacksRequestFallbacksItem,
    )


T = TypeVar("T", bound="InboundsFallbacksRequest")


@_attrs_define
class InboundsFallbacksRequest:
    """
    Attributes:
        fallbacks (list[InboundsFallbacksRequestFallbacksItem] | Unset):
    """

    fallbacks: list[InboundsFallbacksRequestFallbacksItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fallbacks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fallbacks, Unset):
            fallbacks = []
            for fallbacks_item_data in self.fallbacks:
                fallbacks_item = fallbacks_item_data.to_dict()
                fallbacks.append(fallbacks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fallbacks is not UNSET:
            field_dict["fallbacks"] = fallbacks

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.inbounds_fallbacks_request_fallbacks_item import (
            InboundsFallbacksRequestFallbacksItem,
        )

        d = dict(src_dict)
        _fallbacks = d.pop("fallbacks", UNSET)
        fallbacks: list[InboundsFallbacksRequestFallbacksItem] | Unset = UNSET
        if _fallbacks is not UNSET:
            fallbacks = []
            for fallbacks_item_data in _fallbacks:
                fallbacks_item = InboundsFallbacksRequestFallbacksItem.from_dict(
                    fallbacks_item_data
                )

                fallbacks.append(fallbacks_item)

        inbounds_fallbacks_request = cls(
            fallbacks=fallbacks,
        )

        inbounds_fallbacks_request.additional_properties = d
        return inbounds_fallbacks_request

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
