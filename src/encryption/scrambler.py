import os
from pathlib import Path
from src.encryption.errors import FileIsNotPython, FileHasExtension, FileNotFound, TargetFileAlreadyExists
from src.encryption.char_swapper import CharSwapper


class Scrambler:
    __file: str
    __char_swapper: CharSwapper

    def __init__(self, file) -> None:
        self.__file = file
        if not Path(file).is_file():
            raise FileNotFound(file)

    def encrypt(self) -> None:
        new_name = self.__get_encrypted_file_name()
        if self.__file_is_python() and not self.__target_file_already_exists(new_name):
            self.__set_to_encrypt()
            self.__translate()
            self.__rename(new_name)

    def decrypt(self) -> None:
        new_name = self.__get_decrypted_file_name()
        if self.__file_has_no_extension() and not self.__target_file_already_exists(new_name):
            self.__set_to_decrypt()
            self.__translate()
            self.__rename(new_name)

    def __set_to_encrypt(self) -> None:
        self.__char_swapper = CharSwapper.to_encrypt()

    def __set_to_decrypt(self) -> None:
        self.__char_swapper = CharSwapper.to_decrypt()

    def __translate(self) -> None:
        with open(self.__file, 'r') as file:
            original_content = file.read()

        new_content = self.__translate_content(original_content)

        with open(self.__file, 'w') as file:
            file.write(new_content)

    def __translate_content(self, content: str) -> str:
        return ''.join([self.__char_swapper.swap(char) for char in content])

    def __rename(self, new_name: str) -> None:
        os.rename(self.__file, new_name)

    def __get_encrypted_file_name(self) -> str:
        return self.__file.split('.')[0]

    def __get_decrypted_file_name(self) -> str:
        return f'{self.__file}.py'

    def __file_is_python(self) -> bool:
        extension = self.__file.split('.')[-1]
        file_is_python = extension == 'py'
        if not file_is_python:
            raise FileIsNotPython(self.__file)
        return file_is_python

    def __file_has_no_extension(self) -> bool:
        file_has_no_extension = '.' not in self.__file
        if not file_has_no_extension:
            raise FileHasExtension(self.__file)
        return file_has_no_extension

    def __target_file_already_exists(self, target_file: str) -> bool:
        target_file_already_exists = Path(target_file).is_file()
        if target_file_already_exists:
            raise TargetFileAlreadyExists(self.__file, target_file)
        return target_file_already_exists
