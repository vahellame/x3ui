from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientsUpdateTrafficRequest")


@_attrs_define
class ClientsUpdateTrafficRequest:
    """
    Attributes:
        upload (int | Unset):
        download (int | Unset):
    """

    upload: int | Unset = UNSET
    download: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload = self.upload

        download = self.download

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if upload is not UNSET:
            field_dict["upload"] = upload
        if download is not UNSET:
            field_dict["download"] = download

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        upload = d.pop("upload", UNSET)

        download = d.pop("download", UNSET)

        clients_update_traffic_request = cls(
            upload=upload,
            download=download,
        )

        clients_update_traffic_request.additional_properties = d
        return clients_update_traffic_request

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
