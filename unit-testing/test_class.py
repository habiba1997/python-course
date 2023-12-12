import calculate_class
import unittest

# @unittest.skip("reason to skip: skipping for some reason")
class TestCalculateClass(unittest.TestCase):
    def tearDown(self):
        print("finally successfully passed.....")

    def setUp(self):
        self.calculate = calculate_class.Calculate()

    def test_add(self):
        self.assertEqual(self.calculate.add(1, 2), 3)
        self.assertEqual(self.calculate.add(5, 2), 7)
        self.assertEqual(self.calculate.add(3, 7), 10)

    @unittest.skipIf(True, "reason to skip: skipping for some reason")
    def test_multiply(self):
        self.assertEqual(self.calculate.multiply(1, 2), 2)
        self.assertEqual(self.calculate.multiply(5, 2), 10)
        self.assertEqual(self.calculate.multiply(3, 7), 21)

    def test_divide(self):
        self.assertEqual(self.calculate.divide(9, 3), 3)
        #  ensure that our function is capable of raising an exception when givin a zero
        with self.assertRaises(ValueError):
            self.calculate.divide(9, 0)
