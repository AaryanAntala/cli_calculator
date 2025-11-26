import unittest
# Import the functions we want to test from app.py
from app import add, subtract, multiply, divide, power, modulo

class TestCalculator(unittest.TestCase):

    # Test 1: Addition (Happy Path)
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -5), -10)
        self.assertEqual(add(0, 0), 0)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)

    # Test 2: Subtraction
    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-5, -3), -2)
        self.assertAlmostEqual(subtract(10.5, 3.2), 7.3, places=7)

    # Test 3: Multiplication
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(10, 0), 0) # Edge case: multiply by zero
        self.assertEqual(multiply(-5, 3), -15)
        self.assertEqual(multiply(-4, -2), 8)
        self.assertAlmostEqual(multiply(2.5, 4), 10.0, places=7)

    # Test 4: Division
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(10, 3), 3.3333, places=4) # Floats are tricky, use AlmostEqual
        self.assertEqual(divide(0, 5), 0)
        self.assertEqual(divide(-10, 2), -5)
        self.assertAlmostEqual(divide(7, 2), 3.5, places=7)

    # Test 5: Edge Case (Division by Zero)
    def test_divide_by_zero(self):
        # We expect a ValueError when dividing by zero
        with self.assertRaises(ValueError):
            divide(10, 0)
        with self.assertRaises(ValueError):
            divide(0, 0)

    # Test 6: Power Function
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(10, 2), 100)
        self.assertEqual(power(2, -1), 0.5)
        self.assertAlmostEqual(power(4, 0.5), 2.0, places=7)
        self.assertEqual(power(-2, 3), -8)
        self.assertEqual(power(-2, 2), 4)

    # Test 7: Modulo Function
    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(17, 5), 2)
        self.assertEqual(modulo(20, 4), 0)
        self.assertEqual(modulo(7, 7), 0)
        self.assertAlmostEqual(modulo(10.5, 3), 1.5, places=7)

    # Test 8: Edge Case (Modulo by Zero)
    def test_modulo_by_zero(self):
        # We expect a ValueError when modulo by zero
        with self.assertRaises(ValueError):
            modulo(10, 0)
        with self.assertRaises(ValueError):
            modulo(0, 0)

if __name__ == '__main__':
    unittest.main()