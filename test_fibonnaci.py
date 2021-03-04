import fibonnaci
import unittest
import pytest

class TestClass(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fibonnaci.fibonnaci(10), 55)

    def test_factorial(self):
        self.assertEqual(fibonnaci.factorial(5), 120)

if __name__ == "__main__":
    unittest.main()

def test_fibonnaci():
    x = fibonnaci.fibonnaci(10)
    assert x == 55, "test failed"

def test_factorial():
    x = fibonnaci.factorial(5)
    assert x == 120, "test failed"
