from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodesInboundsItem")


@_attrs_define
class NodesInboundsItem:
    """
    Attributes:
        tag (str | Unset):
        remark (str | Unset):
        protocol (str | Unset):
        port (int | Unset):
    """

    tag: str | Unset = UNSET
    remark: str | Unset = UNSET
    protocol: str | Unset = UNSET
    port: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag = self.tag

        remark = self.remark

        protocol = self.protocol

        port = self.port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tag is not UNSET:
            field_dict["tag"] = tag
        if remark is not UNSET:
            field_dict["remark"] = remark
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if port is not UNSET:
            field_dict["port"] = port

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tag = d.pop("tag", UNSET)

        remark = d.pop("remark", UNSET)

        protocol = d.pop("protocol", UNSET)

        port = d.pop("port", UNSET)

        nodes_inbounds_item = cls(
            tag=tag,
            remark=remark,
            protocol=protocol,
            port=port,
        )

        nodes_inbounds_item.additional_properties = d
        return nodes_inbounds_item

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
