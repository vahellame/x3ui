from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clients_add_request_client import ClientsAddRequestClient


T = TypeVar("T", bound="ClientsAddRequest")


@_attrs_define
class ClientsAddRequest:
    """
    Attributes:
        client (ClientsAddRequestClient | Unset):
        inbound_ids (list[int] | Unset):
    """

    client: ClientsAddRequestClient | Unset = UNSET
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
        from ..models.clients_add_request_client import ClientsAddRequestClient

        d = dict(src_dict)
        _client = d.pop("client", UNSET)
        client: ClientsAddRequestClient | Unset
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = ClientsAddRequestClient.from_dict(_client)

        inbound_ids = cast(list[int], d.pop("inboundIds", UNSET))

        clients_add_request = cls(
            client=client,
            inbound_ids=inbound_ids,
        )

        clients_add_request.additional_properties = d
        return clients_add_request

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
