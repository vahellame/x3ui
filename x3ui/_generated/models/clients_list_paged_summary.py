from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientsListPagedSummary")


@_attrs_define
class ClientsListPagedSummary:
    """
    Attributes:
        total (int | Unset):
        active (int | Unset):
        online_count (int | Unset):
        depleted_count (int | Unset):
        expiring_count (int | Unset):
        deactive_count (int | Unset):
        online (list[str] | Unset):
        depleted (Any | Unset):
        expiring (Any | Unset):
        deactive (list[str] | Unset):
    """

    total: int | Unset = UNSET
    active: int | Unset = UNSET
    online_count: int | Unset = UNSET
    depleted_count: int | Unset = UNSET
    expiring_count: int | Unset = UNSET
    deactive_count: int | Unset = UNSET
    online: list[str] | Unset = UNSET
    depleted: Any | Unset = UNSET
    expiring: Any | Unset = UNSET
    deactive: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        active = self.active

        online_count = self.online_count

        depleted_count = self.depleted_count

        expiring_count = self.expiring_count

        deactive_count = self.deactive_count

        online: list[str] | Unset = UNSET
        if not isinstance(self.online, Unset):
            online = self.online

        depleted = self.depleted

        expiring = self.expiring

        deactive: list[str] | Unset = UNSET
        if not isinstance(self.deactive, Unset):
            deactive = self.deactive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if active is not UNSET:
            field_dict["active"] = active
        if online_count is not UNSET:
            field_dict["onlineCount"] = online_count
        if depleted_count is not UNSET:
            field_dict["depletedCount"] = depleted_count
        if expiring_count is not UNSET:
            field_dict["expiringCount"] = expiring_count
        if deactive_count is not UNSET:
            field_dict["deactiveCount"] = deactive_count
        if online is not UNSET:
            field_dict["online"] = online
        if depleted is not UNSET:
            field_dict["depleted"] = depleted
        if expiring is not UNSET:
            field_dict["expiring"] = expiring
        if deactive is not UNSET:
            field_dict["deactive"] = deactive

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        active = d.pop("active", UNSET)

        online_count = d.pop("onlineCount", UNSET)

        depleted_count = d.pop("depletedCount", UNSET)

        expiring_count = d.pop("expiringCount", UNSET)

        deactive_count = d.pop("deactiveCount", UNSET)

        online = cast(list[str], d.pop("online", UNSET))

        depleted = d.pop("depleted", UNSET)

        expiring = d.pop("expiring", UNSET)

        deactive = cast(list[str], d.pop("deactive", UNSET))

        clients_list_paged_summary = cls(
            total=total,
            active=active,
            online_count=online_count,
            depleted_count=depleted_count,
            expiring_count=expiring_count,
            deactive_count=deactive_count,
            online=online,
            depleted=depleted,
            expiring=expiring,
            deactive=deactive,
        )

        clients_list_paged_summary.additional_properties = d
        return clients_list_paged_summary

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
