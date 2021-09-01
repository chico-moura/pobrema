import traceback
from abc import abstractmethod

from src.encryption import Scrambler, FileHasExtension
from src.problem.problem import Problem


class GateKeeper:
    __key: Scrambler
    __key_file_name: str = 'key.py'
    __problems: [Problem] = []

    def __init__(self):
        self.__key = self._get_key()
        self._retrieve_imports()

    @abstractmethod
    def _import_from_key(self) -> None:
        pass

    def add_problems(self, *problems: Problem) -> None:
        [self.__problems.append(problem) for problem in problems]

    def solve(self) -> None:
        if self._solve_problems():
            self._unlock()

    def _get_key(self) -> Scrambler:
        this_file: str = traceback.extract_stack()[1][0]
        path = '/'.join(this_file.split('/')[:-1])
        key_file = f'{path}/{self.__key_file_name}'
        return Scrambler(key_file)

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
