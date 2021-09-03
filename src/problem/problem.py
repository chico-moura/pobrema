from abc import ABC, abstractmethod
from typing import Callable
from unittest.mock import ANY
from src.problem.value_objects.problem_value_objects import Score, CallbackPair


class Problem(ABC):
    __tries: int = 10
    __score: Score
    __name: str
    __input: ANY
    __expected: ANY
    __actual: ANY
    __callback_pair: CallbackPair

    def __init__(self, name: str, user_callback: Callable, solver_callback: Callable) -> None:
        self.__name = name
        self.__score = Score(self.__tries)
        self.__callback_pair = CallbackPair(user=user_callback, solver=solver_callback)

    @abstractmethod
    def create_input(self):
        pass

    def solve(self) -> None:
        for _ in range(self.__tries):
            self._solve_scenario()

    @property
    def complete(self) -> bool:
        return self.__score.complete

    def _solve_scenario(self) -> bool:
        self.__input = self.create_input()
        self.__expected = self._execute_callback(self.__callback_pair.solver, self.__input)
        self.__actual = self._execute_callback(self.__callback_pair.user, self.__input)
        result = self.__expected == self.__actual

        if result:
            self.__score.increment()
        else:
            self.print_error()
        return result

    def print_error(self) -> None:
        self.print(f'{self.__name}\n  entrada: {self.__input}\nresultado: {self.__actual}\n esperado: {self.__expected}\n')

    def print_score(self) -> None:
        self.print(f'{self.__name}: {self.__score}')

    @staticmethod
    def _execute_callback(callback: Callable, args: ANY) -> ANY:
        if type(args) is tuple:
            result = callback(*args)
        else:
            result = callback(args)
        return result

    @staticmethod
    def print(text: str) -> None:
        print(text)
