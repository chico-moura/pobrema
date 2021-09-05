from src.scaffold.path_creation.basic_path import BasicPath
from src.enums import FileSystemEnum


class File(BasicPath):
    def _create(self, content: str = None) -> None:
        self._assure_extension()
        with open(self.path, 'w') as file:
            if content:
                file.write(content)

    @property
    def content(self) -> str:
        with open(self.path, 'r') as file:
            return file.read()

    @property
    def has_extension(self) -> bool:
        return self.path.split('.')[-1] == FileSystemEnum.FILE_EXTENSION

    def _assure_extension(self) -> None:
        if not self.has_extension:
            self.set_path(f'{self.path}.{FileSystemEnum.FILE_EXTENSION}')
