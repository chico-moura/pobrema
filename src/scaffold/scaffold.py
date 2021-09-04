import os
import sys
from pathlib import Path

from src.enums.file_system_enum import FileSystemEnum
from src.scaffold.tag_set import Tags
from src.scaffold.path_repository import PathRepo


class Scaffold:
    __group_name: str
    __problem_name: str
    __path: PathRepo
    __tags: Tags

    def __init__(self, group: str, problem: str) -> None:
        self.__group_name = group
        self.__problem_name = problem
        self.__path = PathRepo(group, problem)
        self.__tags = Tags(problem)

    def create(self) -> None:
        try:
            self._validate_arguments()
            self._initialize_dirs()
            self._initialize_files()

        except FileExistsError or AttributeError as e:
            print(e)

    def _validate_arguments(self) -> None:
        problem = self.__path.problem_file
        if Path(problem).exists():
            raise FileExistsError(f'Files or directories already exists:\n{problem}')

    def _initialize_dirs(self) -> None:
        self._create_dirs(self.__path.problem_group_dir)
        self._create_package(self.__path.problem_file, self.__path.problem_init_file)
        self._create_file(self.__path.key_file)

    def _initialize_files(self) -> None:
        self._create_file(
            path=self.__path.problem_file,
            template=PathConstants.PROBLEM_TEMPLATE
        )
        self._create_file(
            path=self.__path.lock_file,
            template=PathConstants.LOCK_TEMPLATE
        )
        self._create_file(
            path=self.__path.key_file,
            template=PathConstants.KEY_TEMPLATE
        )

    @staticmethod
    def _create_dirs(*paths: str) -> None:
        [os.mkdir(path) for path in paths if not Path(path).exists()]

    def _create_package(self, path: str, init_content: str = '') -> None:
        try:
            self._create_dirs(path)
            init = f'{path}/{FileSystemEnum.INIT_FILE}'
            self._create_file(init, init_content)

        except FileExistsError as e:
            print(e)

    def _create_file(self, path: str, template: str = '') -> None:
        if Path(path).exists():
            raise FileExistsError(f'{path} already exists')

        content = ''
        if template:
            content = self._get_content(template)
        self._write_to_file(path, content)

    def _get_content(self, path: str) -> str:
        with open(path, 'r') as file:
            content = file.read()
        return self.__tags.replace(content)

    @staticmethod
    def _write_to_file(file: str, content: str = '') -> None:
        with open(file, 'w') as f:
            f.write(content)


if __name__ == '__main__':
    try:
        scaffold = Scaffold(sys.argv[1], sys.argv[2])
        scaffold.create()

    except IndexError:
        print('Invalid arguments, try:\n  python -m scaffold <group_name> <problem_name>')
