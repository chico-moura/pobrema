from __future__ import annotations
from src.encryption.characters import Characters


class CharSwapper:
    __original_set: [str]
    __final_set: [str]

    def __init__(self, original: [str], final: [str]) -> None:
        self.__original_set = original
        self.__final_set = final

    @classmethod
    def to_encrypt(cls) -> CharSwapper:
        return cls(original=Characters.ordered, final=Characters.scrambled)

    @classmethod
    def to_decrypt(cls) -> CharSwapper:
        return cls(original=Characters.scrambled, final=Characters.ordered)

    def swap(self, char: str) -> str:
        index = self.__original_set.index(char)
        return self.__final_set[index]
