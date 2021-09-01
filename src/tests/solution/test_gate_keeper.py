from unittest import TestCase
from mockito import unstub, when, mock, verify

from src.encryption import Scrambler
from src.problem import GateKeeper


class Example(GateKeeper):
    def _solve_problems(self) -> bool:
        return True

    def _import_from_key(self) -> None:
        pass


class TestGateKeeper(TestCase):
    def setUp(self) -> None:
        key_mock = mock(Scrambler)
        key_mock.is_python = False
        when(key_mock).encrypt()
        when(key_mock).decrypt()
        when(GateKeeper)._get_key().thenReturn(key_mock)
        self.gate_keeper = Example()

    def tearDown(self) -> None:
        unstub()

    def test_solve_WHEN_solve_problems_returns_true_THEN_calls_unlock(self) -> None:
        when(self.gate_keeper)._solve_problems().thenReturn(True)
        when(self.gate_keeper)._unlock()

        self.gate_keeper.solve()

        verify(self.gate_keeper)._unlock()
