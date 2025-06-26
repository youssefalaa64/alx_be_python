import unittest
from simple_calculator import SimpleCalculator
class test_calculator(unittest.TestCase) :
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_add(self) :
        self.assertEqual(self.calc(5, 5), 10)
    def test_subtract(self) :
        self.assertEqual(self.calc(5, 2 ), 3)
    def test_multiply(self):
        self.assertEqual(self.calc(5, 5), 25)
    def test_divide(self):
        self.assertEqual(self.calc(10,5), 2)

