from src.scaffold.path_repository.dir_repository import DirRepo
from src.scaffold.path_repository.file_repository import FileRepo
from src.scaffold.path_repository.models import BasicPath


class PathRepo:
    dir: DirRepo
    file: FileRepo

    def __init__(self, group: str, problem: str) -> None:
        self.dir = DirRepo(group_name=group, problem_name=problem)
        self.file = FileRepo(problem_name=problem, dir_repo=self.dir)

    @property
    def unique_paths(self) -> [BasicPath]:
        return [self.dir.key, self.dir.problem] + self.file.all
