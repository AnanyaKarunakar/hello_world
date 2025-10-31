import unittest
from hello-world import get_message

class TestApp(unittest.TestCase):
    def test_get_message(self):
        self.assertEqual(get_message(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
