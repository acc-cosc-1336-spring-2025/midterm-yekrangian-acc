import unittest
from src.question_a.question_a import get_random_number

class TestQuestionA(unittest.TestCase):
    def test_get_random_number_range(self):
        for _ in range(1000):  # Test many times to check bounds
            result = get_random_number()
            self.assertIn(result, range(1, 6), f"Number {result} is out of range!")

if __name__ == '__main__': 
    unittest.main()
