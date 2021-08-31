from __future__ import annotations
from src.encryption.characters import Characters


class CharSwapper:
    __original: [str]
    __final: [str]

    def __init__(self, original: [str], final: [str]) -> None:
        self.__original = original
        self.__final = final

    @classmethod
    def to_encrypt(cls) -> CharSwapper:
        return cls(original=Characters.ordered, final=Characters.scrambled)

    @classmethod
    def to_decrypt(cls) -> CharSwapper:
        return cls(original=Characters.scrambled, final=Characters.ordered)

    def swap(self, char: str) -> str:
        index = self.__original.index(char)
        return self.__final[index]
