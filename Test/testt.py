import unittest
def sum(a, b):
    return (a+b)
class My_test(unittest.TestCase):
    def test(self):
        a=10
        b=20
        r=sum(a, b)
        self.assertEqual(r, 30)
    def test1(self):
        a=10
        b=20
        r=sum(a, b)
        self.assertEqual(r, 30)