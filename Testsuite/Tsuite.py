import unittest
from Test_Calcmode import my_test
def my_suite():
    suite=unittest.TestSuite()
    result=unittest.TestResult()
    suite.addTest(unittest.makeSuite(my_test))
    runner=unittest.TextTestRunner(verbosity=2)
    print(runner.run(suite))
my_suite()