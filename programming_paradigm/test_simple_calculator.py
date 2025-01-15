import unittest
from simple_calculator import SimpleCalculator

class TestCalculator(unittest.TestCase):
    def test_add_positive(self):
        result = SimpleCalculator.add(5,6)
        self.assertEqual(result, 11)
    def test_add_negative(self):
        result = SimpleCalculator.add(-5,6)
        self.assertEqual(result, 1)
    def test_add_both_negative(self):
        result = SimpleCalculator.add(-2, -4):
        self.assertEqual(result, -6)
    