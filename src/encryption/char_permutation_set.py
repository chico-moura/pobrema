from __future__ import annotations
from dataclasses import dataclass
from src.encryption.characters import Characters


@dataclass
class CharPermutationSet:
    original: [str]
    final: [str]
    __characters = Characters()

    @classmethod
    def to_encrypt(cls) -> CharPermutationSet:
        return cls(original=cls.__characters.original, final=cls.__characters.scrambled)

    @classmethod
    def to_decrypt(cls) -> CharPermutationSet:
        return cls(original=cls.__characters.scrambled, final=cls.__characters.original)
