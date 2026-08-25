from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.panel_update_status import PanelUpdateStatus


T = TypeVar("T", bound="GetPanelApiServerGetUpdateStatusResponse200")


@_attrs_define
class GetPanelApiServerGetUpdateStatusResponse200:
    """
    Attributes:
        success (bool | Unset):
        msg (str | Unset):
        obj (PanelUpdateStatus | Unset): PanelUpdateStatus reports the outcome of the most recently launched panel
            self-update. RunID lets the caller confirm this status belongs to the
            update it started rather than a stale result left over from an earlier
            run; State is one of "pending", "success", or "failed". RunID is a decimal
            string, not a JSON number: it's a formatted UnixNano timestamp, and
            JavaScript's number type can't represent that precisely (it exceeds
            Number.MAX_SAFE_INTEGER), which would let two different runs round to the
            same value on the wire and defeat the whole point of this field.
    """

    success: bool | Unset = UNSET
    msg: str | Unset = UNSET
    obj: PanelUpdateStatus | Unset = UNSET
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
        from ..models.panel_update_status import PanelUpdateStatus

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        msg = d.pop("msg", UNSET)

        _obj = d.pop("obj", UNSET)
        obj: PanelUpdateStatus | Unset
        if isinstance(_obj, Unset):
            obj = UNSET
        else:
            obj = PanelUpdateStatus.from_dict(_obj)

        get_panel_api_server_get_update_status_response_200 = cls(
            success=success,
            msg=msg,
            obj=obj,
        )

        get_panel_api_server_get_update_status_response_200.additional_properties = d
        return get_panel_api_server_get_update_status_response_200

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
