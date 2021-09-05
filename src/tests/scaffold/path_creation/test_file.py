import os
from pathlib import Path
from unittest import TestCase

from mockito import when, unstub

from src.enums import FileSystemEnum
from src.scaffold.path_creation import File
from src.errors import PathAlreadyExistsError


class TestFile(TestCase):
    def setUp(self) -> None:
        self.fake_file_name = 'fake_file_name.py'
        self.fake_file_name_no_extension = 'fake_file_name'
        self.fake_content = 'fake_content'

    def tearDown(self) -> None:
        unstub()
        self.remove(self.fake_file_name)
        self.remove(self.fake_file_name_no_extension)

    @staticmethod
    def remove(file: str) -> None:
        if Path(file).exists():
            os.remove(file)

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

    def test_init_WHEN_path_has_no_extension_THEN_creates_file_with_extension(self) -> None:
        name_without_extension = 'fake_file_name'
        name_with_extension = f'{name_without_extension}.{FileSystemEnum.FILE_EXTENSION}'

        File(path=name_without_extension)

        path = Path(name_with_extension)
        self.assertTrue(path.is_file())

    def test_content_WHEN_called_THEN_returns_file_content(self) -> None:
        expected_content = self.fake_content
        file = File(path=self.fake_file_name, content=expected_content)

        actual_content = file.content

        self.assertEqual(expected_content, actual_content)

    def test_assure_extension_WHEN_file_has_no_extension_THEN_assigns_extension(self) -> None:
        file_name = 'foo'
        expected_name = f'{file_name}.{FileSystemEnum.FILE_EXTENSION}'
        when(File)._create(None)
        file = File(file_name)

        file._assure_extension()

        self.assertEqual(expected_name, file.path)

    def test_has_extension_WHEN_file_is_python_THEN_returns_true(self) -> None:
        file_name = 'foo.py'
        when(File)._create(None)
        file = File(file_name)

        has_extension = file.has_extension

        self.assertTrue(has_extension)

    def test_has_extension_WHEN_file_has_no_extension_THEN_returns_false(self) -> None:
        file_name = 'foo'
        when(File)._create(None)
        file = File(file_name)

        has_extension = file.has_extension

        self.assertFalse(has_extension)
