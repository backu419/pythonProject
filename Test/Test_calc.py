import unittest, calc
class Test_Calc(unittest.TestCase):
    def Test(self):
        self.assertEqual(calc.add(10,5),15)
