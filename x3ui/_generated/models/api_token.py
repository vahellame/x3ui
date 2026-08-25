from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="ApiToken")


@_attrs_define
class ApiToken:
    """
    Attributes:
        created_at (int):
        enabled (bool):
        expires_at (int):
        id (int):
        name (str):
        scope (str):
        token (str): SHA-256 hash; the plaintext is shown only once at creation
    """

    created_at: int
    enabled: bool
    expires_at: int
    id: int
    name: str
    scope: str
    token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        enabled = self.enabled

        expires_at = self.expires_at

        id = self.id

        name = self.name

        scope = self.scope

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "enabled": enabled,
                "expiresAt": expires_at,
                "id": id,
                "name": name,
                "scope": scope,
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = d.pop("createdAt")

        enabled = d.pop("enabled")

        expires_at = d.pop("expiresAt")

        id = d.pop("id")

        name = d.pop("name")

        scope = d.pop("scope")

        token = d.pop("token")

        api_token = cls(
            created_at=created_at,
            enabled=enabled,
            expires_at=expires_at,
            id=id,
            name=name,
            scope=scope,
            token=token,
        )

        api_token.additional_properties = d
        return api_token

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
