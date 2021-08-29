import os
from pathlib import Path
from dataclasses import dataclass
from src.encryption.errors import FileIsNotPython, FileHasExtension, FileNotFound, TargetFileAlreadyExists


@dataclass
class CharPermutationSet:
    original: [str]
    target: [str]


class Scrambler:
    __file: str
    __original_char_set: [str]
    __scrambled_char_set: [str]
    __permutation_set: CharPermutationSet
    __original_chars: str = 'abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVXWYZ0123456789,.<>:;\\/\'?|"' \
                            '~^]}[-_=+àáâãèéêêíìĩîóòõôúùũûÁÀÃÂÉÈẼÊÍÌĨÎÓÒÕÔÚÙŨÛ!@#$%*() ¹²³£¢¬{[]§ªº°\n'
    __scrambled_chars: str = '7@A_Û(Înũdi[Ì{Â2vjâ\nìàúPÒ^LN.IG=T²3qhoe6< $Yafò*áêm\\À+]Ùí;1pZÈHº£zXW9Ũ?,' \
                             '!¢-ùèEw4~uÁêéî¹Ó}§]#¬VÔsã5³ôlbÊÍDÉFKS\'ĩx:%rªõ°Ã/8Õ[>RkOMUẼ|)ĨcyBÚûJtgó"0CQ'

    def __init__(self, file) -> None:
        self.__file = file
        self.__original_char_set = list(self.__original_chars)
        self.__scrambled_char_set = list(self.__scrambled_chars)
        if not Path(self.__file).is_file():
            raise FileNotFound(self.__file)

    def encrypt(self) -> None:
        new_name = self.__get_encrypted_file_name()
        if self.__file_is_python() and not self.__target_file_already_exists(new_name):
            self.__set_to_encrypt()
            self.__replace_file(new_name)

    def decrypt(self) -> None:
        new_name = self.__get_decrypted_file_name()
        if self.__file_has_no_extension() and not self.__target_file_already_exists(new_name):
            self.__set_to_decrypt()
            self.__replace_file(new_name)

    def __replace_file(self, new_file: str) -> None:
        text = self.__permute_chars()
        new_file = open(new_file, 'w')
        new_file.write(text)
        new_file.close()
        self.__remove_file()

    def __permute_chars(self) -> str:
        original_text = self.__get_file_text()
        new_text = self.__get_scrambled_text(original_text)
        return new_text

    def __get_file_text(self) -> str:
        created_file = open(self.__file, 'r')
        text = created_file.read()
        created_file.close()
        return text

    def __get_char_replacement(self, char: str) -> str:
        index = self.__permutation_set.original.index(char)
        return self.__permutation_set.target[index]

    def __get_scrambled_text(self, text: str) -> str:
        scrambled_list = [self.__get_char_replacement(char) for char in text]
        scrambled_text = ''.join(scrambled_list)
        return scrambled_text

    def __remove_file(self) -> None:
        if os.path.isfile(self.__file):
            os.remove(self.__file)
        else:
            raise FileNotFound(self.__file)

    def __set_to_encrypt(self) -> None:
        self.__permutation_set = CharPermutationSet(
            original=self.__original_char_set,
            target=self.__scrambled_char_set
        )

    def __set_to_decrypt(self) -> None:
        self.__permutation_set = CharPermutationSet(
            original=self.__scrambled_char_set,
            target=self.__original_char_set
        )

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
