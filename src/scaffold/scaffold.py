import sys
from pathlib import Path

from src.scaffold.path_repository.models import Dir
from src.enums import FileSystemEnum, PathConstants
from src.scaffold.template_repository.template_repository import TemplateRepo


class Scaffold:
    __group_name: str
    __problem_name: str
    __group_path: str
    __problem_path: str
    __templates: TemplateRepo

    def __init__(self, group: str, problem: str) -> None:
        self.__group_name = group
        self.__problem_name = problem
        self.__group_path = f'{PathConstants.PROBLEM_GROUPS}/{group}'
        self.__problem_path = f'{self.__group_path}/{problem}'
        self.__templates = TemplateRepo(problem_name=problem)

    def create(self) -> None:
        try:
            self._validate_arguments()
            self._create_structure()

        except FileExistsError or AttributeError as e:
            print(e)

    def _validate_arguments(self) -> None:
        if Path(self.__problem_path).exists():
            raise FileExistsError(f'Files or directories already exists:\n{self.__problem_path}')

    def _create_structure(self) -> None:
        group_dir = Dir(
            path=self.__group_path,
            accept_existing=True
        )
        problem_dir = group_dir.spawn_dir(
            name=self.__problem_name,
            init_content=self.__templates.problem_init
        )
        problem_dir.spawn_file(
            name=self.__problem_name,
            content=self.__templates.problem
        )
        key_dir = problem_dir.spawn_dir(
            name=FileSystemEnum.KEY,
            init_content=self.__templates.key_init
        )
        key_dir.spawn_file(
            name=FileSystemEnum.KEY,
            content=self.__templates.key
        )
        key_dir.spawn_file(
            name=FileSystemEnum.LOCK,
            content=self.__templates.lock
        )


if __name__ == '__main__':
    try:
        scaffold = Scaffold(sys.argv[1], sys.argv[2])
        scaffold.create()

    except IndexError:
        print('Invalid arguments, try:\n  python -m scaffold <group_name> <problem_name>')
