import os
import sys

from src.enums.file_system_enum import FileSystemEnum
from src.scaffold.tag_set import Tags
from src.scaffold.path_repository.path_repository import PathRepo, BasicPath


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
        existing_files = [file for file in self.__path.unique_paths if file.exists]
        if existing_files:
            existing_files_to_string = '\n'.join([path.to_string() for path in existing_files])
            raise FileExistsError(f'Files or directories already exists:\n{existing_files_to_string}')

    def _initialize_dirs(self) -> None:
        self._create_dir(self.__path.dir.problem_group)
        self._create_package(self.__path.file.problem, self.__path.file.init_problem)
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
    def _create_dir(path: BasicPath) -> None:
        if not path.exists:
            os.mkdir(path.to_string)
        else:
            raise FileExistsError(path.to_string)

    def _create_package(self, path: BasicPath, init_template: BasicPath = None) -> None:
        try:
            self._create_dir(path)
            init_path = path.with_complement(FileSystemEnum.INIT_FILE)
            self._create_file(init_path, init_template)

        except FileExistsError as e:
            print(e)

    def _create_file(self, path: BasicPath, template: BasicPath = None) -> None:
        if path.exists:
            raise FileExistsError(f'{path} already exists')

        content = ''
        if template:
            content = self._get_content(template)
        with open(path.to_string, 'w') as file:
            file.write(content)

    def _get_content(self, path: BasicPath) -> str:
        with open(path.to_string, 'r') as file:
            content = file.read()
        return self.__tags.replace(content)


if __name__ == '__main__':
    try:
        scaffold = Scaffold(sys.argv[1], sys.argv[2])
        scaffold.create()

    except IndexError:
        print('Invalid arguments, try:\n  python -m scaffold <group_name> <problem_name>')
