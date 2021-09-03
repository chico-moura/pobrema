import os
import sys
from dataclasses import dataclass
from pathlib import Path


class Name:
    PROJECT = 'pobrema'
    FILE_EXTENSION = '.py'
    KEY = 'key'
    LOCK = 'lock'
    INIT_FILE = f'__init__{FILE_EXTENSION}'
    TAG_SYMBOL = '%'
    SRC = 'src'
    EXERCICIOS = 'exercicios'
    SOLUTIONS = 'solutions'
    SCAFFOLD = 'scaffold'
    TEMPLATES = 'templates'
    LOCK_TEMPLATE = 'lock_template'
    PROBLEM_TEMPLATE = 'problem_template'
    KEY_TEMPLATE = 'key_template'
    SOLUTION_INIT_TEMPLATE = 'solution_init_template'


@dataclass
class PathConstants:
    ROOT = f'{__file__.split(Name.PROJECT)[0]}{Name.PROJECT}'
    PROBLEM_GROUPS = f'{ROOT}/{Name.EXERCICIOS}'
    SOLUTION_GROUPS = f'{ROOT}/{Name.SRC}/{Name.SOLUTIONS}'
    TEMPLATES = f'{ROOT}/{Name.SRC}/{Name.SCAFFOLD}/{Name.TEMPLATES}'
    LOCK_TEMPLATE = f'{TEMPLATES}/{Name.LOCK_TEMPLATE}'
    PROBLEM_TEMPLATE = f'{TEMPLATES}/{Name.PROBLEM_TEMPLATE}'
    KEY_TEMPLATE = f'{TEMPLATES}/{Name.KEY_TEMPLATE}'
    SOLUTION_INIT_TEMPLATE = f'{TEMPLATES}/{Name.SOLUTION_INIT_TEMPLATE}'
    IMPORT = f'{Name.SRC}.{Name.SOLUTIONS}'


class PathRepo:
    problem_group: str
    problem: str
    solution_group: str
    solution: str
    solution_init: str
    key: str
    lock: str
    import_lock: str

    def __init__(self, group: str, problem: str) -> None:
        self.problem_group = f'{PathConstants.PROBLEM_GROUPS}/{group}'
        self.problem = f'{self.problem_group}/{problem}{Name.FILE_EXTENSION}'
        self.solution_group = f'{PathConstants.SOLUTION_GROUPS}/{group}'
        self.solution = f'{self.solution_group}/{problem}'
        self.solution_init = f'{self.solution}/{Name.INIT_FILE}'
        self.key = f'{self.solution}/{Name.KEY}{Name.FILE_EXTENSION}'
        self.lock = f'{self.solution}/{Name.LOCK}{Name.FILE_EXTENSION}'
        self.import_lock = f'{PathConstants.IMPORT}.{group}.{problem}'


@dataclass
class Tags:
    __tags: {str, str}

    def __init__(self, group: str, problem: str) -> None:
        self.__tags = {
            'problem_name': problem,
            'lock_name': self._to_pascal(problem),
            'lock_path': f'{PathConstants.IMPORT}.{group}.{problem}',
            'lock_path_full': f'{PathConstants.IMPORT}.{group}.{problem}.{Name.LOCK}'
        }

    def replace(self, text: str) -> str:
        for tag in self.__tags.keys():
            actual_tag = f'{Name.TAG_SYMBOL}{tag}{Name.TAG_SYMBOL}'
            replacement = self.__tags[tag]
            text = text.replace(actual_tag, replacement)
        return text

    @staticmethod
    def _to_pascal(name: str) -> str:
        return ''.join(char for char in name.title() if not char.isspace() and not char == '_')


class Scaffold:
    __group_name: str
    __problem_name: str
    __path: PathRepo
    __tags: Tags

    def __init__(self, group: str, problem: str) -> None:
        self.__group_name = group
        self.__problem_name = problem
        self.__path = PathRepo(group, problem)
        self.__tags = Tags(group, problem)

    def create(self) -> None:
        try:
            self._validate_arguments()
            self._initialize_dirs()
            self._initialize_files()

        except FileExistsError or AttributeError as e:
            print(e)

    def _validate_arguments(self) -> None:
        subjects = [self.__path.problem, self.__path.solution]
        files_existing = [file for file in subjects if Path(file).exists()]
        if files_existing:
            files = '\n'.join(files_existing)
            raise FileExistsError(f'Files or directories already exists:\n{files}')

    def _initialize_dirs(self) -> None:
        self._create_dirs(self.__path.problem_group)
        self._create_packages(
            self.__path.solution_group,
            self.__path.solution
        )

    def _initialize_files(self) -> None:
        self._create_file(
            path=self.__path.problem,
            template=PathConstants.PROBLEM_TEMPLATE
        )
        self._create_file(
            path=self.__path.lock,
            template=PathConstants.LOCK_TEMPLATE
        )
        self._create_file(
            path=self.__path.key,
            template=PathConstants.KEY_TEMPLATE
        )
        self._edit_solution_init_file()

    @staticmethod
    def _create_dirs(*paths: str) -> None:
        [os.mkdir(path) for path in paths if not Path(path).exists()]

    def _create_packages(self, *paths: str) -> None:
        self._create_dirs(*paths)
        for path in paths:
            init = f'{path}/{Name.INIT_FILE}'
            if not Path(init).exists():
                self._create_file(init)

    def _create_file(self, path: str, template: str = None) -> None:
        content = ''
        if template:
            content = self._get_content(template)
        with open(path, 'w') as file:
            file.write(content)

    def _edit_solution_init_file(self) -> None:
        content = self._get_content(PathConstants.SOLUTION_INIT_TEMPLATE)
        with open(self.__path.solution_init, 'a') as file:
            file.write(content)

    def _get_content(self, path: str) -> str:
        with open(path, 'r') as file:
            content = file.read()
        return self.__tags.replace(content)


if __name__ == '__main__':
    try:
        scaffold = Scaffold(sys.argv[1], sys.argv[2])
        scaffold.create()

    except IndexError:
        print('Invalid arguments, try:\n  python -m scaffold <group_name> <problem_name>')
