from abc import ABC, abstractmethod
from typing import Callable
from unittest.mock import ANY
from dataclasses import dataclass


@dataclass
class CallbackPair:
    user: Callable
    solver: Callable


class Problem(ABC):
    __tries: int = 10
    __name: str
    __input: ANY
    __expected: ANY
    __actual: ANY
    __callback_pair: CallbackPair

    def __init__(self, name: str, user_callback: Callable, solver_callback: Callable) -> None:
        self.__name = name
        self.__callback_pair = CallbackPair(user=user_callback, solver=solver_callback)

    @abstractmethod
    def create_input(self) -> ANY:
        pass

    def solve(self) -> bool:
        score = 0
        for _ in range(self.__tries):
            if self.__solve_each():
                score += 1
        self.print(f'{self.__name}    {score}/{self.__tries}')
        return score == self.__tries

    def set_tries(self, tries: int) -> None:
        self.__tries = tries

    def __solve_each(self) -> bool:
        self.__input = self.create_input()
        self.__expected = self.__callback_pair.solver(self.__input)
        self.__actual = self.__callback_pair.user(self.__input)
        result = self.__expected == self.__actual
        if not result:
            self.alert_failure()
        return result

    def alert_failure(self) -> None:
        self.print(f'{self.__name}\n  entrada: {self.__input}\nresultado: {self.__actual}\n esperado: {self.__expected}\n')

    @staticmethod
    def print(text: str) -> None:
        print(text)
