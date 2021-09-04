from __future__ import annotations
import os

from src.enums import FileSystemEnum
from src.scaffold.path_repository.models.basic_path import BasicPath
from src.scaffold.path_repository.models.file import File


class Dir(BasicPath):
    def _create(self, content: str = None) -> None:
        os.mkdir(self.to_string)
        if content is not None:
            self._spawn_init_file(init_content=content)

    def __init__(self, path: str, init_content: str = None) -> None:
        super().__init__(path=path, content=init_content)

    def _spawn_init_file(self, init_content: str):
        init_file = f'{self.to_string}/{FileSystemEnum.INIT_FILE}'
        File(init_file, init_content)

    @classmethod
    def empty_package(cls, path: str) -> Dir:
        return cls(path=path, init_content='')

    @classmethod
    def