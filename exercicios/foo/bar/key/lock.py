from typing import Callable

from src.problem import Problem, GateKeeper
from src.encryption import FileNotFound


class BarProblem(Problem):
    __min = -99
    __max = 99

    def create_input(self):
        pass


class Bar(GateKeeper):
    __solver: Callable

    def __init__(self, *callbacks: Callable) -> None:
        super().__init__()
        self.add_problems(
            BarProblem(
                name='bar',
                user_callback=callbacks[0],
                solver_callback=self.__solver
            )
        )

    def _import_from_key(self) -> None:
        try:
            from .key import solver
            self.__solver = solver
        except FileNotFound:
            pass
