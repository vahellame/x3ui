from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_detail_external_links_item import ClientDetailExternalLinksItem
    from ..models.client_detail_tunnel_allowed_i_ps import ClientDetailTunnelAllowedIPs
    from ..models.client_record import ClientRecord


T = TypeVar("T", bound="ClientDetail")


@_attrs_define
class ClientDetail:
    """Read shape for GET /panel/api/clients/get/{email}.

    Attributes:
        client (ClientRecord):
        inbound_ids (list[int]):
        external_links (list[ClientDetailExternalLinksItem] | Unset):
        used_traffic (int | Unset):
        tunnel_allowed_i_ps (ClientDetailTunnelAllowedIPs | Unset):
    """

    client: ClientRecord
    inbound_ids: list[int]
    external_links: list[ClientDetailExternalLinksItem] | Unset = UNSET
    used_traffic: int | Unset = UNSET
    tunnel_allowed_i_ps: ClientDetailTunnelAllowedIPs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client = self.client.to_dict()

        inbound_ids = self.inbound_ids

        external_links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.external_links, Unset):
            external_links = []
            for external_links_item_data in self.external_links:
                external_links_item = external_links_item_data.to_dict()
                external_links.append(external_links_item)

        used_traffic = self.used_traffic

        tunnel_allowed_i_ps: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tunnel_allowed_i_ps, Unset):
            tunnel_allowed_i_ps = self.tunnel_allowed_i_ps.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client": client,
                "inboundIds": inbound_ids,
            }
        )
        if external_links is not UNSET:
            field_dict["externalLinks"] = external_links
        if used_traffic is not UNSET:
            field_dict["usedTraffic"] = used_traffic
        if tunnel_allowed_i_ps is not UNSET:
            field_dict["tunnelAllowedIPs"] = tunnel_allowed_i_ps

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_detail_external_links_item import (
            ClientDetailExternalLinksItem,
        )
        from ..models.client_detail_tunnel_allowed_i_ps import (
            ClientDetailTunnelAllowedIPs,
        )
        from ..models.client_record import ClientRecord

        d = dict(src_dict)
        client = ClientRecord.from_dict(d.pop("client"))

        inbound_ids = cast(list[int], d.pop("inboundIds"))

        _external_links = d.pop("externalLinks", UNSET)
        external_links: list[ClientDetailExternalLinksItem] | Unset = UNSET
        if _external_links is not UNSET:
            external_links = []
            for external_links_item_data in _external_links:
                external_links_item = ClientDetailExternalLinksItem.from_dict(
                    external_links_item_data
                )

                external_links.append(external_links_item)

        used_traffic = d.pop("usedTraffic", UNSET)

        _tunnel_allowed_i_ps = d.pop("tunnelAllowedIPs", UNSET)
        tunnel_allowed_i_ps: ClientDetailTunnelAllowedIPs | Unset
        if isinstance(_tunnel_allowed_i_ps, Unset):
            tunnel_allowed_i_ps = UNSET
        else:
            tunnel_allowed_i_ps = ClientDetailTunnelAllowedIPs.from_dict(
                _tunnel_allowed_i_ps
            )

        client_detail = cls(
            client=client,
            inbound_ids=inbound_ids,
            external_links=external_links,
            used_traffic=used_traffic,
            tunnel_allowed_i_ps=tunnel_allowed_i_ps,
        )

        client_detail.additional_properties = d
        return client_detail

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
