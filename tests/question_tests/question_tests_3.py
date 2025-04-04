import unittest
from src.question_c.question_c import reverse_string

class TestQuestionC(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")  # Edge case: empty string

if __name__ == '__main__':
    unittest.main()
