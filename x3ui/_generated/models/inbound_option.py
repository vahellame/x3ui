from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_settings import ServerSettings


T = TypeVar("T", bound="InboundOption")


@_attrs_define
class InboundOption:
    """
    Attributes:
        enable (bool):  Example: True.
        id (int):  Example: 1.
        port (int):  Example: 443.
        protocol (str):  Example: vless.
        remark (str):  Example: VLESS-443.
        ss_method (str):
        tag (str):  Example: in-443-tcp.
        tls_flow_capable (bool):  Example: True.
        awg_server (None | ServerSettings | Unset): AwgServer carries the full AmneziaWG server block (keys, subnet,
            obfuscation params) so the clients page can render a downloadable
            per-client .conf without a second round trip.
        listen (str | Unset):
        mtproto_domain (str | Unset):
        node_address (str | Unset): Share-host resolution inputs, mirroring the subscription's
            resolveInboundAddress so the clients page renders a node-managed WireGuard
            Endpoint that points at the node, not the master panel. NodeAddress is the
            hosting node's externally reachable address (empty for this panel's own
            inbounds); Listen and ShareAddrStrategy/ShareAddr feed the same
            node→listen→custom fallback the share/QR links already use.
        node_id (int | None | Unset): Hosting node; nil for this panel's own inbounds. Lets the clients
            page map a node filter onto inbound IDs (#4997).
        share_addr (str | Unset):
        share_addr_strategy (str | Unset):
        wg_dns (str | Unset):
        wg_mtu (int | Unset):
        wg_public_key (str | Unset):
    """

    enable: bool
    id: int
    port: int
    protocol: str
    remark: str
    ss_method: str
    tag: str
    tls_flow_capable: bool
    awg_server: None | ServerSettings | Unset = UNSET
    listen: str | Unset = UNSET
    mtproto_domain: str | Unset = UNSET
    node_address: str | Unset = UNSET
    node_id: int | None | Unset = UNSET
    share_addr: str | Unset = UNSET
    share_addr_strategy: str | Unset = UNSET
    wg_dns: str | Unset = UNSET
    wg_mtu: int | Unset = UNSET
    wg_public_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.server_settings import ServerSettings

        enable = self.enable

        id = self.id

        port = self.port

        protocol = self.protocol

        remark = self.remark

        ss_method = self.ss_method

        tag = self.tag

        tls_flow_capable = self.tls_flow_capable

        awg_server: dict[str, Any] | None | Unset
        if isinstance(self.awg_server, Unset):
            awg_server = UNSET
        elif isinstance(self.awg_server, ServerSettings):
            awg_server = self.awg_server.to_dict()
        else:
            awg_server = self.awg_server

        listen = self.listen

        mtproto_domain = self.mtproto_domain

        node_address = self.node_address

        node_id: int | None | Unset
        if isinstance(self.node_id, Unset):
            node_id = UNSET
        else:
            node_id = self.node_id

        share_addr = self.share_addr

        share_addr_strategy = self.share_addr_strategy

        wg_dns = self.wg_dns

        wg_mtu = self.wg_mtu

        wg_public_key = self.wg_public_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "id": id,
                "port": port,
                "protocol": protocol,
                "remark": remark,
                "ssMethod": ss_method,
                "tag": tag,
                "tlsFlowCapable": tls_flow_capable,
            }
        )
        if awg_server is not UNSET:
            field_dict["awgServer"] = awg_server
        if listen is not UNSET:
            field_dict["listen"] = listen
        if mtproto_domain is not UNSET:
            field_dict["mtprotoDomain"] = mtproto_domain
        if node_address is not UNSET:
            field_dict["nodeAddress"] = node_address
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if share_addr is not UNSET:
            field_dict["shareAddr"] = share_addr
        if share_addr_strategy is not UNSET:
            field_dict["shareAddrStrategy"] = share_addr_strategy
        if wg_dns is not UNSET:
            field_dict["wgDns"] = wg_dns
        if wg_mtu is not UNSET:
            field_dict["wgMtu"] = wg_mtu
        if wg_public_key is not UNSET:
            field_dict["wgPublicKey"] = wg_public_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.server_settings import ServerSettings

        d = dict(src_dict)
        enable = d.pop("enable")

        id = d.pop("id")

        port = d.pop("port")

        protocol = d.pop("protocol")

        remark = d.pop("remark")

        ss_method = d.pop("ssMethod")

        tag = d.pop("tag")

        tls_flow_capable = d.pop("tlsFlowCapable")

        def _parse_awg_server(data: object) -> None | ServerSettings | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                awg_server_type_1 = ServerSettings.from_dict(data)

                return awg_server_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ServerSettings | Unset, data)

        awg_server = _parse_awg_server(d.pop("awgServer", UNSET))

        listen = d.pop("listen", UNSET)

        mtproto_domain = d.pop("mtprotoDomain", UNSET)

        node_address = d.pop("nodeAddress", UNSET)

        def _parse_node_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        node_id = _parse_node_id(d.pop("nodeId", UNSET))

        share_addr = d.pop("shareAddr", UNSET)

        share_addr_strategy = d.pop("shareAddrStrategy", UNSET)

        wg_dns = d.pop("wgDns", UNSET)

        wg_mtu = d.pop("wgMtu", UNSET)

        wg_public_key = d.pop("wgPublicKey", UNSET)

        inbound_option = cls(
            enable=enable,
            id=id,
            port=port,
            protocol=protocol,
            remark=remark,
            ss_method=ss_method,
            tag=tag,
            tls_flow_capable=tls_flow_capable,
            awg_server=awg_server,
            listen=listen,
            mtproto_domain=mtproto_domain,
            node_address=node_address,
            node_id=node_id,
            share_addr=share_addr,
            share_addr_strategy=share_addr_strategy,
            wg_dns=wg_dns,
            wg_mtu=wg_mtu,
            wg_public_key=wg_public_key,
        )

        inbound_option.additional_properties = d
        return inbound_option

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
