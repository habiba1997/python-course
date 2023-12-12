import unittest
import main


class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertEqual(main.add(1, 2), 3)
        self.assertEqual(main.add(5, 2), 7)
        self.assertEqual(main.add(3, 7), 10)

    def test_multiply(self):
        self.assertEqual(main.multiply(1, 2), 2)
        self.assertEqual(main.multiply(5, 2), 10)
        self.assertEqual(main.multiply(3, 7), 21)

    def test_divide(self):
        self.assertEqual(main.divide(10, 2), 5)
        self.assertEqual(main.divide(9, 3), 3)
        self.assertEqual(main.divide(24, 8), 4)
