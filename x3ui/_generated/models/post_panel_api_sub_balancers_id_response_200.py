from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sub_balancer import SubBalancer


T = TypeVar("T", bound="PostPanelApiSubBalancersIdResponse200")


@_attrs_define
class PostPanelApiSubBalancersIdResponse200:
    """
    Attributes:
        success (bool | Unset):
        msg (str | Unset):
        obj (SubBalancer | Unset): SubBalancer is one extra JSON-subscription config document whose members are
            the selected inbounds' proxy outbounds. SortOrder shares SubSortIndex semantics.
    """

    success: bool | Unset = UNSET
    msg: str | Unset = UNSET
    obj: SubBalancer | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        msg = self.msg

        obj: dict[str, Any] | Unset = UNSET
        if not isinstance(self.obj, Unset):
            obj = self.obj.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if msg is not UNSET:
            field_dict["msg"] = msg
        if obj is not UNSET:
            field_dict["obj"] = obj

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sub_balancer import SubBalancer

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        msg = d.pop("msg", UNSET)

        _obj = d.pop("obj", UNSET)
        obj: SubBalancer | Unset
        if isinstance(_obj, Unset):
            obj = UNSET
        else:
            obj = SubBalancer.from_dict(_obj)

        post_panel_api_sub_balancers_id_response_200 = cls(
            success=success,
            msg=msg,
            obj=obj,
        )

        post_panel_api_sub_balancers_id_response_200.additional_properties = d
        return post_panel_api_sub_balancers_id_response_200

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
