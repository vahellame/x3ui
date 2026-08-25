from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clients_export_item_client import ClientsExportItemClient


T = TypeVar("T", bound="ClientsExportItem")


@_attrs_define
class ClientsExportItem:
    """
    Attributes:
        client (ClientsExportItemClient | Unset):
        inbound_ids (list[int] | Unset):
    """

    client: ClientsExportItemClient | Unset = UNSET
    inbound_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        inbound_ids: list[int] | Unset = UNSET
        if not isinstance(self.inbound_ids, Unset):
            inbound_ids = self.inbound_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client is not UNSET:
            field_dict["client"] = client
        if inbound_ids is not UNSET:
            field_dict["inboundIds"] = inbound_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.clients_export_item_client import ClientsExportItemClient

        d = dict(src_dict)
        _client = d.pop("client", UNSET)
        client: ClientsExportItemClient | Unset
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = ClientsExportItemClient.from_dict(_client)

        inbound_ids = cast(list[int], d.pop("inboundIds", UNSET))

        clients_export_item = cls(
            client=client,
            inbound_ids=inbound_ids,
        )

        clients_export_item.additional_properties = d
        return clients_export_item

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
