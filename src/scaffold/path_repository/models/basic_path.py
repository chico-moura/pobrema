from __future__ import annotations
from pathlib import Path
from abc import ABC, abstractmethod

from src.errors import PathAlreadyExistsError


class BasicPath(ABC):
    __path: str

    def __init__(self, path: str, content: str = None) -> None:
        self.__path = path
        self.validate_path()
        self._create(content)

    def validate_path(self) -> None:
        if self.exists:
            raise PathAlreadyExistsError(self.to_string)

    @property
    def exists(self) -> bool:
        return Path(self.__path).exists()

    @property
    def to_string(self) -> str:
        return self.__path

    @abstractmethod
    def _create(self, content: str = None) -> None:
        pass

    def __str__(self) -> str:
        return self.to_string
