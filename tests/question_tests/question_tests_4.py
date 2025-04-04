import unittest
from src.question_d.question_d import get_assessment_value, get_tax_assessed

class TestQuestionD(unittest.TestCase):
    def test_get_assessment_value(self):
        self.assertEqual(get_assessment_value(10000), 6000)
        self.assertEqual(get_assessment_value(20000), 12000)

    def test_get_tax_assessed(self):
        self.assertAlmostEqual(get_tax_assessed(6000), 43.20, places=2)
        self.assertAlmostEqual(get_tax_assessed(10000), 72.00, places=2)

if __name__ == '__main__':
    unittest.main()
