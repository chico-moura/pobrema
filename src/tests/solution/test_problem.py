from unittest import TestCase
from mockito import when, unstub
from src.solution.problem import Problem


class Example(Problem):
    def create_input(self) -> int:
        return 5


class TestProblem(TestCase):
    def setUp(self) -> None:
        when(Example).alert_failure()

    def tearDown(self) -> None:
        unstub()

    def test_solve_WHEN_results_match_THEN_returns_true(self) -> None:
        problem = Example(lambda x: x * 2, lambda y: y * 2)

        result = problem.solve()

        self.assertTrue(result)

    def teste_solve_WHEN_results_do_not_match_THEN_returns_false(self) -> None:
        problem = Example(lambda x: x + 1, lambda y: y + 2)

        result = problem.solve()

        self.assertFalse(result)
