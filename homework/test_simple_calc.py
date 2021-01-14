import unittest


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y


class TestCalculator(unittest.TestCase):
    def test_multiply_string(self):
        with self.assertRaises(TypeError):
            multiply('2', '16')

    def test_multiply_number(self):
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(0, 1), 0)
        self.assertEqual(multiply(0, -1), 0)

        self.assertEqual(multiply(2, 0.4), 0.8)
        self.assertEqual(multiply(0.1, 0.5), 0.05)

        self.assertEqual(multiply(12, 12), 144)
        self.assertEqual(multiply(100, 100), 10000)

        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(-5, 5), -25)

    def test_division_string(self):
        with self.assertRaises(TypeError):
            divide('10', '5')
        with self.assertRaises(TypeError):
            divide('3', 3)
        with self.assertRaises(TypeError):
            divide(1, '1')

    def test_division_zero(self):
        with self.assertRaises(ValueError):
            divide(0, 0)
        with self.assertRaises(ValueError):
            divide(-1, 0)

    def test_division_number(self):
        self.assertEqual(divide(5, 1), 5)
        self.assertEqual(divide(1, 1), 1)
        self.assertEqual(divide(0.333, 1), 0.333)

        self.assertEqual(divide(100, -100), -1)
        self.assertEqual(divide(25, 25), 1)

        self.assertEqual(divide(0, -1), 0)
        self.assertEqual(divide(0, 10), 0)

        self.assertEqual(divide(20, 0.5), 40)
        self.assertEqual(divide(0.5, 20), 0.025)
        self.assertEqual(divide(0.8, 0.2), 4)

    def test_add_string(self):
        with self.assertRaises(TypeError):
            add('1', 1)
        with self.assertRaises(TypeError):
            add(5, '5')
        with self.assertRaises(TypeError):
            add('10', '11')

    def test_add_number(self):
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, 4), -1)

        self.assertEqual(add(5, 5), 10)
        self.assertEqual(add(0.5, 0.75), 1.25)

        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(0, -1), -1)

    def test_str_subtract(self):
        with self.assertRaises(TypeError):
            subtract('4', 5)
        with self.assertRaises(TypeError):
            subtract(2, '3')
        with self.assertRaises(TypeError):
            subtract('1', '11')

    def test_subtract_number(self):
        self.assertEqual(subtract(99, 99), 0)
        self.assertEqual(subtract(99, 98), 1)
        self.assertEqual(subtract(99, 100), -1)

        self.assertEqual(subtract(-10, -10), 0)
        self.assertEqual(subtract(-20, 10), -30)

        self.assertEqual(subtract(10, 0), 10)
        self.assertEqual(subtract(0, 10), -10)


if __name__ == '__main__':
    unittest.main(verbosity=2)