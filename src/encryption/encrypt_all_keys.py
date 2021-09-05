import os
from pathlib import Path

from src.encryption.scrambler import Scrambler
from src.enums import PathConstants
from src.enums import FileSystemEnum as En


class EncryptAllKeys:
    @classmethod
    def execute(cls) -> None:
        keys_paths = cls._get_keys_paths()
        cls._encrypt_keys(keys_paths)

    @classmethod
    def _get_keys_paths(cls) -> [str]:
        keys = []
        groups = cls._get_sub_dirs(PathConstants.PROBLEM_GROUPS)
        for group in groups:
            problems = cls._get_sub_dirs(group)
            for problem in problems:
                key = f'{problem}/{En.KEY}/{En.KEY}.{En.FILE_EXTENSION}'
                if Path(key).exists():
                    keys.append(key)
        return keys

    @staticmethod
    def _get_sub_dirs(path: str) -> [str]:
        return [f'{path}/{sub_dir}' for sub_dir in os.listdir(path) if not sub_dir[:2] == '__']

    @staticmethod
    def _encrypt_keys(paths: [str]) -> None:
        [Scrambler(key).encrypt() for key in paths]


if __name__ == '__main__':
    EncryptAllKeys.execute()
