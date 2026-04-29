from abc import ABC, abstractmethod
from typing import Any


class BaseFetcher(ABC):
    @abstractmethod
    def fetch(self) -> dict[str, Any]:
        ...
