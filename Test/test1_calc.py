import unittest, calc
class Test_Calc(unittest.TestCase):
    def test(self):
        r=calc.add(10,5)
        self.assertEqual(r,15)
    def test1(self):
        r=calc.add(-2,-5)
        self.assertEqual(r,-7)

