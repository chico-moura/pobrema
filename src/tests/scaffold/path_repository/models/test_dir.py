import os
from pathlib import Path
from unittest import TestCase


class TestDir(TestCase):
    def setUp(self) -> None:
        self.fake_dir_name = 'fake_dir_name'

    def tearDown(self) -> None:
        if Path(self.fake_dir_name).exists():
            os.remove(self.fake_dir_name)

    def test_init_
