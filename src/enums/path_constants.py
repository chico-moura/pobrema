from dataclasses import dataclass

from src.enums.file_system_enum import FileSystemEnum as En


@dataclass
class PathConstants:
    ROOT = f'{__file__.split(En.PROJECT)[0]}{En.PROJECT}'
    PROBLEM_GROUPS = f'{ROOT}/{En.EXERCICIOS}'
    TEMPLATES = f'{ROOT}/{En.SRC}/{En.SCAFFOLD}/{En.TEMPLATE_REPOSITORY}/{En.TEMPLATES}'
    LOCK_TEMPLATE = f'{TEMPLATES}/{En.LOCK_TEMPLATE}'
    PROBLEM_TEMPLATE = f'{TEMPLATES}/{En.PROBLEM_TEMPLATE}'
    PROBLEM_INIT_TEMPLATE = f'{TEMPLATES}/{En.PROBLEM_INIT_TEMPLATE}'
    KEY_TEMPLATE = f'{TEMPLATES}/{En.KEY_TEMPLATE}'
    KEY_INIT_TEMPLATE = f'{TEMPLATES}/{En.KEY_INIT_TEMPLPATE}'
