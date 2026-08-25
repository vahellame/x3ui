from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inbounds_list_slim_item_settings import InboundsListSlimItemSettings


T = TypeVar("T", bound="InboundsListSlimItem")


@_attrs_define
class InboundsListSlimItem:
    """
    Attributes:
        id (int | Unset):
        remark (str | Unset):
        settings (InboundsListSlimItemSettings | Unset):
        client_stats (Any | Unset):
    """

    id: int | Unset = UNSET
    remark: str | Unset = UNSET
    settings: InboundsListSlimItemSettings | Unset = UNSET
    client_stats: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        remark = self.remark

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        client_stats = self.client_stats

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if remark is not UNSET:
            field_dict["remark"] = remark
        if settings is not UNSET:
            field_dict["settings"] = settings
        if client_stats is not UNSET:
            field_dict["clientStats"] = client_stats

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.inbounds_list_slim_item_settings import (
            InboundsListSlimItemSettings,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        remark = d.pop("remark", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: InboundsListSlimItemSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = InboundsListSlimItemSettings.from_dict(_settings)

        client_stats = d.pop("clientStats", UNSET)

        inbounds_list_slim_item = cls(
            id=id,
            remark=remark,
            settings=settings,
            client_stats=client_stats,
        )

        inbounds_list_slim_item.additional_properties = d
        return inbounds_list_slim_item

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
