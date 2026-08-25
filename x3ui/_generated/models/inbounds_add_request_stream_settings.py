from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inbounds_add_request_stream_settings_reality_settings import (
        InboundsAddRequestStreamSettingsRealitySettings,
    )


T = TypeVar("T", bound="InboundsAddRequestStreamSettings")


@_attrs_define
class InboundsAddRequestStreamSettings:
    """
    Attributes:
        network (str | Unset):
        security (str | Unset):
        reality_settings (InboundsAddRequestStreamSettingsRealitySettings | Unset):
    """

    network: str | Unset = UNSET
    security: str | Unset = UNSET
    reality_settings: InboundsAddRequestStreamSettingsRealitySettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network = self.network

        security = self.security

        reality_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reality_settings, Unset):
            reality_settings = self.reality_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network is not UNSET:
            field_dict["network"] = network
        if security is not UNSET:
            field_dict["security"] = security
        if reality_settings is not UNSET:
            field_dict["realitySettings"] = reality_settings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.inbounds_add_request_stream_settings_reality_settings import (
            InboundsAddRequestStreamSettingsRealitySettings,
        )

        d = dict(src_dict)
        network = d.pop("network", UNSET)

        security = d.pop("security", UNSET)

        _reality_settings = d.pop("realitySettings", UNSET)
        reality_settings: InboundsAddRequestStreamSettingsRealitySettings | Unset
        if isinstance(_reality_settings, Unset):
            reality_settings = UNSET
        else:
            reality_settings = (
                InboundsAddRequestStreamSettingsRealitySettings.from_dict(
                    _reality_settings
                )
            )

        inbounds_add_request_stream_settings = cls(
            network=network,
            security=security,
            reality_settings=reality_settings,
        )

        inbounds_add_request_stream_settings.additional_properties = d
        return inbounds_add_request_stream_settings

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
