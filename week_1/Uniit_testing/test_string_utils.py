import unittest

def to_uppercase(s):
    return s.upper()

def string_length(s):
    return len(s)

class TestStringUtils(unittest.TestCase):
    def test_uppercase(self):
        self.assertEqual(to_uppercase("hello"), "HELLO")

    def test_length(self):
        self.assertEqual(string_length("python"), 6)

    def test_empty_string(self):
        self.assertEqual(string_length(""), 0)

if __name__ == "__main__":
    unittest.main()
