from random import randrange
from typing import Callable

from src.problem import Problem, GateKeeper
from src.encryption import FileNotFound


class VetoresOrdenadosProblem(Problem):
    __min = 0
    __max = 50

    def create_input(self) -> int:
        return randrange(self.__min, self.__max)


class VetoresOrdenados(GateKeeper):
    __criar_vetor_crescente: Callable
    __criar_vetor_decrescente: Callable
    __criar_vetor_de_intervalo: Callable

    def __init__(self, *callbacks: Callable) -> None:
        super().__init__()
        self.add_problems(
            VetoresOrdenadosProblem(
                name='criar_vetor_crescente',
                user_callback=callbacks[0],
                solver_callback=self.__criar_vetor_crescente
            ),
            VetoresOrdenadosProblem(
                name='criar_vetor_decrescente',
                user_callback=callbacks[1],
                solver_callback=self.__criar_vetor_decrescente
            )
        )

    def _import_from_key(self) -> None:
        try:
            from .key import criar_vetor_crescente, criar_vetor_decrescente
            self.__criar_vetor_crescente = criar_vetor_crescente
            self.__criar_vetor_decrescente = criar_vetor_decrescente
        except FileNotFound:
            pass
