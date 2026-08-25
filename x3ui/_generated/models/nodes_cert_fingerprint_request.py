from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodesCertFingerprintRequest")


@_attrs_define
class NodesCertFingerprintRequest:
    """
    Attributes:
        scheme (str | Unset):
        address (str | Unset):
        port (int | Unset):
        base_path (str | Unset):
    """

    scheme: str | Unset = UNSET
    address: str | Unset = UNSET
    port: int | Unset = UNSET
    base_path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scheme = self.scheme

        address = self.address

        port = self.port

        base_path = self.base_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scheme is not UNSET:
            field_dict["scheme"] = scheme
        if address is not UNSET:
            field_dict["address"] = address
        if port is not UNSET:
            field_dict["port"] = port
        if base_path is not UNSET:
            field_dict["basePath"] = base_path

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        scheme = d.pop("scheme", UNSET)

        address = d.pop("address", UNSET)

        port = d.pop("port", UNSET)

        base_path = d.pop("basePath", UNSET)

        nodes_cert_fingerprint_request = cls(
            scheme=scheme,
            address=address,
            port=port,
            base_path=base_path,
        )

        nodes_cert_fingerprint_request.additional_properties = d
        return nodes_cert_fingerprint_request

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
