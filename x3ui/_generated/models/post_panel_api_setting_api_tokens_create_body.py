from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="PostPanelApiSettingApiTokensCreateBody")


@_attrs_define
class PostPanelApiSettingApiTokensCreateBody:
    """
    Attributes:
        name (str): Human-readable label, e.g. "central-panel-a".
        scope (str): admin (default), monitor, or node-sync.
        expires_at (int): Future Unix milliseconds, or 0 for no expiry.
    """

    name: str
    scope: str
    expires_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        scope = self.scope

        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "scope": scope,
                "expiresAt": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        scope = d.pop("scope")

        expires_at = d.pop("expiresAt")

        post_panel_api_setting_api_tokens_create_body = cls(
            name=name,
            scope=scope,
            expires_at=expires_at,
        )

        post_panel_api_setting_api_tokens_create_body.additional_properties = d
        return post_panel_api_setting_api_tokens_create_body

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
