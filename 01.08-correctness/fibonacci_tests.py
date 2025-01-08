import unittest
import fibonacci as fib


class TestFibonacci(unittest.TestCase):
    def test01(self):
        self.assertEqual(fib.fibonacci(0), 0)

    def test02(self):
        self.assertEqual(fib.fibonacci(1), 1)

    def test03(self):
        self.assertEqual(fib.fibonacci(4), 3)


if __name__ == "__main__":
    unittest.main()
