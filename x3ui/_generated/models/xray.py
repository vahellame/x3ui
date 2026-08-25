from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Xray")


@_attrs_define
class Xray:
    """
    Attributes:
        xray_setting (str | Unset):
        inbound_tags (str | Unset):
        client_reverse_tags (str | Unset):
        outbound_test_url (str | Unset):
    """

    xray_setting: str | Unset = UNSET
    inbound_tags: str | Unset = UNSET
    client_reverse_tags: str | Unset = UNSET
    outbound_test_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        xray_setting = self.xray_setting

        inbound_tags = self.inbound_tags

        client_reverse_tags = self.client_reverse_tags

        outbound_test_url = self.outbound_test_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if xray_setting is not UNSET:
            field_dict["xraySetting"] = xray_setting
        if inbound_tags is not UNSET:
            field_dict["inboundTags"] = inbound_tags
        if client_reverse_tags is not UNSET:
            field_dict["clientReverseTags"] = client_reverse_tags
        if outbound_test_url is not UNSET:
            field_dict["outboundTestUrl"] = outbound_test_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        xray_setting = d.pop("xraySetting", UNSET)

        inbound_tags = d.pop("inboundTags", UNSET)

        client_reverse_tags = d.pop("clientReverseTags", UNSET)

        outbound_test_url = d.pop("outboundTestUrl", UNSET)

        xray = cls(
            xray_setting=xray_setting,
            inbound_tags=inbound_tags,
            client_reverse_tags=client_reverse_tags,
            outbound_test_url=outbound_test_url,
        )

        xray.additional_properties = d
        return xray

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
