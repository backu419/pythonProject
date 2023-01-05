import unittest,cale as ca
print(ca.name)
print(ca.version)
print(ca.test_runner)
class my_test1(unittest.TestCase):
    def test_a(self):
        r=ca.login(username="Hcluser",password="1234")
        self.assertEqual(r,1)
    def test_b(self):
        r=ca.login(username="Hclur",password="123")
        self.assertEqual(r,0)