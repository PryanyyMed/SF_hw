import pytest
import sys
sys.path.append('..')

from app.Calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correct(self):
        assert self.calc.multiply(self, 1, 2) == 3

    def test_division_correct(self):
        assert self.calc.division(self, 10, 5) == 2

    def test_subtraction_correct(self):
        assert self.calc.subtraction(self, 16, 9) == 7

    def test_adding_correct(self):
        assert self.calc.adding(self, 4, 5) == 9