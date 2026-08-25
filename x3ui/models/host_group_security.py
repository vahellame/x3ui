from enum import Enum


class HostGroupSecurity(str, Enum):
    NONE = "none"
    REALITY = "reality"
    SAME = "same"
    TLS = "tls"

    def __str__(self) -> str:
        return str(self.value)
