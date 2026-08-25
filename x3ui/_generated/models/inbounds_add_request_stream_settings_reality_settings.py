from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="InboundsAddRequestStreamSettingsRealitySettings")


@_attrs_define
class InboundsAddRequestStreamSettingsRealitySettings:
    """
    Attributes:
        show (bool | Unset):
        dest (str | Unset):
    """

    show: bool | Unset = UNSET
    dest: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        show = self.show

        dest = self.dest

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if show is not UNSET:
            field_dict["show"] = show
        if dest is not UNSET:
            field_dict["dest"] = dest

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        show = d.pop("show", UNSET)

        dest = d.pop("dest", UNSET)

        inbounds_add_request_stream_settings_reality_settings = cls(
            show=show,
            dest=dest,
        )

        inbounds_add_request_stream_settings_reality_settings.additional_properties = d
        return inbounds_add_request_stream_settings_reality_settings

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
