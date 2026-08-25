from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerSettings")


@_attrs_define
class ServerSettings:
    """ServerSettings is the "server" block of an AmneziaWG inbound's Settings
    JSON: the interface-level configuration shared by every client/peer. The
    listen port is deliberately not duplicated here — it lives on the inbound
    row itself (Inbound.Port), like every other protocol.

        Attributes:
            disable_cookies (bool):
            h1 (str):
            h2 (str):
            h3 (str):
            h4 (str):
            jc (int): Obfuscation31's fields, repeated flat (not embedded) rather than
                nested under their own key: encoding/json would happily inline an
                embedded Obfuscation31 the same way, but the frontend's Go->Zod/TS
                generator (tools/openapigen) does not — it emits a genuinely nested
                `obfuscation31` object, which would silently diverge from the real
                wire JSON. See Obfuscation() below for the manager-facing conversion.
            jmax (int):
            jmin (int):
            primary_dns (str): PrimaryDNS/SecondaryDNS seed client configs' DNS line. Blank is
                meaningful, so no omitempty: a dropped key resurrects frontend defaults.
            private_key (str):
            public_key (str):
            random_trailers (bool): RandomTrailers/DisableCookies mirror Instance's identically named
                AmneziaWG 3.1 fields -- see that type's own doc comment for the real
                protocol/interop details. Both real bool fields (not omitempty):
                buildUAPIConfig always emits both lines explicitly so the
                reconfigure-in-place diff correctly notices a true->false edit, not
                just false->true.
            s1 (int):
            s2 (int):
            s3 (int):
            s4 (int):
            secondary_dns (str):
            subnet_cidr (int):
            subnet_ip (str):
            content_padding_addition (str | Unset):
            external_interface (str | Unset): ExternalInterface, IPv6Enabled, and IPv6ExternalInterface are live
                again as of Phase 3.5 -- see the matching fields on Instance for what
                they gate (internal/amneziawgnet's IPv6-address-alias mechanism).
                IPv6Subnet was never actually vestigial either: InstanceFromInbound
                already consumes it (via serverAddressV6) to build the server's own
                tunnel address, same as always. Only RouteThroughXray, below, remains
                genuinely vestigial as of the hard cutover to the embedded path
                (internal/amneziawgnet) -- read from existing stored settings for
                backward compatibility, but not acted on by anything.
            header_protection_key (str | Unset): HeaderProtectionKey and ContentPaddingAddition are AmneziaWG 3.0
                fields, flat and top-level for the same tools/openapigen reason as
                the block above; Obfuscation() below folds them back into
                Obfuscation31's own identically named fields.
                HeaderProtectionKey is a base64 32-byte key; empty (the default)
                disables AWG 3.0 header protection. A non-empty value requires
                every one of S1-S4 above to be >= 12 -- ValidateObfuscation
                enforces this at save time, not just at IpcSet time.
                ContentPaddingAddition is a "low-high" range or bare integer, the
                same grammar and uint32 cap as H1-H4.
            i1 (str | Unset):
            i2 (str | Unset):
            i3 (str | Unset):
            i4 (str | Unset):
            i5 (str | Unset):
            ipv_6_enabled (bool | Unset):
            ipv_6_external_interface (str | Unset):
            ipv_6_subnet (str | Unset):
            keepalive_timeout (str | Unset):
            max_handshake_attempts (str | Unset):
            mtu (int | Unset):
            reject_after_time (str | Unset):
            rekey_after_time (str | Unset): RekeyAfterTime/RekeyTimeout/RejectAfterTime/KeepaliveTimeout/
                MaxHandshakeAttempts mirror Instance's identically named fields --
                see that type's own doc comment for the grammar/width/real-default
                details. Flat and top-level for the same tools/openapigen reason as
                the rest of this struct.
            rekey_timeout (str | Unset):
            route_through_xray (bool | Unset):
    """

    disable_cookies: bool
    h1: str
    h2: str
    h3: str
    h4: str
    jc: int
    jmax: int
    jmin: int
    primary_dns: str
    private_key: str
    public_key: str
    random_trailers: bool
    s1: int
    s2: int
    s3: int
    s4: int
    secondary_dns: str
    subnet_cidr: int
    subnet_ip: str
    content_padding_addition: str | Unset = UNSET
    external_interface: str | Unset = UNSET
    header_protection_key: str | Unset = UNSET
    i1: str | Unset = UNSET
    i2: str | Unset = UNSET
    i3: str | Unset = UNSET
    i4: str | Unset = UNSET
    i5: str | Unset = UNSET
    ipv_6_enabled: bool | Unset = UNSET
    ipv_6_external_interface: str | Unset = UNSET
    ipv_6_subnet: str | Unset = UNSET
    keepalive_timeout: str | Unset = UNSET
    max_handshake_attempts: str | Unset = UNSET
    mtu: int | Unset = UNSET
    reject_after_time: str | Unset = UNSET
    rekey_after_time: str | Unset = UNSET
    rekey_timeout: str | Unset = UNSET
    route_through_xray: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disable_cookies = self.disable_cookies

        h1 = self.h1

        h2 = self.h2

        h3 = self.h3

        h4 = self.h4

        jc = self.jc

        jmax = self.jmax

        jmin = self.jmin

        primary_dns = self.primary_dns

        private_key = self.private_key

        public_key = self.public_key

        random_trailers = self.random_trailers

        s1 = self.s1

        s2 = self.s2

        s3 = self.s3

        s4 = self.s4

        secondary_dns = self.secondary_dns

        subnet_cidr = self.subnet_cidr

        subnet_ip = self.subnet_ip

        content_padding_addition = self.content_padding_addition

        external_interface = self.external_interface

        header_protection_key = self.header_protection_key

        i1 = self.i1

        i2 = self.i2

        i3 = self.i3

        i4 = self.i4

        i5 = self.i5

        ipv_6_enabled = self.ipv_6_enabled

        ipv_6_external_interface = self.ipv_6_external_interface

        ipv_6_subnet = self.ipv_6_subnet

        keepalive_timeout = self.keepalive_timeout

        max_handshake_attempts = self.max_handshake_attempts

        mtu = self.mtu

        reject_after_time = self.reject_after_time

        rekey_after_time = self.rekey_after_time

        rekey_timeout = self.rekey_timeout

        route_through_xray = self.route_through_xray

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "disableCookies": disable_cookies,
                "h1": h1,
                "h2": h2,
                "h3": h3,
                "h4": h4,
                "jc": jc,
                "jmax": jmax,
                "jmin": jmin,
                "primaryDns": primary_dns,
                "privateKey": private_key,
                "publicKey": public_key,
                "randomTrailers": random_trailers,
                "s1": s1,
                "s2": s2,
                "s3": s3,
                "s4": s4,
                "secondaryDns": secondary_dns,
                "subnetCidr": subnet_cidr,
                "subnetIp": subnet_ip,
            }
        )
        if content_padding_addition is not UNSET:
            field_dict["contentPaddingAddition"] = content_padding_addition
        if external_interface is not UNSET:
            field_dict["externalInterface"] = external_interface
        if header_protection_key is not UNSET:
            field_dict["headerProtectionKey"] = header_protection_key
        if i1 is not UNSET:
            field_dict["i1"] = i1
        if i2 is not UNSET:
            field_dict["i2"] = i2
        if i3 is not UNSET:
            field_dict["i3"] = i3
        if i4 is not UNSET:
            field_dict["i4"] = i4
        if i5 is not UNSET:
            field_dict["i5"] = i5
        if ipv_6_enabled is not UNSET:
            field_dict["ipv6Enabled"] = ipv_6_enabled
        if ipv_6_external_interface is not UNSET:
            field_dict["ipv6ExternalInterface"] = ipv_6_external_interface
        if ipv_6_subnet is not UNSET:
            field_dict["ipv6Subnet"] = ipv_6_subnet
        if keepalive_timeout is not UNSET:
            field_dict["keepaliveTimeout"] = keepalive_timeout
        if max_handshake_attempts is not UNSET:
            field_dict["maxHandshakeAttempts"] = max_handshake_attempts
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if reject_after_time is not UNSET:
            field_dict["rejectAfterTime"] = reject_after_time
        if rekey_after_time is not UNSET:
            field_dict["rekeyAfterTime"] = rekey_after_time
        if rekey_timeout is not UNSET:
            field_dict["rekeyTimeout"] = rekey_timeout
        if route_through_xray is not UNSET:
            field_dict["routeThroughXray"] = route_through_xray

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        disable_cookies = d.pop("disableCookies")

        h1 = d.pop("h1")

        h2 = d.pop("h2")

        h3 = d.pop("h3")

        h4 = d.pop("h4")

        jc = d.pop("jc")

        jmax = d.pop("jmax")

        jmin = d.pop("jmin")

        primary_dns = d.pop("primaryDns")

        private_key = d.pop("privateKey")

        public_key = d.pop("publicKey")

        random_trailers = d.pop("randomTrailers")

        s1 = d.pop("s1")

        s2 = d.pop("s2")

        s3 = d.pop("s3")

        s4 = d.pop("s4")

        secondary_dns = d.pop("secondaryDns")

        subnet_cidr = d.pop("subnetCidr")

        subnet_ip = d.pop("subnetIp")

        content_padding_addition = d.pop("contentPaddingAddition", UNSET)

        external_interface = d.pop("externalInterface", UNSET)

        header_protection_key = d.pop("headerProtectionKey", UNSET)

        i1 = d.pop("i1", UNSET)

        i2 = d.pop("i2", UNSET)

        i3 = d.pop("i3", UNSET)

        i4 = d.pop("i4", UNSET)

        i5 = d.pop("i5", UNSET)

        ipv_6_enabled = d.pop("ipv6Enabled", UNSET)

        ipv_6_external_interface = d.pop("ipv6ExternalInterface", UNSET)

        ipv_6_subnet = d.pop("ipv6Subnet", UNSET)

        keepalive_timeout = d.pop("keepaliveTimeout", UNSET)

        max_handshake_attempts = d.pop("maxHandshakeAttempts", UNSET)

        mtu = d.pop("mtu", UNSET)

        reject_after_time = d.pop("rejectAfterTime", UNSET)

        rekey_after_time = d.pop("rekeyAfterTime", UNSET)

        rekey_timeout = d.pop("rekeyTimeout", UNSET)

        route_through_xray = d.pop("routeThroughXray", UNSET)

        server_settings = cls(
            disable_cookies=disable_cookies,
            h1=h1,
            h2=h2,
            h3=h3,
            h4=h4,
            jc=jc,
            jmax=jmax,
            jmin=jmin,
            primary_dns=primary_dns,
            private_key=private_key,
            public_key=public_key,
            random_trailers=random_trailers,
            s1=s1,
            s2=s2,
            s3=s3,
            s4=s4,
            secondary_dns=secondary_dns,
            subnet_cidr=subnet_cidr,
            subnet_ip=subnet_ip,
            content_padding_addition=content_padding_addition,
            external_interface=external_interface,
            header_protection_key=header_protection_key,
            i1=i1,
            i2=i2,
            i3=i3,
            i4=i4,
            i5=i5,
            ipv_6_enabled=ipv_6_enabled,
            ipv_6_external_interface=ipv_6_external_interface,
            ipv_6_subnet=ipv_6_subnet,
            keepalive_timeout=keepalive_timeout,
            max_handshake_attempts=max_handshake_attempts,
            mtu=mtu,
            reject_after_time=reject_after_time,
            rekey_after_time=rekey_after_time,
            rekey_timeout=rekey_timeout,
            route_through_xray=route_through_xray,
        )

        server_settings.additional_properties = d
        return server_settings

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
