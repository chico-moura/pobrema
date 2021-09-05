from pathlib import Path
from shutil import rmtree
from unittest import TestCase

from src.scaffold import Scaffold
from src.enums import FileSystemEnum as En


class TestScaffold(TestCase):
    def setUp(self) -> None:
        self.group = 'foo'
        self.problem = 'bar'
        self.scaffold = Scaffold(self.group, self.problem)

    def tearDown(self) -> None:
        if Path(self.group).exists():
            rmtree(self.group)

    def test_scaffold_WHEN_nothing_exists_THEN_creates_structure(self) -> None:
        expected_file = f'{self.group}/{self.problem}/{En.KEY}/{En.KEY}.{En.FILE_EXTENSION}'
        print(expected_file)

        self.scaffold.create()

        self.assertTrue(Path(expected_file).is_file())