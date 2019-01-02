"""
Unit tests for the calculator library
"""

from .calculator import add, subtract


class TestCalculator:

    def test_addition(self):
        assert add(2, 2) == 4

    def test_subtraction(self):
        assert subtract(4,2) == 2

