import os
from pathlib import Path
from shutil import rmtree
from unittest import TestCase

from src.scaffold.path_creation import Dir
from src.errors import PathAlreadyExistsError
from src.enums import FileSystemEnum


class TestDir(TestCase):
    def setUp(self) -> None:
        self.fake_content = 'fake_content'
        self.fake_dir_path = 'fake_dir_path'
        self.child_dir_name = 'fake_child_dir_name'
        self.child_file_name = 'child_file_name.py'
        self.init_file_path = f'{self.fake_dir_path}/{FileSystemEnum.INIT_FILE}'
        self.child_dir_path = f'{self.fake_dir_path}/{self.child_dir_name}'
        self.child_dir_init_path = f'{self.child_dir_path}/{FileSystemEnum.INIT_FILE}'
        self.child_file_path = f'{self.fake_dir_path}/{self.child_file_name}'

    def tearDown(self) -> None:
        if Path(self.fake_dir_path).exists():
            rmtree(self.fake_dir_path)

    def test_init_WHEN_no_content_given_THEN_creates_empty_dir(self) -> None:
        Dir(path=self.fake_dir_path)

        created_dir = Path(self.fake_dir_path)
        self.assertTrue(created_dir.is_dir())

    def test_init_WHEN_dir_exists_THEN_raises_path_already_exists_error(self) -> None:
        os.mkdir(path=self.fake_dir_path)

        self.assertRaises(PathAlreadyExistsError, lambda: Dir(path=self.fake_dir_path))

    def test_init_WHEN_content_is_given_THEN_creates_init_file(self) -> None:
        Dir(path=self.fake_dir_path, init_content='')

        init_file = Path(self.init_file_path)

        self.assertTrue(init_file.is_file())

    def test_init_WHEN_content_is_given_THEN_writes_content_to_init_file(self) -> None:
        expected_content = self.fake_content

        Dir(self.fake_dir_path, expected_content)
        with open(self.init_file_path, 'r') as file:
            actual_content = file.read()

        self.assertEqual(expected_content, actual_content)

    def test_init_WHEN_dir_exists_and_accept_existing_is_true_THEN_accepts_existing_dir(self) -> None:
        os.mkdir(path=self.fake_dir_path)

        Dir(path=self.fake_dir_path, accept_existing=True)

        self.assertTrue(Path(self.fake_dir_path).is_dir())

    def test_init_WHEN_accept_existing_is_true_and_dir_does_not_exist_THEN_creates_dir(self) -> None:
        Dir(path=self.fake_dir_path, accept_existing=True)

        self.assertTrue(Path(self.fake_dir_path).is_dir())

    def test_spawn_dir_WHEN_no_content_given_THEN_creates_sub_dir(self) -> None:
        mother_dir = Dir(self.fake_dir_path)

        mother_dir.spawn_dir(self.child_dir_name)
        child_path = Path(f'{self.fake_dir_path}/{self.child_dir_name}')

        self.assertTrue(child_path.is_dir())

    def test_spawn_dir_WHEN_content_is_given_THEN_creates_init_file_inside_sub_dir(self) -> None:
        mother_dir = Dir(self.fake_dir_path)

        mother_dir.spawn_dir(self.child_dir_name)

        self.assertTrue(self.child_dir_init_path)

    def test_spawn_dir_WHEN_mother_dir_was_created_with_accept_existing_THEN_creates_child_dir(self) -> None:
        child_dir_name = 'child'
        expected_created_path = f'{self.fake_dir_path}/{child_dir_name}'
        os.mkdir(path=self.fake_dir_path)
        mother_dir = Dir(path=self.fake_dir_path, accept_existing=True)

        mother_dir.spawn_dir(child_dir_name)

        self.assertTrue(Path(expected_created_path).is_dir())

    def test_spawn_file_WHEN_called_THEN_creates_file(self) -> None:
        mother_dir = Dir(self.fake_dir_path)

        mother_dir.spawn_file(self.child_file_name, self.fake_content)
        path = Path(self.child_file_path)

        self.assertTrue(path.is_file())
