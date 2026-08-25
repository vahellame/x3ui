from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clients_list_item_traffic import ClientsListItemTraffic


T = TypeVar("T", bound="ClientsListItem")


@_attrs_define
class ClientsListItem:
    """
    Attributes:
        id (int | Unset):
        email (str | Unset):
        sub_id (str | Unset):
        uuid (str | Unset):
        total_gb (int | Unset):
        expiry_time (int | Unset):
        enable (bool | Unset):
        reverse (Any | Unset):
        inbound_ids (list[int] | Unset):
        traffic (ClientsListItemTraffic | Unset):
    """

    id: int | Unset = UNSET
    email: str | Unset = UNSET
    sub_id: str | Unset = UNSET
    uuid: str | Unset = UNSET
    total_gb: int | Unset = UNSET
    expiry_time: int | Unset = UNSET
    enable: bool | Unset = UNSET
    reverse: Any | Unset = UNSET
    inbound_ids: list[int] | Unset = UNSET
    traffic: ClientsListItemTraffic | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        sub_id = self.sub_id

        uuid = self.uuid

        total_gb = self.total_gb

        expiry_time = self.expiry_time

        enable = self.enable

        reverse = self.reverse

        inbound_ids: list[int] | Unset = UNSET
        if not isinstance(self.inbound_ids, Unset):
            inbound_ids = self.inbound_ids

        traffic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.traffic, Unset):
            traffic = self.traffic.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if email is not UNSET:
            field_dict["email"] = email
        if sub_id is not UNSET:
            field_dict["subId"] = sub_id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if total_gb is not UNSET:
            field_dict["totalGB"] = total_gb
        if expiry_time is not UNSET:
            field_dict["expiryTime"] = expiry_time
        if enable is not UNSET:
            field_dict["enable"] = enable
        if reverse is not UNSET:
            field_dict["reverse"] = reverse
        if inbound_ids is not UNSET:
            field_dict["inboundIds"] = inbound_ids
        if traffic is not UNSET:
            field_dict["traffic"] = traffic

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.clients_list_item_traffic import ClientsListItemTraffic

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        email = d.pop("email", UNSET)

        sub_id = d.pop("subId", UNSET)

        uuid = d.pop("uuid", UNSET)

        total_gb = d.pop("totalGB", UNSET)

        expiry_time = d.pop("expiryTime", UNSET)

        enable = d.pop("enable", UNSET)

        reverse = d.pop("reverse", UNSET)

        inbound_ids = cast(list[int], d.pop("inboundIds", UNSET))

        _traffic = d.pop("traffic", UNSET)
        traffic: ClientsListItemTraffic | Unset
        if isinstance(_traffic, Unset):
            traffic = UNSET
        else:
            traffic = ClientsListItemTraffic.from_dict(_traffic)

        clients_list_item = cls(
            id=id,
            email=email,
            sub_id=sub_id,
            uuid=uuid,
            total_gb=total_gb,
            expiry_time=expiry_time,
            enable=enable,
            reverse=reverse,
            inbound_ids=inbound_ids,
            traffic=traffic,
        )

        clients_list_item.additional_properties = d
        return clients_list_item

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
