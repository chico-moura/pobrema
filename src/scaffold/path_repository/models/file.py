from src.scaffold.path_repository.models import BasicPath


class File(BasicPath):
    def _create(self, content: str = None) -> None:
        if not content:
            content = ''
        with open(self.to_string, 'w') as file:
            file.write(content)
