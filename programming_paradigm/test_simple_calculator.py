import unittest
from simple_calculator import SimpleCalculator
class test_calculator(unittest.TestCase) :
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self) :
        self.assertEqual(self.calc.add(5, 5), 10)
    def test_subtraction(self) :
        self.assertEqual(self.calc.subtract(5, 2 ), 3)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5, 5), 25)
    def test_divide(self):
        self.assertEqual(self.calc.divide(10,5), 2)

