import os
from pathlib import Path
from unittest import TestCase

from src.scaffold.path_repository.models import File
from src.errors import PathAlreadyExistsError


class TestFile(TestCase):
    def setUp(self) -> None:
        self.fake_file_name = 'fake_file_name'
        self.fake_content = 'fake_content'

    def tearDown(self) -> None:
        if Path(self.fake_file_name).exists():
            os.remove(self.fake_file_name)

    def get_file_content(self) -> str:
        with open(self.fake_file_name, 'r') as file:
            return file.read()

    def test_init_WHEN_file_does_not_exists_THEN_create_file(self) -> None:
        File(self.fake_file_name)

        path = Path(self.fake_file_name)
        self.assertTrue(path.exists())

    def test_init_WHEN_file_already_exists_THEN_throws_path_already_exists_error(self) -> None:
        with open(self.fake_file_name, 'w'):
            pass

        self.assertRaises(PathAlreadyExistsError, lambda: File(path=self.fake_file_name))

    def test_init_WHEN_no_content_given_THEN_creates_empty_file(self) -> None:
        expected_content = ''

        File(path=self.fake_file_name)

        actual_content = self.get_file_content()
        self.assertEqual(expected_content, actual_content)

    def test_init_WHEN_content_is_given_THEN_writes_content_to_file_created(self) -> None:
        expected_content = self.fake_content

        File(path=self.fake_file_name, content=expected_content)

        actual_content = self.get_file_content()
        self.assertEqual(expected_content, actual_content)

    def test_content_WHEN_called_THEN_returns_file_content(self) -> None:
        expected_content = self.fake_content
        file = File(path=self.fake_file_name, content=expected_content)

        actual_content = file.content

        self.assertEqual(expected_content, actual_content)
