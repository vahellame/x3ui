from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clients_list_paged_items_item import ClientsListPagedItemsItem
    from ..models.clients_list_paged_summary import ClientsListPagedSummary


T = TypeVar("T", bound="ClientsListPaged")


@_attrs_define
class ClientsListPaged:
    """
    Attributes:
        items (list[ClientsListPagedItemsItem] | Unset):
        total (int | Unset):
        filtered (int | Unset):
        page (int | Unset):
        page_size (int | Unset):
        summary (ClientsListPagedSummary | Unset):
    """

    items: list[ClientsListPagedItemsItem] | Unset = UNSET
    total: int | Unset = UNSET
    filtered: int | Unset = UNSET
    page: int | Unset = UNSET
    page_size: int | Unset = UNSET
    summary: ClientsListPagedSummary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        total = self.total

        filtered = self.filtered

        page = self.page

        page_size = self.page_size

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if total is not UNSET:
            field_dict["total"] = total
        if filtered is not UNSET:
            field_dict["filtered"] = filtered
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.clients_list_paged_items_item import ClientsListPagedItemsItem
        from ..models.clients_list_paged_summary import ClientsListPagedSummary

        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: list[ClientsListPagedItemsItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = ClientsListPagedItemsItem.from_dict(items_item_data)

                items.append(items_item)

        total = d.pop("total", UNSET)

        filtered = d.pop("filtered", UNSET)

        page = d.pop("page", UNSET)

        page_size = d.pop("pageSize", UNSET)

        _summary = d.pop("summary", UNSET)
        summary: ClientsListPagedSummary | Unset
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = ClientsListPagedSummary.from_dict(_summary)

        clients_list_paged = cls(
            items=items,
            total=total,
            filtered=filtered,
            page=page,
            page_size=page_size,
            summary=summary,
        )

        clients_list_paged.additional_properties = d
        return clients_list_paged

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
