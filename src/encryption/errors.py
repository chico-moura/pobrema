class FileIsNotPython(Exception):
    def __init__(self, file: str) -> None:
        self.message = f'Could not encrypt: "{file}" is not a Python file (missing .py extension)'
        super().__init__(self.message)


class FileHasExtension(Exception):
    def __init__(self, file: str) -> None:
        self.message = f'Could not decrypt: "{file}" has extension (can only decrypt files without extension)'
        super().__init__(self.message)


class FileNotFound(Exception):
    def __init__(self, file: str) -> None:
        self.message = f'File not found: "{file}"'
        super().__init__(self.message)


class TargetFileAlreadyExists(Exception):
    def __init__(self, original_file: str, target_file) -> None:
        self.message = f'Could not encrypt or decrypt "{original_file}": "{target_file}" already exists'
        super().__init__(self.message)
