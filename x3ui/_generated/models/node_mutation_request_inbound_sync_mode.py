from enum import Enum


class NodeMutationRequestInboundSyncMode(str, Enum):
    ALL = "all"
    SELECTED = "selected"

    def __str__(self) -> str:
        return str(self.value)
