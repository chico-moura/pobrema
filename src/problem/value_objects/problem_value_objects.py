from __future__ import annotations
from dataclasses import dataclass
from typing import Callable


@dataclass
class CallbackPair:
    user: Callable
    solver: Callable


@dataclass
class Score:
    max: int
    score: int = 0

    def increment(self) -> None:
        self.score += 1

    @property
    def complete(self) -> bool:
        return self.score == self.max

    def __str__(self):
        return f'{self.score}/{self.max}'
