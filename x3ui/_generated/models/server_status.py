from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_status_disk import ServerStatusDisk
    from ..models.server_status_load import ServerStatusLoad
    from ..models.server_status_mem import ServerStatusMem
    from ..models.server_status_net_io import ServerStatusNetIO
    from ..models.server_status_swap import ServerStatusSwap
    from ..models.server_status_xray import ServerStatusXray


T = TypeVar("T", bound="ServerStatus")


@_attrs_define
class ServerStatus:
    """
    Attributes:
        cpu (float | Unset):
        mem (ServerStatusMem | Unset):
        swap (ServerStatusSwap | Unset):
        disk (ServerStatusDisk | Unset):
        net_io (ServerStatusNetIO | Unset):
        xray (ServerStatusXray | Unset):
        tcp_count (int | Unset):
        load (ServerStatusLoad | Unset):
    """

    cpu: float | Unset = UNSET
    mem: ServerStatusMem | Unset = UNSET
    swap: ServerStatusSwap | Unset = UNSET
    disk: ServerStatusDisk | Unset = UNSET
    net_io: ServerStatusNetIO | Unset = UNSET
    xray: ServerStatusXray | Unset = UNSET
    tcp_count: int | Unset = UNSET
    load: ServerStatusLoad | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu = self.cpu

        mem: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mem, Unset):
            mem = self.mem.to_dict()

        swap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.swap, Unset):
            swap = self.swap.to_dict()

        disk: dict[str, Any] | Unset = UNSET
        if not isinstance(self.disk, Unset):
            disk = self.disk.to_dict()

        net_io: dict[str, Any] | Unset = UNSET
        if not isinstance(self.net_io, Unset):
            net_io = self.net_io.to_dict()

        xray: dict[str, Any] | Unset = UNSET
        if not isinstance(self.xray, Unset):
            xray = self.xray.to_dict()

        tcp_count = self.tcp_count

        load: dict[str, Any] | Unset = UNSET
        if not isinstance(self.load, Unset):
            load = self.load.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if mem is not UNSET:
            field_dict["mem"] = mem
        if swap is not UNSET:
            field_dict["swap"] = swap
        if disk is not UNSET:
            field_dict["disk"] = disk
        if net_io is not UNSET:
            field_dict["netIO"] = net_io
        if xray is not UNSET:
            field_dict["xray"] = xray
        if tcp_count is not UNSET:
            field_dict["tcpCount"] = tcp_count
        if load is not UNSET:
            field_dict["load"] = load

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.server_status_disk import ServerStatusDisk
        from ..models.server_status_load import ServerStatusLoad
        from ..models.server_status_mem import ServerStatusMem
        from ..models.server_status_net_io import ServerStatusNetIO
        from ..models.server_status_swap import ServerStatusSwap
        from ..models.server_status_xray import ServerStatusXray

        d = dict(src_dict)
        cpu = d.pop("cpu", UNSET)

        _mem = d.pop("mem", UNSET)
        mem: ServerStatusMem | Unset
        if isinstance(_mem, Unset):
            mem = UNSET
        else:
            mem = ServerStatusMem.from_dict(_mem)

        _swap = d.pop("swap", UNSET)
        swap: ServerStatusSwap | Unset
        if isinstance(_swap, Unset):
            swap = UNSET
        else:
            swap = ServerStatusSwap.from_dict(_swap)

        _disk = d.pop("disk", UNSET)
        disk: ServerStatusDisk | Unset
        if isinstance(_disk, Unset):
            disk = UNSET
        else:
            disk = ServerStatusDisk.from_dict(_disk)

        _net_io = d.pop("netIO", UNSET)
        net_io: ServerStatusNetIO | Unset
        if isinstance(_net_io, Unset):
            net_io = UNSET
        else:
            net_io = ServerStatusNetIO.from_dict(_net_io)

        _xray = d.pop("xray", UNSET)
        xray: ServerStatusXray | Unset
        if isinstance(_xray, Unset):
            xray = UNSET
        else:
            xray = ServerStatusXray.from_dict(_xray)

        tcp_count = d.pop("tcpCount", UNSET)

        _load = d.pop("load", UNSET)
        load: ServerStatusLoad | Unset
        if isinstance(_load, Unset):
            load = UNSET
        else:
            load = ServerStatusLoad.from_dict(_load)

        server_status = cls(
            cpu=cpu,
            mem=mem,
            swap=swap,
            disk=disk,
            net_io=net_io,
            xray=xray,
            tcp_count=tcp_count,
            load=load,
        )

        server_status.additional_properties = d
        return server_status

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
