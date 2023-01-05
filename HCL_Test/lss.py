import unittest
def li(a):
    a=[i for i in range(a)]
    return a.reverse()
class tes(unittest.TestCase):
    def test0(self):
        r=li(9)
        h=[8,7,6,5,4,3,2,1,0]
        self.assertEqual(r, h)
