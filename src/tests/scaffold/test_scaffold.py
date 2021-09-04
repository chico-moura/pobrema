import os
from pathlib import Path
from unittest import TestCase
from shutil import rmtree

from mockito import unstub, when

from src.scaffold.scaffold import Scaffold, PathConstants


class TestScaffold(TestCase):
    def setUp(self) -> None:
        self.group_name = 'group_name'
        self.problem_name = 'problem_name'
        self.fake_tamplate = 'fake_template'
        self.fake_content = 'fake_content'
        self.fake_path = 'fake_path'
        self.scaffold = Scaffold(self.group_name, self.problem_name)

    def tearDown(self) -> None:
        unstub()

    def test_write_to_file_WHEN_no_template_given_THEN_creates_file(self) -> None:
        self.scaffold._write_to_file(self.fake_path)

        self.assertTrue(Path(self.fake_path).is_file())
        os.remove(self.fake_path)

    def test_write_to_file_WHEN_template_given_THEN_creates_file(self) -> None:
        self.scaffold._write_to_file(self.fake_path, self.fake_content)

        self.assertTrue(Path(self.fake_path).is_file())
        os.remove(self.fake_path)

    def test_write_to_file_WHEN_template_given_THEN_content_is_writen(self) -> None:
        expected_content = self.fake_content

        self.scaffold._write_to_file(self.fake_path, expected_content)
        with open(self.fake_path, 'r') as file:
            actual_content = file.read()

        self.assertEqual(expected_content, actual_content)


