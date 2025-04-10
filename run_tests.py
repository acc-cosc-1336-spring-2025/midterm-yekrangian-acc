#DON'T MAKE CHANGES TO THIS FILE

#write tests for all the questions here

import unittest

from tests.question_tests import question_tests_2

suite = unittest.TestLoader().loadTestsFromModule(question_tests_2)
unittest.TextTestRunner(verbosity=2).run(suite) 
