from src.errors.base_exception import BasicException


class PathAlreadyExistsError(BasicException):
    def __init__(self, file: str) -> None:
        self.message = f'Path already exists: {file}'
