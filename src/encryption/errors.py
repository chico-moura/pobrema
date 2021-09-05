from src.errors.basic_exception import BasicException
from src.enums import FileSystemEnum as En


class FileWithoutExtensionError(BasicException):
    def __init__(self, file: str) -> None:
        self.message = f'Could not encrypt "{file}": was expecting a file with .{En.FILE_EXTENSION} extension'


class FileHasExtensionError(BasicException):
    def __init__(self, file: str) -> None:
        self.message = f'Could not decrypt: "{file}" has extension (can only decrypt files without extension)'


class TargetFileAlreadyExistsError(BasicException):
    def __init__(self, original_file: str, target_file) -> None:
        self.message = f'Could not encrypt or decrypt "{original_file}": "{target_file}" already exists'
