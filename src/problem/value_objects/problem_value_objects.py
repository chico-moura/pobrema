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

    def add(self, score: Score) -> None:
        self.max += score.max
        self.score += score.score

    @property
    def complete(self) -> bool:
        return self.score == self.max

    @classmethod
    def merge(cls, *scores: Score) -> Score:
        final_score = Score(max=0)
        for score in scores:
            final_score.add(score)
        return final_score

    def __str__(self):
        return f'{self.score}/{self.max}'
