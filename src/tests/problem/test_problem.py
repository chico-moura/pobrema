from typing import Callable
from unittest import TestCase
from mockito import when, unstub

from src.problem import Problem


class Example(Problem):
    def __init__(self, user_callback: Callable, solver_callback: Callable) -> None:
        super().__init__('foo', user_callback, solver_callback)

    def create_input(self) -> int:
        return 5


class TestProblem(TestCase):
    def setUp(self) -> None:
        when(Example).print_error()

    def tearDown(self) -> None:
        unstub()

    def test_solve_WHEN_results_match_THEN_returns_true(self) -> None:
        problem = Example(lambda x: x * 2, lambda y: y * 2)

        problem.solve()

        self.assertTrue(problem.complete)

    def test_solve_WHEN_results_do_not_match_THEN_returns_false(self) -> None:
        problem = Example(lambda x: x + 1, lambda y: y + 2)

        problem.solve()

        self.assertFalse(problem.complete)
