from unittest import TestCase

from src.scaffold.template_repository.tag_set import Tags
from src.enums import FileSystemEnum as En


class TestTags(TestCase):
    def setUp(self) -> None:
        self.tag_function = 'function'
        self.tag_gate_keeper = 'gate_keeper'
        self.tag_problem = 'problem'
        self.fake_name = 'fake_name'
        self.tags = Tags(problem=self.fake_name)

    def tearDown(self) -> None:
        pass

    def test_replace_WHEN_text_has_tags_THEN_returns_text_with_tags_replaced_by_its_values(self) -> None:
        original_content = f'function={En.TAG_SYMBOL}{self.tag_function}{En.TAG_SYMBOL}' \
                           f'gate_keeper={En.TAG_SYMBOL}{self.tag_gate_keeper}{En.TAG_SYMBOL}' \
                           f'problem={En.TAG_SYMBOL}{self.tag_problem}{En.TAG_SYMBOL}'
        expected_content = f'function=fake_name' \
                           f'gate_keeper=FakeName' \
                           f'problem=FakeNameProblem'

        actual_content = self.tags.replace(original_content)

        self.assertEqual(expected_content, actual_content)

    def test_to_pascal_WHEN_name_is_snake_case_THEN_returns_name_in_pascal_case(self) -> None:
        original_name = 'fake_name'
        expected_name = 'FakeName'

        actual_name = self.tags._to_pascal(original_name)

        self.assertEqual(expected_name, actual_name)
