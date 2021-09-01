from src.solution import Problem, GateKeeper
from random import randrange
from typing import Callable


class ParImpar(GateKeeper):
    __solver_par: Callable
    __solver_impar: Callable
    __par: Problem
    __impar: Problem

    def __init__(self, selecionar_pares: Callable, selecionar_impares: Callable) -> None:
        super().__init__()
        self.__import_from_key()
        self.__par = ParImparCase(
            name='selecionar_pares()',
            user_callback=selecionar_pares,
            solver_callback=self.__solver_par
        )
        self.__impar = ParImparCase(
            name='selecionar_impares()',
            user_callback=selecionar_impares,
            solver_callback=self.__solver_impar
        )

    def _solution(self) -> bool:
        par = self.__par.solve()
        impar = self.__impar.solve()
        return par and impar

    def __import_from_key(self) -> None:
        try:
            from .key import par, impar
            self.__solver_par = par
            self.__solver_impar = impar
        except FileNotFoundError:
            pass


class ParImparCase(Problem):
    __min_int = -99
    __max_int = 99
    __min_size = 10
    __max_size = 20

    def create_input(self) -> [int]:
        size = randrange(self.__min_size, self.__max_size)
        return [randrange(self.__min_int, self.__max_int) for _ in range(size)]




