from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inbounds_add_request_settings import InboundsAddRequestSettings
    from ..models.inbounds_add_request_sniffing import InboundsAddRequestSniffing
    from ..models.inbounds_add_request_stream_settings import (
        InboundsAddRequestStreamSettings,
    )


T = TypeVar("T", bound="InboundsAddRequest")


@_attrs_define
class InboundsAddRequest:
    """
    Attributes:
        enable (bool | Unset):
        remark (str | Unset):
        listen (str | Unset):
        port (int | Unset):
        protocol (str | Unset):
        expiry_time (int | Unset):
        total (int | Unset):
        settings (InboundsAddRequestSettings | Unset):
        stream_settings (InboundsAddRequestStreamSettings | Unset):
        sniffing (InboundsAddRequestSniffing | Unset):
    """

    enable: bool | Unset = UNSET
    remark: str | Unset = UNSET
    listen: str | Unset = UNSET
    port: int | Unset = UNSET
    protocol: str | Unset = UNSET
    expiry_time: int | Unset = UNSET
    total: int | Unset = UNSET
    settings: InboundsAddRequestSettings | Unset = UNSET
    stream_settings: InboundsAddRequestStreamSettings | Unset = UNSET
    sniffing: InboundsAddRequestSniffing | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        remark = self.remark

        listen = self.listen

        port = self.port

        protocol = self.protocol

        expiry_time = self.expiry_time

        total = self.total

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        stream_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stream_settings, Unset):
            stream_settings = self.stream_settings.to_dict()

        sniffing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sniffing, Unset):
            sniffing = self.sniffing.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if remark is not UNSET:
            field_dict["remark"] = remark
        if listen is not UNSET:
            field_dict["listen"] = listen
        if port is not UNSET:
            field_dict["port"] = port
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if expiry_time is not UNSET:
            field_dict["expiryTime"] = expiry_time
        if total is not UNSET:
            field_dict["total"] = total
        if settings is not UNSET:
            field_dict["settings"] = settings
        if stream_settings is not UNSET:
            field_dict["streamSettings"] = stream_settings
        if sniffing is not UNSET:
            field_dict["sniffing"] = sniffing

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.inbounds_add_request_settings import InboundsAddRequestSettings
        from ..models.inbounds_add_request_sniffing import InboundsAddRequestSniffing
        from ..models.inbounds_add_request_stream_settings import (
            InboundsAddRequestStreamSettings,
        )

        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        remark = d.pop("remark", UNSET)

        listen = d.pop("listen", UNSET)

        port = d.pop("port", UNSET)

        protocol = d.pop("protocol", UNSET)

        expiry_time = d.pop("expiryTime", UNSET)

        total = d.pop("total", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: InboundsAddRequestSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = InboundsAddRequestSettings.from_dict(_settings)

        _stream_settings = d.pop("streamSettings", UNSET)
        stream_settings: InboundsAddRequestStreamSettings | Unset
        if isinstance(_stream_settings, Unset):
            stream_settings = UNSET
        else:
            stream_settings = InboundsAddRequestStreamSettings.from_dict(
                _stream_settings
            )

        _sniffing = d.pop("sniffing", UNSET)
        sniffing: InboundsAddRequestSniffing | Unset
        if isinstance(_sniffing, Unset):
            sniffing = UNSET
        else:
            sniffing = InboundsAddRequestSniffing.from_dict(_sniffing)

        inbounds_add_request = cls(
            enable=enable,
            remark=remark,
            listen=listen,
            port=port,
            protocol=protocol,
            expiry_time=expiry_time,
            total=total,
            settings=settings,
            stream_settings=stream_settings,
            sniffing=sniffing,
        )

        inbounds_add_request.additional_properties = d
        return inbounds_add_request

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
