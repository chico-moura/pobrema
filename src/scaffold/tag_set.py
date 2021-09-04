from dataclasses import dataclass

from src.enums.file_system_enum import FileSystemEnum


@dataclass
class Tags:
    __tags: {str, str}

    def __init__(self, problem: str) -> None:
        pascal = self._to_pascal(problem)
        self.__tags = {
            'snake_name': problem,
            'pascal_name': pascal,
            'problem_name': f'{pascal}Problem'
        }

    def replace(self, text: str) -> str:
        for tag in self.__tags.keys():
            actual_tag = f'{FileSystemEnum.TAG_SYMBOL}{tag}{FileSystemEnum.TAG_SYMBOL}'
            replacement = self.__tags[tag]
            text = text.replace(actual_tag, replacement)
        return text

    @staticmethod
    def _to_pascal(name: str) -> str:
        return ''.join(char for char in name.title() if not char.isspace() and not char == '_')
