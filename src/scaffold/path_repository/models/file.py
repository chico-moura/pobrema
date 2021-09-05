from src.scaffold.path_repository.models import BasicPath
from src.enums import FileSystemEnum


class File(BasicPath):
    def _create(self, content: str = None) -> None:
        if self.path.split('.')[-1] != FileSystemEnum.FILE_EXTENSION:
            self.__path = f'{self.path}{FileSystemEnum.FILE_EXTENSION}'
        with open(self.path, 'w') as file:
            if content:
                file.write(content)

    @property
    def content(self) -> str:
        with open(self.path, 'r') as file:
            return file.read()
