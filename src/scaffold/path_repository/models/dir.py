from __future__ import annotations
import os

from src.enums import FileSystemEnum
from src.scaffold.path_repository.models.basic_path import BasicPath
from src.scaffold.path_repository.models.file import File


class Dir(BasicPath):
    def _create(self, content: str = None) -> None:
        os.mkdir(self.path)
        if content is not None:
            self._spawn_init_file(content)

    def __init__(self, path: str, init_content: str = None) -> None:
        super().__init__(path=path, content=init_content)

    def _spawn_init_file(self, init_content: str = ''):
        init_file_path = f'{self.path}/{FileSystemEnum.INIT_FILE}'
        File(init_file_path, init_content)

    def spawn_dir(self, name: str, init_content: str = None) -> Dir:
        path = self._get_spawned_path(name)
        return Dir(path=path, init_content=init_content)

    def spawn_file(self, name: str, content: str) -> File:
        path = self._get_spawned_path(name)
        return File(path=path, content=content)

    def _get_spawned_path(self, name: str) -> str:
        return f'{self.path}/{name}'
