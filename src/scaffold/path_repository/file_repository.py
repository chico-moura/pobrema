from src.scaffold.path_repository.models import File
from src.scaffold.path_repository.dir_repository import DirRepo
from src.enums import FileSystemEnum as En


class FileRepo:
    problem: File
    key: File
    lock: File
    init_problem: File
    init_key: File

    def __init__(self, problem_name: str, dir_repo: DirRepo) -> None:
        self.problem = File(f'{dir_repo.problem}/{problem_name}{En.FILE_EXTENSION}')
        self.key = File(f'{dir_repo.problem}/{En.KEY}{En.FILE_EXTENSION}')
        self.lock = File(f'{dir_repo.problem}/{En.LOCK}{En.FILE_EXTENSION}')
        self.init_problem = File(f'{dir_repo.problem}/{En.INIT_FILE}')
        self.init_key = File(f'{dir_repo.key}/{En.INIT_FILE}')

    @property
    def all(self) -> [File]:
        return [
            self.problem,
            self.key,
            self.lock,
            self.init_problem,
            self.init_key,
        ]
