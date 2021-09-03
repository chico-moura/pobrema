from random import randrange
from typing import Callable

from src.problem import Problem, GateKeeper
from src.encryption import FileNotFound


class ParImpar(GateKeeper):
    __solver_par: Callable
    __solver_impar: Callable

    def __init__(self, selecionar_pares: Callable, selecionar_impares: Callable) -> None:
        super().__init__()
        self.add_problems(
            ParImparCase(
                name='selecionar_impares()',
                user_callback=selecionar_impares,
                solver_callback=self.__solver_impar
            ),
            ParImparCase(
                name='selecionar_pares()',
                user_callback=selecionar_pares,
                solver_callback=self.__solver_par
            )
        )

    def _import_from_key(self) -> None:
        try:
            from .key import par, impar
            self.__solver_par = par
            self.__solver_impar = impar
        except FileNotFound:
            pass


class ParImparCase(Problem):
    __min_int = -99
    __max_int = 99
    __min_size = 10
    __max_size = 20

    def create_input(self) -> [int]:
        size = randrange(self.__min_size, self.__max_size)
        return [randrange(self.__min_int, self.__max_int) for _ in range(size)]
