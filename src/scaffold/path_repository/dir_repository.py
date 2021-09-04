from src.enums import PathConstants, FileSystemEnum
from src.scaffold.path_repository.models import Dir


class DirRepo:
    problem_group: Dir
    problem: Dir
    key: Dir

    def __init__(self, group_name: str, problem_name: str) -> None:
        self.problem_group = Dir(f'{PathConstants.PROBLEM_GROUPS}/{group_name}')
        self.problem = Dir(f'{self.problem_group}/{problem_name}')
        self.key = Dir(f'{self.problem}/{FileSystemEnum.KEY}')
