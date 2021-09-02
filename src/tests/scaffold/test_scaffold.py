import os
from pathlib import Path
from unittest import TestCase
from shutil import rmtree

from src.scaffold.scaffold import Scaffold, PathConstants


class TestScaffold(TestCase):
    def setUp(self) -> None:
        self.group_name = 'foo'
        self.problem_name = 'bar'
        self.solution_dir = f'{PathConstants.SOLUTION_GROUPS}/{self.group_name}'
        self.problem_dir = f'{PathConstants.PROBLEM_GROUPS}/{self.group_name}'
        self.scaffold = Scaffold(self.group_name, self.problem_name)

    def tearDown(self) -> None:
        rmtree(self.solution_dir)
        rmtree(self.problem_dir)

    def test_create_WHEN_nothing_exists_THEN_creates_problem_directory(self) -> None:
        self.scaffold.create()

        problem_dir = Path(self.problem_dir)
        self.assertTrue(problem_dir.is_dir())

    def test_create_WHEN_nothing_exists_THEN_creates_solution_directory(self) -> None:
        self.scaffold.create()

        solution_dir = Path(self.solution_dir)
        self.assertTrue(solution_dir.is_dir())
