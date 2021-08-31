from unittest import TestCase
from src.encryption.char_swapper import CharSwapper


class TestCharSwapper(TestCase):
    def test_to_encrypt_WHEN_called_THEN_returns_instance(self) -> None:
        swapper = CharSwapper.to_encrypt()

        self.assertIsInstance(swapper, CharSwapper)

    def test_to_decrypt_WHEN_called_THEN_returns_instance(self) -> None:
        swapper = CharSwapper.to_decrypt()

        self.assertIsInstance(swapper, CharSwapper)

    def test_swap_WHEN_called_with_character_THEN_returns_different_character(self) -> None:
        swapper = CharSwapper.to_encrypt()
        original_char = 'x'

        final_char = swapper.swap(original_char)

        self.assertNotEqual(original_char, final_char)

    def test_swap_WHEN_called_with_character_THEN_does_not_return_empty_string(self) -> None:
        swapper = CharSwapper.to_encrypt()
        original_char = 'x'
        empty_string = ''

        final_char = swapper.swap(original_char)

        self.assertNotEqual(final_char, empty_string)
