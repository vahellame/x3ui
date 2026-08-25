from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodesWebCert")


@_attrs_define
class NodesWebCert:
    """
    Attributes:
        web_cert_file (str | Unset):
        web_key_file (str | Unset):
    """

    web_cert_file: str | Unset = UNSET
    web_key_file: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        web_cert_file = self.web_cert_file

        web_key_file = self.web_key_file

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if web_cert_file is not UNSET:
            field_dict["webCertFile"] = web_cert_file
        if web_key_file is not UNSET:
            field_dict["webKeyFile"] = web_key_file

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        web_cert_file = d.pop("webCertFile", UNSET)

        web_key_file = d.pop("webKeyFile", UNSET)

        nodes_web_cert = cls(
            web_cert_file=web_cert_file,
            web_key_file=web_key_file,
        )

        nodes_web_cert.additional_properties = d
        return nodes_web_cert

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
