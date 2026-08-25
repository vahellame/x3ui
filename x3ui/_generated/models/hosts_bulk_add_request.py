from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostsBulkAddRequest")


@_attrs_define
class HostsBulkAddRequest:
    """
    Attributes:
        inbound_ids (list[int] | Unset):
        hosts (list[str] | Unset):
        remark (str | Unset):
        port (int | Unset):
        security (str | Unset):
        is_disabled (bool | Unset):
    """

    inbound_ids: list[int] | Unset = UNSET
    hosts: list[str] | Unset = UNSET
    remark: str | Unset = UNSET
    port: int | Unset = UNSET
    security: str | Unset = UNSET
    is_disabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inbound_ids: list[int] | Unset = UNSET
        if not isinstance(self.inbound_ids, Unset):
            inbound_ids = self.inbound_ids

        hosts: list[str] | Unset = UNSET
        if not isinstance(self.hosts, Unset):
            hosts = self.hosts

        remark = self.remark

        port = self.port

        security = self.security

        is_disabled = self.is_disabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inbound_ids is not UNSET:
            field_dict["inboundIds"] = inbound_ids
        if hosts is not UNSET:
            field_dict["hosts"] = hosts
        if remark is not UNSET:
            field_dict["remark"] = remark
        if port is not UNSET:
            field_dict["port"] = port
        if security is not UNSET:
            field_dict["security"] = security
        if is_disabled is not UNSET:
            field_dict["isDisabled"] = is_disabled

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        inbound_ids = cast(list[int], d.pop("inboundIds", UNSET))

        hosts = cast(list[str], d.pop("hosts", UNSET))

        remark = d.pop("remark", UNSET)

        port = d.pop("port", UNSET)

        security = d.pop("security", UNSET)

        is_disabled = d.pop("isDisabled", UNSET)

        hosts_bulk_add_request = cls(
            inbound_ids=inbound_ids,
            hosts=hosts,
            remark=remark,
            port=port,
            security=security,
            is_disabled=is_disabled,
        )

        hosts_bulk_add_request.additional_properties = d
        return hosts_bulk_add_request

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
