from random import randrange
from typing import Callable

from src.problem import Problem, GateKeeper
from src.encryption import FileNotFound


class VetorDeIntervaloProblem(Problem):
    __min = -20
    __max = 20

    def create_input(self) -> [int]:
        return self.random_int, self.random_int

    @property
    def random_int(self) -> int:
        return randrange(self.__min, self.__max)


class VetorDeIntervalo(GateKeeper):
    __solver: Callable

    def __init__(self, *callbacks: Callable) -> None:
        super().__init__()
        self.add_problems(
            VetorDeIntervaloProblem(
                name='vetor_a_partir_de_intervalo',
                user_callback=callbacks[0],
                solver_callback=self.__solver
            )
        )

    def _import_from_key(self) -> None:
        try:
            from .key import criar_vetor_a_partir_de_intervalo
            self.__solver = criar_vetor_a_partir_de_intervalo
        except FileNotFound:
            pass
