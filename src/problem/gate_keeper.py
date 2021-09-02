import traceback
from abc import abstractmethod
from pathlib import Path

from src.encryption import Scrambler, FileHasExtension, FileNotFound
from src.problem.problem import Problem


class GateKeeper:
    __key: Scrambler
    __key_file_name: str = 'key'
    __problems: [Problem] = []

    def __init__(self):
        self.__key = self._get_key()
        self._retrieve_imports()

    def add_problems(self, *problems: Problem) -> None:
        [self.__problems.append(problem) for problem in problems]

    def solve(self) -> None:
        if self._solve_problems():
            self._unlock()

    @abstractmethod
    def _import_from_key(self) -> None:
        pass

    def _get_key(self) -> Scrambler:
        this_file: str = traceback.extract_stack()[1][0]
        path = '/'.join(this_file.split('/')[:-1])
        key_file = f'{path}/{self.__key_file_name}'
        return Scrambler(key_file)  

    def _get_key_file_name(self) -> str:
        path = self._get_key_path()
        key_file = f'{path}{self.__key_file_name}'
        if not Path(key_file).is_file():
            key_file += '.py'
        if not Path(key_file).is_file():
            raise FileNotFound
        return key_file

    @staticmethod
    def _get_key_path() -> str:
        this_file: str = traceback.extract_stack()[1][0]
        path = '/'.join(this_file.split('/')[:-1])
        return f'{path}/'

    def _solve_problems(self) -> bool:
        [problem.solve() for problem in self.__problems]
        [problem.print_score() for problem in self.__problems]
        return all([problem.complete for problem in self.__problems])

    def _unlock(self) -> None:
        try:
            self.__key.decrypt()
        except FileHasExtension:
            pass

    def _retrieve_imports(self) -> None:
        if not self.__key.is_python:
            self.__key.decrypt()
            self._import_from_key()
            self.__key.encrypt()
        else:
            self._import_from_key()

    @staticmethod
    def print(text: str) -> None:
        print(text)
