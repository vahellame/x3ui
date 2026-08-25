from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="GeodataTokenIssue")


@_attrs_define
class GeodataTokenIssue:
    """GeodataTokenIssue reports a routing token the running core would reject,
    or would silently match nothing against.

        Attributes:
            reason (str):  Example: categoryMissing.
            token (str):  Example: geosite:blabla.
            code (str | Unset):  Example: blabla.
            file (str | Unset):  Example: geosite.dat.
    """

    reason: str
    token: str
    code: str | Unset = UNSET
    file: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        token = self.token

        code = self.code

        file = self.file

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
                "token": token,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        reason = d.pop("reason")

        token = d.pop("token")

        code = d.pop("code", UNSET)

        file = d.pop("file", UNSET)

        geodata_token_issue = cls(
            reason=reason,
            token=token,
            code=code,
            file=file,
        )

        geodata_token_issue.additional_properties = d
        return geodata_token_issue

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
