from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clients_list_paged_items_item_traffic import (
        ClientsListPagedItemsItemTraffic,
    )


T = TypeVar("T", bound="ClientsListPagedItemsItem")


@_attrs_define
class ClientsListPagedItemsItem:
    """
    Attributes:
        email (str | Unset):
        sub_id (str | Unset):
        enable (bool | Unset):
        total_gb (int | Unset):
        expiry_time (int | Unset):
        limit_ip (int | Unset):
        limit_hwid (int | Unset):
        reset (int | Unset):
        inbound_ids (list[int] | Unset):
        traffic (ClientsListPagedItemsItemTraffic | Unset):
        created_at (int | Unset):
        updated_at (int | Unset):
    """

    email: str | Unset = UNSET
    sub_id: str | Unset = UNSET
    enable: bool | Unset = UNSET
    total_gb: int | Unset = UNSET
    expiry_time: int | Unset = UNSET
    limit_ip: int | Unset = UNSET
    limit_hwid: int | Unset = UNSET
    reset: int | Unset = UNSET
    inbound_ids: list[int] | Unset = UNSET
    traffic: ClientsListPagedItemsItemTraffic | Unset = UNSET
    created_at: int | Unset = UNSET
    updated_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        sub_id = self.sub_id

        enable = self.enable

        total_gb = self.total_gb

        expiry_time = self.expiry_time

        limit_ip = self.limit_ip

        limit_hwid = self.limit_hwid

        reset = self.reset

        inbound_ids: list[int] | Unset = UNSET
        if not isinstance(self.inbound_ids, Unset):
            inbound_ids = self.inbound_ids

        traffic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.traffic, Unset):
            traffic = self.traffic.to_dict()

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if sub_id is not UNSET:
            field_dict["subId"] = sub_id
        if enable is not UNSET:
            field_dict["enable"] = enable
        if total_gb is not UNSET:
            field_dict["totalGB"] = total_gb
        if expiry_time is not UNSET:
            field_dict["expiryTime"] = expiry_time
        if limit_ip is not UNSET:
            field_dict["limitIp"] = limit_ip
        if limit_hwid is not UNSET:
            field_dict["limitHwid"] = limit_hwid
        if reset is not UNSET:
            field_dict["reset"] = reset
        if inbound_ids is not UNSET:
            field_dict["inboundIds"] = inbound_ids
        if traffic is not UNSET:
            field_dict["traffic"] = traffic
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.clients_list_paged_items_item_traffic import (
            ClientsListPagedItemsItemTraffic,
        )

        d = dict(src_dict)
        email = d.pop("email", UNSET)

        sub_id = d.pop("subId", UNSET)

        enable = d.pop("enable", UNSET)

        total_gb = d.pop("totalGB", UNSET)

        expiry_time = d.pop("expiryTime", UNSET)

        limit_ip = d.pop("limitIp", UNSET)

        limit_hwid = d.pop("limitHwid", UNSET)

        reset = d.pop("reset", UNSET)

        inbound_ids = cast(list[int], d.pop("inboundIds", UNSET))

        _traffic = d.pop("traffic", UNSET)
        traffic: ClientsListPagedItemsItemTraffic | Unset
        if isinstance(_traffic, Unset):
            traffic = UNSET
        else:
            traffic = ClientsListPagedItemsItemTraffic.from_dict(_traffic)

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        clients_list_paged_items_item = cls(
            email=email,
            sub_id=sub_id,
            enable=enable,
            total_gb=total_gb,
            expiry_time=expiry_time,
            limit_ip=limit_ip,
            limit_hwid=limit_hwid,
            reset=reset,
            inbound_ids=inbound_ids,
            traffic=traffic,
            created_at=created_at,
            updated_at=updated_at,
        )

        clients_list_paged_items_item.additional_properties = d
        return clients_list_paged_items_item

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
