from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="PeerActivity")


@_attrs_define
class PeerActivity:
    """PeerActivity is one peer's live embedded-Device-reported state, the
    counterpart of an Xray access-log entry: a tunnel logs no requests, only
    handshakes and bytes.

        Attributes:
            allowed_i_ps (str):  Example: 10.8.1.2/32.
            down (int):  Example: 4194304.
            email (str):  Example: peer@example.com.
            endpoint (str):  Example: 203.0.113.9:51820.
            handshake (int): Handshake is unix milliseconds, 0 when the peer has never connected. Example: 1735732800000.
            inbound_id (int):  Example: 1.
            interface (str):  Example: awg1.
            online (bool):  Example: True.
            tag (str):  Example: inbound-51820.
            up (int):  Example: 1048576.
    """

    allowed_i_ps: str
    down: int
    email: str
    endpoint: str
    handshake: int
    inbound_id: int
    interface: str
    online: bool
    tag: str
    up: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_i_ps = self.allowed_i_ps

        down = self.down

        email = self.email

        endpoint = self.endpoint

        handshake = self.handshake

        inbound_id = self.inbound_id

        interface = self.interface

        online = self.online

        tag = self.tag

        up = self.up

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowedIPs": allowed_i_ps,
                "down": down,
                "email": email,
                "endpoint": endpoint,
                "handshake": handshake,
                "inboundId": inbound_id,
                "interface": interface,
                "online": online,
                "tag": tag,
                "up": up,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        allowed_i_ps = d.pop("allowedIPs")

        down = d.pop("down")

        email = d.pop("email")

        endpoint = d.pop("endpoint")

        handshake = d.pop("handshake")

        inbound_id = d.pop("inboundId")

        interface = d.pop("interface")

        online = d.pop("online")

        tag = d.pop("tag")

        up = d.pop("up")

        peer_activity = cls(
            allowed_i_ps=allowed_i_ps,
            down=down,
            email=email,
            endpoint=endpoint,
            handshake=handshake,
            inbound_id=inbound_id,
            interface=interface,
            online=online,
            tag=tag,
            up=up,
        )

        peer_activity.additional_properties = d
        return peer_activity

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
