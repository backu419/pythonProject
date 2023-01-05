import unittest
def mul(a, b):
    return a*b
#5 test cases for this function
class my_Test(unittest.TestCase):
    def test(self):
        r=mul(10, 5)
        self.assertEqual(r, 50)
    def test1(self):
        r=mul(2, 5)
        self.assertEqual(r, 10)
    def test2(self):
        r=mul(10, 5)
        self.assertEqual(r, 50)
    def test3(self):
        r=mul(4, 5)
        self.assertEqual(r, 20)
    def test4(self):
        r=mul(10, 50)
        self.assertEqual(r, 500)

