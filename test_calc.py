import unittest as ut
import calc

class TestCalc(ut.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
    
    # @ut.skip("demonstrating skipping")
    def test_subtract(self):
        self.assertEqual(calc.subtract(5, 3), 2)
        self.assertEqual(calc.subtract(0, 0), 0)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 3), 6)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    # @ut.skipIf(True, "demonstrating skipping")
    def test_divide(self):
        self.assertEqual(calc.divide(6, 3), 2)
        self.assertEqual(calc.divide(-6, -3), 2)
        self.assertEqual(calc.divide(-6, 3), -2)
        with self.assertRaises(ValueError): #divide function should raise error otherwise fails test case.
            calc.divide(1, 0)

if __name__ == '__main__':
    ut.main()