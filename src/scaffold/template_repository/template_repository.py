from src.scaffold.path_creation import File
from src.scaffold.template_repository.tag_set import Tags
from src.enums import PathConstants


class TemplateRepo:
    __tags: Tags

    def __init__(self, problem_name: str) -> None:
        self.__tags = Tags(problem_name)

    @property
    def problem(self) -> str:
        return self._get_content(PathConstants.PROBLEM_TEMPLATE)

    @property
    def key(self) -> str:
        return self._get_content(PathConstants.KEY_TEMPLATE)

    @property
    def lock(self) -> str:
        return self._get_content(PathConstants.LOCK_TEMPLATE)

    @property
    def problem_init(self) -> str:
        return self._get_content(PathConstants.PROBLEM_INIT_TEMPLATE)

    @property
    def key_init(self) -> str:
        return self._get_content(PathConstants.KEY_INIT_TEMPLATE)

    def _get_content(self, template_path: str) -> str:
        template = File(template_path, accept_existing=True)
        return self.__tags.replace(template.content)
