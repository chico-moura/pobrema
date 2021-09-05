import os
from pathlib import Path
from shutil import rmtree
from unittest import TestCase

from src.errors import PathAlreadyExistsError
from src.scaffold import Scaffold
from src.enums import FileSystemEnum as En
from src.enums import PathConstants


class TestScaffold(TestCase):
    def setUp(self) -> None:
        self.group_name = 'foo'
        self.problem_name = 'bar'
        self.group_path = f'{PathConstants.PROBLEM_GROUPS}/{self.group_name}'
        self.problem_dir_path = f'{self.group_path}/{self.problem_name}'
        self.problem_path = f'{self.problem_dir_path}/{self.problem_name}.{En.FILE_EXTENSION}'
        self.scaffold = Scaffold(self.group_name, self.problem_name)

    def tearDown(self) -> None:
        if Path(self.group_path).exists():
            rmtree(self.group_path)

    def test_create_WHEN_nothing_exists_THEN_creates_problem(self) -> None:
        self.scaffold.create()

        self.assertTrue(Path(self.problem_path).is_file())

    def test_create_WHEN_group_exists_THEN_creates_problem(self) -> None:
        os.mkdir(self.group_path)

        self.scaffold.create()

        self.assertTrue(Path(self.problem_path).is_file())

    def test_create_WHEN_problem_directory_exists_THEN_does_not_create_problem(self) -> None:
        os.mkdir(self.group_path)
        os.mkdir(self.problem_dir_path)

        self.scaffold.create()

        self.assertFalse(Path(self.problem_path).is_file())

    def test_validate_arguments_WHEN_problem_exists_THEN_throws_path_already_exists_error(self) -> None:
        os.mkdir(self.group_path)
        os.mkdir(self.problem_dir_path)

        self.assertRaises(PathAlreadyExistsError, lambda: self.scaffold._validate_arguments())

    def test_create_structure_WHEN_called_THEN_creates_key_file(self) -> None:
        key_file = f'{self.problem_dir_path}/{En.KEY}/{En.KEY}.{En.FILE_EXTENSION}'

        self.scaffold._create_structure()

        self.assertTrue(Path(key_file).is_file())
