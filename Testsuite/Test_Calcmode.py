import Calcmode as cm, unittest

print(cm.name)
print(cm.version)
print(cm.test_runner)
class my_test(unittest.TestCase):
    def test0(self):
        r=cm.add_int(10,20)
        self.assertEqual(r, 30)
    def test1(self):
        r=cm.sub(20,10)
        self.assertEqual(r, 10)
    def test2(self):
        r=cm.mul(10,5)
        self.assertEqual(r, 50)
    def test3(self):
        r=cm.mul(5,4)
        self.assertEqual(r, 20)
    def test4(self):
        r=cm.div(10,3)
        self.assertEqual(r,3)

if '__name__' == '__main__':
    unittest.main()