# tests/test_app.py
import unittest
from app import greet


class TestApp(unittest.TestCase):
    def test_greet(self):
        expected = "Hello, World fromAhmad Abbas!"
        self.assertEqual(greet("World"), expected)


if __name__ == "__main__":
    unittest.main()
