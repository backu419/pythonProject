import unittest
def maa(a):
    a=[i for i in range(a)]
    return max(a)
class tes(unittest.TestCase):
    def test1(self):
        r=maa(10)
        self.assertEqual(r,9)