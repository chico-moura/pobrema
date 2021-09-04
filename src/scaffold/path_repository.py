from dataclasses import dataclass
from pathlib import Path

from src.enums.file_system_enum import FileSystemEnum as En
from src.enums.path_constants import PathConstants


@dataclass
class BasicPath:
    __path: str

    @property
    def exists(self) -> bool:
        return Path(self.__path).exists()


class Dir:
    problem_group: BasicPath
    problem: BasicPath
    key: BasicPath

    def __init__(self, group: str, problem: str) -> None:
        self.problem_group = BasicPath(f'{PathConstants.PROBLEM_GROUPS}/{group}')
        self.problem = BasicPath(f'{self.problem_group}/{problem}')
        self.key_dir = BasicPath(f'{self.problem}/{En.KEY}')


class File:
    problem: BasicPath
    key: BasicPath
    lock: BasicPath
    init_problem: BasicPath
    init_key: BasicPath

    def __init__(self, problem: str, dirs: Dir) -> None:
        self.problem = BasicPath(f'{dirs.problem}/{problem}{En.FILE_EXTENSION}')
        self.key = BasicPath(f'{dirs.problem}/{En.KEY}{En.FILE_EXTENSION}')
        self.lock = BasicPath(f'{dirs.problem}/{En.LOCK}{En.FILE_EXTENSION}')
        self.init_problem = BasicPath(f'{dirs.problem}/{En.INIT_FILE}')
        self.init_key = BasicPath(f'{dirs.key}/{En.INIT_FILE}')


class PathRepo:
    dir: Dir
    file: File

    def __init__(self, group: str, problem: str) -> None:
        self.dir = Dir(group, problem)
        self.file = File(problem, self.dir)
