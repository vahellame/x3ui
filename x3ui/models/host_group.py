from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.host_group_mihomo_ip_version import HostGroupMihomoIpVersion
from ..models.host_group_security import HostGroupSecurity

T = TypeVar("T", bound="HostGroup")


@_attrs_define
class HostGroup:
    """
    Attributes:
        allow_insecure (bool):
        alpn (list[str]):
        ech_config_list (str):
        exclude_from_sub_types (list[str]):
        final_mask (str):
        fingerprint (str):
        group_id (str):
        host_header (str):
        hosts (list[str]):
        inbound_ids (list[int]):
        is_disabled (bool):
        is_hidden (bool):
        keep_sni_blank (bool):
        mihomo_ip_version (HostGroupMihomoIpVersion):
        mihomo_x25519 (bool):
        mux_params (str):
        node_guids (list[str]):
        override_sni_from_address (bool):
        path (str):
        pinned_peer_cert_sha_256 (list[str]):
        port (int):
        remark (str):
        security (HostGroupSecurity):
        server_description (str):
        shuffle_host (bool):
        sni (str):
        sockopt_params (str):
        sort_order (int):
        tags (list[str]):
        verify_peer_cert_by_name (str):
        vless_route (str):
    """

    allow_insecure: bool
    alpn: list[str]
    ech_config_list: str
    exclude_from_sub_types: list[str]
    final_mask: str
    fingerprint: str
    group_id: str
    host_header: str
    hosts: list[str]
    inbound_ids: list[int]
    is_disabled: bool
    is_hidden: bool
    keep_sni_blank: bool
    mihomo_ip_version: HostGroupMihomoIpVersion
    mihomo_x25519: bool
    mux_params: str
    node_guids: list[str]
    override_sni_from_address: bool
    path: str
    pinned_peer_cert_sha_256: list[str]
    port: int
    remark: str
    security: HostGroupSecurity
    server_description: str
    shuffle_host: bool
    sni: str
    sockopt_params: str
    sort_order: int
    tags: list[str]
    verify_peer_cert_by_name: str
    vless_route: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_insecure = self.allow_insecure

        alpn = self.alpn

        ech_config_list = self.ech_config_list

        exclude_from_sub_types = self.exclude_from_sub_types

        final_mask = self.final_mask

        fingerprint = self.fingerprint

        group_id = self.group_id

        host_header = self.host_header

        hosts = self.hosts

        inbound_ids = self.inbound_ids

        is_disabled = self.is_disabled

        is_hidden = self.is_hidden

        keep_sni_blank = self.keep_sni_blank

        mihomo_ip_version = self.mihomo_ip_version.value

        mihomo_x25519 = self.mihomo_x25519

        mux_params = self.mux_params

        node_guids = self.node_guids

        override_sni_from_address = self.override_sni_from_address

        path = self.path

        pinned_peer_cert_sha_256 = self.pinned_peer_cert_sha_256

        port = self.port

        remark = self.remark

        security = self.security.value

        server_description = self.server_description

        shuffle_host = self.shuffle_host

        sni = self.sni

        sockopt_params = self.sockopt_params

        sort_order = self.sort_order

        tags = self.tags

        verify_peer_cert_by_name = self.verify_peer_cert_by_name

        vless_route = self.vless_route

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowInsecure": allow_insecure,
                "alpn": alpn,
                "echConfigList": ech_config_list,
                "excludeFromSubTypes": exclude_from_sub_types,
                "finalMask": final_mask,
                "fingerprint": fingerprint,
                "groupId": group_id,
                "hostHeader": host_header,
                "hosts": hosts,
                "inboundIds": inbound_ids,
                "isDisabled": is_disabled,
                "isHidden": is_hidden,
                "keepSniBlank": keep_sni_blank,
                "mihomoIpVersion": mihomo_ip_version,
                "mihomoX25519": mihomo_x25519,
                "muxParams": mux_params,
                "nodeGuids": node_guids,
                "overrideSniFromAddress": override_sni_from_address,
                "path": path,
                "pinnedPeerCertSha256": pinned_peer_cert_sha_256,
                "port": port,
                "remark": remark,
                "security": security,
                "serverDescription": server_description,
                "shuffleHost": shuffle_host,
                "sni": sni,
                "sockoptParams": sockopt_params,
                "sortOrder": sort_order,
                "tags": tags,
                "verifyPeerCertByName": verify_peer_cert_by_name,
                "vlessRoute": vless_route,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        allow_insecure = d.pop("allowInsecure")

        alpn = cast(list[str], d.pop("alpn"))

        ech_config_list = d.pop("echConfigList")

        exclude_from_sub_types = cast(list[str], d.pop("excludeFromSubTypes"))

        final_mask = d.pop("finalMask")

        fingerprint = d.pop("fingerprint")

        group_id = d.pop("groupId")

        host_header = d.pop("hostHeader")

        hosts = cast(list[str], d.pop("hosts"))

        inbound_ids = cast(list[int], d.pop("inboundIds"))

        is_disabled = d.pop("isDisabled")

        is_hidden = d.pop("isHidden")

        keep_sni_blank = d.pop("keepSniBlank")

        mihomo_ip_version = HostGroupMihomoIpVersion(d.pop("mihomoIpVersion"))

        mihomo_x25519 = d.pop("mihomoX25519")

        mux_params = d.pop("muxParams")

        node_guids = cast(list[str], d.pop("nodeGuids"))

        override_sni_from_address = d.pop("overrideSniFromAddress")

        path = d.pop("path")

        pinned_peer_cert_sha_256 = cast(list[str], d.pop("pinnedPeerCertSha256"))

        port = d.pop("port")

        remark = d.pop("remark")

        security = HostGroupSecurity(d.pop("security"))

        server_description = d.pop("serverDescription")

        shuffle_host = d.pop("shuffleHost")

        sni = d.pop("sni")

        sockopt_params = d.pop("sockoptParams")

        sort_order = d.pop("sortOrder")

        tags = cast(list[str], d.pop("tags"))

        verify_peer_cert_by_name = d.pop("verifyPeerCertByName")

        vless_route = d.pop("vlessRoute")

        host_group = cls(
            allow_insecure=allow_insecure,
            alpn=alpn,
            ech_config_list=ech_config_list,
            exclude_from_sub_types=exclude_from_sub_types,
            final_mask=final_mask,
            fingerprint=fingerprint,
            group_id=group_id,
            host_header=host_header,
            hosts=hosts,
            inbound_ids=inbound_ids,
            is_disabled=is_disabled,
            is_hidden=is_hidden,
            keep_sni_blank=keep_sni_blank,
            mihomo_ip_version=mihomo_ip_version,
            mihomo_x25519=mihomo_x25519,
            mux_params=mux_params,
            node_guids=node_guids,
            override_sni_from_address=override_sni_from_address,
            path=path,
            pinned_peer_cert_sha_256=pinned_peer_cert_sha_256,
            port=port,
            remark=remark,
            security=security,
            server_description=server_description,
            shuffle_host=shuffle_host,
            sni=sni,
            sockopt_params=sockopt_params,
            sort_order=sort_order,
            tags=tags,
            verify_peer_cert_by_name=verify_peer_cert_by_name,
            vless_route=vless_route,
        )

        host_group.additional_properties = d
        return host_group

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
