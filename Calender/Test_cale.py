import unittest,cale as ca
print(ca.name)
print(ca.version)
print(ca.test_runner)
class my_test(unittest.TestCase):
    def test0(self):
        r=ca.months(2,2022)
        self.assertEqual(r,28)
    def test1(self):
        r=ca.months(2,2020)
        self.assertEqual(r,29)
    def test2(self):
        r=ca.months(1,2020)
        self.assertEqual(r,31)

    def test3(self):
        r=ca.months(3,2020)
        self.assertEqual(r,31)


    def test4(self):
        r=ca.months(4,2020)
        self.assertEqual(r,30)


    def test5(self):
        r=ca.months(5,2020)
        self.assertEqual(r,31)
    def test6(self):
        r=ca.months(6,2020)
        self.assertEqual(r,30)

    def test7(self):
        r=ca.months(7,2020)
        self.assertEqual(r,31)
    def test8(self):
        r=ca.months(8,2020)
        self.assertEqual(r,31)

    def test9(self):
        r=ca.months(9,2020)
        self.assertEqual(r,30)
    def test10(self):
        r=ca.months(10,2020)
        self.assertEqual(r,31)

    def test11(self):
        r=ca.months(11,2020)
        self.assertEqual(r,30)
    def test12(self):
        r=ca.months(12,2020)
        self.assertEqual(r,31)


    def test13(self):

        r=ca.months(4,2020)
        self.assertEqual(r,30)
    def test14(self):
        r=ca.login(username="Hcluser",password="1234")
        self.assertEqual(r,1)
