import unittest, calc
class Test_Calc(unittest.TestCase):
    def test(self):
        r=calc.add(10,5)
        self.assertEqual(r,15)
    def test1(self):
        r=calc.add(-2,-5)
        self.assertEqual(r,-7)
    def test2(self):
        r=calc.sub(2,5)
        self.assertEqual(r,- 3)
    def test3(self):
        r=calc.sub(5,2)
        self.assertEqual(r,3)
