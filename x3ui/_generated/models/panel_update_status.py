from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="PanelUpdateStatus")


@_attrs_define
class PanelUpdateStatus:
    """PanelUpdateStatus reports the outcome of the most recently launched panel
    self-update. RunID lets the caller confirm this status belongs to the
    update it started rather than a stale result left over from an earlier
    run; State is one of "pending", "success", or "failed". RunID is a decimal
    string, not a JSON number: it's a formatted UnixNano timestamp, and
    JavaScript's number type can't represent that precisely (it exceeds
    Number.MAX_SAFE_INTEGER), which would let two different runs round to the
    same value on the wire and defeat the whole point of this field.

        Attributes:
            exit_code (int):
            finished_at (int):  Example: 1735689612.
            run_id (str):  Example: 1735689600123456789.
            state (str):  Example: success.
    """

    exit_code: int
    finished_at: int
    run_id: str
    state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exit_code = self.exit_code

        finished_at = self.finished_at

        run_id = self.run_id

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exitCode": exit_code,
                "finishedAt": finished_at,
                "runId": run_id,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        exit_code = d.pop("exitCode")

        finished_at = d.pop("finishedAt")

        run_id = d.pop("runId")

        state = d.pop("state")

        panel_update_status = cls(
            exit_code=exit_code,
            finished_at=finished_at,
            run_id=run_id,
            state=state,
        )

        panel_update_status.additional_properties = d
        return panel_update_status

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
