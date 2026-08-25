from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.peer_activity import PeerActivity


T = TypeVar("T", bound="AmneziaWGLogs")


@_attrs_define
class AmneziaWGLogs:
    """AmneziaWGLogs is what the overview's AmneziaWG log view renders: the live
    per-peer activity of every running embedded interface, plus the panel's
    own recent AmneziaWG lifecycle log lines that explain a peer being absent
    from Peers at all.

        Attributes:
            events (list[str]):  Example: ['2025/01/01 12:00:00 amneziawg: started interface awg1 for inbound 1'].
            peers (list[PeerActivity]):
            running (bool):  Example: True.
    """

    events: list[str]
    peers: list[PeerActivity]
    running: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events = self.events

        peers = []
        for peers_item_data in self.peers:
            peers_item = peers_item_data.to_dict()
            peers.append(peers_item)

        running = self.running

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
                "peers": peers,
                "running": running,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.peer_activity import PeerActivity

        d = dict(src_dict)
        events = cast(list[str], d.pop("events"))

        peers = []
        _peers = d.pop("peers")
        for peers_item_data in _peers:
            peers_item = PeerActivity.from_dict(peers_item_data)

            peers.append(peers_item)

        running = d.pop("running")

        amnezia_wg_logs = cls(
            events=events,
            peers=peers,
            running=running,
        )

        amnezia_wg_logs.additional_properties = d
        return amnezia_wg_logs

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
