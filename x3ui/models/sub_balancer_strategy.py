from enum import Enum


class SubBalancerStrategy(str, Enum):
    LEASTLOAD = "leastLoad"
    LEASTPING = "leastPing"
    RANDOM = "random"
    ROUNDROBIN = "roundRobin"

    def __str__(self) -> str:
        return str(self.value)
