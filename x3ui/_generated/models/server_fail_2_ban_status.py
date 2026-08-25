from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerFail2BanStatus")


@_attrs_define
class ServerFail2BanStatus:
    """
    Attributes:
        enabled (bool | Unset):
        installed (bool | Unset):
        usable (bool | Unset):
        windows (bool | Unset):
    """

    enabled: bool | Unset = UNSET
    installed: bool | Unset = UNSET
    usable: bool | Unset = UNSET
    windows: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        installed = self.installed

        usable = self.usable

        windows = self.windows

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if installed is not UNSET:
            field_dict["installed"] = installed
        if usable is not UNSET:
            field_dict["usable"] = usable
        if windows is not UNSET:
            field_dict["windows"] = windows

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        installed = d.pop("installed", UNSET)

        usable = d.pop("usable", UNSET)

        windows = d.pop("windows", UNSET)

        server_fail_2_ban_status = cls(
            enabled=enabled,
            installed=installed,
            usable=usable,
            windows=windows,
        )

        server_fail_2_ban_status.additional_properties = d
        return server_fail_2_ban_status

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
