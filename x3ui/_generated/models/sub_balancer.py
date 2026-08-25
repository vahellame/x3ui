from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.sub_balancer_strategy import SubBalancerStrategy

T = TypeVar("T", bound="SubBalancer")


@_attrs_define
class SubBalancer:
    """SubBalancer is one extra JSON-subscription config document whose members are
    the selected inbounds' proxy outbounds. SortOrder shares SubSortIndex semantics.

        Attributes:
            created_at (int):  Example: 1710000000000.
            enabled (bool): No gorm default:true — a bool default makes an explicit false at insert
                collapse back to the column default (zero value is skipped). Example: True.
            id (int):  Example: 1.
            inbound_ids (list[int]):  Example: [1, 3].
            remark (str):  Example: auto-fastest.
            sort_order (int):  Example: 1.
            strategy (SubBalancerStrategy):  Example: random.
            updated_at (int):  Example: 1710000000000.
    """

    created_at: int
    enabled: bool
    id: int
    inbound_ids: list[int]
    remark: str
    sort_order: int
    strategy: SubBalancerStrategy
    updated_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        enabled = self.enabled

        id = self.id

        inbound_ids = self.inbound_ids

        remark = self.remark

        sort_order = self.sort_order

        strategy = self.strategy.value

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "enabled": enabled,
                "id": id,
                "inboundIds": inbound_ids,
                "remark": remark,
                "sortOrder": sort_order,
                "strategy": strategy,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = d.pop("createdAt")

        enabled = d.pop("enabled")

        id = d.pop("id")

        inbound_ids = cast(list[int], d.pop("inboundIds"))

        remark = d.pop("remark")

        sort_order = d.pop("sortOrder")

        strategy = SubBalancerStrategy(d.pop("strategy"))

        updated_at = d.pop("updatedAt")

        sub_balancer = cls(
            created_at=created_at,
            enabled=enabled,
            id=id,
            inbound_ids=inbound_ids,
            remark=remark,
            sort_order=sort_order,
            strategy=strategy,
            updated_at=updated_at,
        )

        sub_balancer.additional_properties = d
        return sub_balancer

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
