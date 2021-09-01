import traceback
from abc import abstractmethod
from src.encryption import Scrambler, FileHasExtension


class GateKeeper:
    __key: Scrambler
    __key_file_name: str = 'key.py'

    def __init__(self):
        self.__key = self._get_key()

    def solve(self) -> None:
        if self._solution():
            self.print('Passou em todos os testes')
            self._unlock()
        else:
            self.print('Não passou em todos os testes')

    @abstractmethod
    def _solution(self) -> bool:
        pass

    @abstractmethod
    def __import_from_key(self) -> None:
        pass

    def _get_key(self) -> Scrambler:
        this_file: str = traceback.extract_stack()[1][0]
        path = '/'.join(this_file.split('/')[:-1])
        key_file = f'{path}/{self.__key_file_name}'
        return Scrambler(key_file)

    def __retrieve_key(self) -> None:
        if self.__key.is_python:
            self.__key.decrypt()
            self.__import_from_key()
            self.__key.encrypt()
        else:
            self.__import_from_key()

    def _unlock(self) -> None:
        try:
            self.__key.decrypt()
        except FileHasExtension:
            pass

    @staticmethod
    def print(text: str) -> None:
        print(text)
