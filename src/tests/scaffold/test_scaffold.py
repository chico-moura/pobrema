from pathlib import Path
from shutil import rmtree
from unittest import TestCase

from src.scaffold import Scaffold
from src.enums import FileSystemEnum as En
from src.enums import PathConstants


class TestScaffold(TestCase):
    def setUp(self) -> None:
        self.group_name = 'foo'
        self.problem_name = 'bar'
        self.group_path = f'{PathConstants.PROBLEM_GROUPS}/{self.group_name}'
        self.problem_path = f'{self.group_path}/{self.problem_name}/{self.problem_name}.{En.FILE_EXTENSION}'
        self.scaffold = Scaffold(self.group_name, self.problem_name)

    def tearDown(self) -> None:
        if Path(self.group_path).exists():
            rmtree(self.group_path)

    def test_scaffold_WHEN_nothing_exists_THEN_creates_structure(self) -> None:
        self.scaffold.create()

        self.assertTrue(Path(self.problem_path).is_file())

    def test_scaffold_WHEN