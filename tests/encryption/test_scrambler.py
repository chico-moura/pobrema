import pathlib
from unittest import TestCase
from src.encryption.scrambler import Scrambler
from src.encryption import FileHasExtension, FileIsNotPython, FileNotFound, TargetFileAlreadyExists
from tests.encryption.factories.file_factory import FileFactory


class TestScrambler(TestCase):
    unencrypted_file_name: str
    encrypted_file: str

    def setUp(self) -> None:
        self.python_file = 'foo.py'
        self.encrypted_file = 'foo'
        self.python_file_path = pathlib.Path(self.python_file)
        self.encrypted_file_path = pathlib.Path(self.encrypted_file)

    def tearDown(self) -> None:
        FileFactory.remove_files(self.encrypted_file, self.python_file)

    @staticmethod
    def read_file(file: str) -> str:
        opened_file = open(file, 'r')
        expected_content = opened_file.read()
        opened_file.close()
        return expected_content

    def test_init_WHEN_file_doesnt_exists_THEN_raises_file_not_found_error(self) -> None:
        self.assertRaises(FileNotFound, lambda: Scrambler(self.python_file))

    def test_encrypt_WHEN_called_with_python_file_THEN_creates_file_without_extension(self) -> None:
        FileFactory.create_python_file(self.python_file)
        scrambler = Scrambler(self.python_file)

        scrambler.encrypt()

        self.assertTrue(self.encrypted_file_path.is_file())

    def test_encrypt_WHEN_called_with_python_file_THEN_remove_python_file(self) -> None:
        FileFactory.create_python_file(self.python_file)
        scrambler = Scrambler(self.python_file)

        scrambler.encrypt()

        self.assertFalse(self.python_file_path.is_file())

    def test_encrypt_WHEN_called_with_non_python_file_THEN_raises_file_is_not_python_error(self) -> None:
        FileFactory.create_file_without_extension(self.encrypted_file)
        scrambler = Scrambler(self.encrypted_file)

        self.assertRaises(FileIsNotPython, lambda: scrambler.encrypt())

    def test_encrypt_WHEN_target_file_name_is_taken_THEN_raises_target_file_already_exists(self) -> None:
        FileFactory.create_python_file(self.python_file)
        FileFactory.create_file_without_extension(self.encrypted_file)
        scrambler = Scrambler(self.python_file)

        self.assertRaises(TargetFileAlreadyExists, lambda: scrambler.encrypt())

    def test_decrypt_WHEN_called_with_file_without_extension_THEN_creates_decrypted_python_file(self) -> None:
        FileFactory.create_file_without_extension(self.encrypted_file)
        scrambler = Scrambler(self.encrypted_file)

        scrambler.decrypt()

        self.assertTrue(self.python_file_path.is_file())

    def test_decrypt_WHEN_called_with_file_without_extension_THEN_remove_file_without_extension(self) -> None:
        FileFactory.create_file_without_extension(self.encrypted_file)
        scrambler = Scrambler(self.encrypted_file)

        scrambler.decrypt()

        self.assertFalse(self.encrypted_file_path.is_file())

    def test_decrypt_WHEN_called_with_python_file_THEN_raises_file_has_extension_error(self) -> None:
        FileFactory.create_python_file(self.python_file)
        scrambler = Scrambler(self.python_file)

        self.assertRaises(FileHasExtension, lambda: scrambler.decrypt())

    def test_decrypt_WHEN_target_file_name_is_taken_THEN_raises_target_file_already_exists(self) -> None:
        FileFactory.create_python_file(self.python_file)
        FileFactory.create_file_without_extension(self.encrypted_file)
        scrambler = Scrambler(self.encrypted_file)

        self.assertRaises(TargetFileAlreadyExists, lambda: scrambler.decrypt())

    def test_decrypt_WHEN_called_with_encrypted_file_THEN_preserve_file_content(self) -> None:
        FileFactory.create_python_file(self.python_file)
        expected_content = self.read_file(self.python_file)

        Scrambler(self.python_file).encrypt()
        Scrambler(self.encrypted_file).decrypt()

        actual_content = self.read_file(self.python_file)
        self.assertEqual(actual_content, expected_content)
