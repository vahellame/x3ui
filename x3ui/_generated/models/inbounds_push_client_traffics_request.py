from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inbounds_push_client_traffics_request_traffics_item import (
        InboundsPushClientTrafficsRequestTrafficsItem,
    )


T = TypeVar("T", bound="InboundsPushClientTrafficsRequest")


@_attrs_define
class InboundsPushClientTrafficsRequest:
    """
    Attributes:
        master_guid (str | Unset):
        traffics (list[InboundsPushClientTrafficsRequestTrafficsItem] | Unset):
    """

    master_guid: str | Unset = UNSET
    traffics: list[InboundsPushClientTrafficsRequestTrafficsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        master_guid = self.master_guid

        traffics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.traffics, Unset):
            traffics = []
            for traffics_item_data in self.traffics:
                traffics_item = traffics_item_data.to_dict()
                traffics.append(traffics_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if master_guid is not UNSET:
            field_dict["masterGuid"] = master_guid
        if traffics is not UNSET:
            field_dict["traffics"] = traffics

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.inbounds_push_client_traffics_request_traffics_item import (
            InboundsPushClientTrafficsRequestTrafficsItem,
        )

        d = dict(src_dict)
        master_guid = d.pop("masterGuid", UNSET)

        _traffics = d.pop("traffics", UNSET)
        traffics: list[InboundsPushClientTrafficsRequestTrafficsItem] | Unset = UNSET
        if _traffics is not UNSET:
            traffics = []
            for traffics_item_data in _traffics:
                traffics_item = InboundsPushClientTrafficsRequestTrafficsItem.from_dict(
                    traffics_item_data
                )

                traffics.append(traffics_item)

        inbounds_push_client_traffics_request = cls(
            master_guid=master_guid,
            traffics=traffics,
        )

        inbounds_push_client_traffics_request.additional_properties = d
        return inbounds_push_client_traffics_request

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
