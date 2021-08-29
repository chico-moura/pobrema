import os
from shutil import copy2


class FileFactory:
    template: str = '/'.join(__file__.split('/')[0:-2]) + '/factories/template.py'

    @classmethod
    def create_python_file(cls, file: str) -> None:
        name = cls.__format_python_file_name(file)
        copy2(cls.template, name)

    @classmethod
    def create_file_without_extension(cls, file: str) -> None:
        file = open(file, 'w')
        file.close()

    @classmethod
    def remove_files(cls, *files: str) -> None:
        for file in files:
            if os.path.isfile(file):
                os.remove(file)

    @staticmethod
    def __format_python_file_name(file) -> str:
        name = file
        if '.' not in name:
            name += '.py'
        return name
