from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.post_panel_api_clients_email_external_links_body_external_links_item import (
        PostPanelApiClientsEmailExternalLinksBodyExternalLinksItem,
    )


T = TypeVar("T", bound="PostPanelApiClientsEmailExternalLinksBody")


@_attrs_define
class PostPanelApiClientsEmailExternalLinksBody:
    """
    Attributes:
        external_links (list[PostPanelApiClientsEmailExternalLinksBodyExternalLinksItem]): Full replacement list; the
            server replaces all rows. Each row supports { kind, value, remark, enable, expiryTime, namePrefix }. kind=link:
            value must be a supported share link such as vless://, vmess://, trojan://, ss://, hysteria2://, or
            wireguard://, and remark overrides the exported node name. kind=subscription: value must be an http(s)
            subscription URL, and namePrefix is prepended to fetched node names. Omit enable to default true; enable=false
            or an expired expiryTime keeps the row saved but excludes it from generated subscriptions. expiryTime is a unix
            millisecond timestamp where 0 means never expire; a negative value is rejected. Rows are matched by kind+value
            across saves, so id is ignored on write. lastFetchAt and lastFetchError are read-only status fields returned by
            GET.
    """

    external_links: list[PostPanelApiClientsEmailExternalLinksBodyExternalLinksItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_links = []
        for external_links_item_data in self.external_links:
            external_links_item = external_links_item_data.to_dict()
            external_links.append(external_links_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "externalLinks": external_links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.post_panel_api_clients_email_external_links_body_external_links_item import (
            PostPanelApiClientsEmailExternalLinksBodyExternalLinksItem,
        )

        d = dict(src_dict)
        external_links = []
        _external_links = d.pop("externalLinks")
        for external_links_item_data in _external_links:
            external_links_item = (
                PostPanelApiClientsEmailExternalLinksBodyExternalLinksItem.from_dict(
                    external_links_item_data
                )
            )

            external_links.append(external_links_item)

        post_panel_api_clients_email_external_links_body = cls(
            external_links=external_links,
        )

        post_panel_api_clients_email_external_links_body.additional_properties = d
        return post_panel_api_clients_email_external_links_body

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
