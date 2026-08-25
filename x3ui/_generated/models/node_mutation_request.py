from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.node_mutation_request_inbound_sync_mode import (
    NodeMutationRequestInboundSyncMode,
)
from ..models.node_mutation_request_scheme import NodeMutationRequestScheme
from ..models.node_mutation_request_tls_verify_mode import (
    NodeMutationRequestTlsVerifyMode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeMutationRequest")


@_attrs_define
class NodeMutationRequest:
    """NodeMutationRequest is the node write/probe contract. ApiToken is accepted
    only as input. On update, nil means keep the stored token; replacement and
    clearing are explicit and mutually exclusive.

        Attributes:
            address (str):
            allow_private_address (bool):
            base_path (str):
            enable (bool):
            id (int):
            inbound_sync_mode (NodeMutationRequestInboundSyncMode):
            inbound_tags (list[str]):
            name (str):
            outbound_tag (str):
            pinned_cert_sha_256 (str):
            port (int):
            remark (str):
            scheme (NodeMutationRequestScheme):
            tls_verify_mode (NodeMutationRequestTlsVerifyMode):
            api_token (None | str | Unset):
            clear_api_token (bool | Unset):
    """

    address: str
    allow_private_address: bool
    base_path: str
    enable: bool
    id: int
    inbound_sync_mode: NodeMutationRequestInboundSyncMode
    inbound_tags: list[str]
    name: str
    outbound_tag: str
    pinned_cert_sha_256: str
    port: int
    remark: str
    scheme: NodeMutationRequestScheme
    tls_verify_mode: NodeMutationRequestTlsVerifyMode
    api_token: None | str | Unset = UNSET
    clear_api_token: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        allow_private_address = self.allow_private_address

        base_path = self.base_path

        enable = self.enable

        id = self.id

        inbound_sync_mode = self.inbound_sync_mode.value

        inbound_tags = self.inbound_tags

        name = self.name

        outbound_tag = self.outbound_tag

        pinned_cert_sha_256 = self.pinned_cert_sha_256

        port = self.port

        remark = self.remark

        scheme = self.scheme.value

        tls_verify_mode = self.tls_verify_mode.value

        api_token: None | str | Unset
        if isinstance(self.api_token, Unset):
            api_token = UNSET
        else:
            api_token = self.api_token

        clear_api_token = self.clear_api_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "allowPrivateAddress": allow_private_address,
                "basePath": base_path,
                "enable": enable,
                "id": id,
                "inboundSyncMode": inbound_sync_mode,
                "inboundTags": inbound_tags,
                "name": name,
                "outboundTag": outbound_tag,
                "pinnedCertSha256": pinned_cert_sha_256,
                "port": port,
                "remark": remark,
                "scheme": scheme,
                "tlsVerifyMode": tls_verify_mode,
            }
        )
        if api_token is not UNSET:
            field_dict["apiToken"] = api_token
        if clear_api_token is not UNSET:
            field_dict["clearApiToken"] = clear_api_token

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        address = d.pop("address")

        allow_private_address = d.pop("allowPrivateAddress")

        base_path = d.pop("basePath")

        enable = d.pop("enable")

        id = d.pop("id")

        inbound_sync_mode = NodeMutationRequestInboundSyncMode(d.pop("inboundSyncMode"))

        inbound_tags = cast(list[str], d.pop("inboundTags"))

        name = d.pop("name")

        outbound_tag = d.pop("outboundTag")

        pinned_cert_sha_256 = d.pop("pinnedCertSha256")

        port = d.pop("port")

        remark = d.pop("remark")

        scheme = NodeMutationRequestScheme(d.pop("scheme"))

        tls_verify_mode = NodeMutationRequestTlsVerifyMode(d.pop("tlsVerifyMode"))

        def _parse_api_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_token = _parse_api_token(d.pop("apiToken", UNSET))

        clear_api_token = d.pop("clearApiToken", UNSET)

        node_mutation_request = cls(
            address=address,
            allow_private_address=allow_private_address,
            base_path=base_path,
            enable=enable,
            id=id,
            inbound_sync_mode=inbound_sync_mode,
            inbound_tags=inbound_tags,
            name=name,
            outbound_tag=outbound_tag,
            pinned_cert_sha_256=pinned_cert_sha_256,
            port=port,
            remark=remark,
            scheme=scheme,
            tls_verify_mode=tls_verify_mode,
            api_token=api_token,
            clear_api_token=clear_api_token,
        )

        node_mutation_request.additional_properties = d
        return node_mutation_request

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
