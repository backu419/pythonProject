import unittest
from Test_cale import my_test
from T_case import my_test1
def my_suite():
    suite=unittest.TestSuite()
    result=unittest.TestResult()
    suite.addTest(unittest.makeSuite(my_test))
    suite.addTest(unittest.makeSuite(my_test1))
    runner=unittest.TextTestRunner(verbosity=2)
    print(runner.run(suite))
my_suite()