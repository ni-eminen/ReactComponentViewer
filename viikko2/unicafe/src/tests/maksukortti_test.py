import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_balance_correct(self):
        self.assertEqual(str(self.maksukortti), 'saldo: 0.1')

    def test_balance_increase(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), 'saldo: 0.2')

    def test_balance_decreases_correctly_with_sufficient_funds(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), 'saldo: 0.05')

    def test_balance_unaffected_insufficient_funds(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(str(self.maksukortti), 'saldo: 0.1')

    def test_returns_true_sufficient_funds_otherwise_false(self):
        a = self.maksukortti.ota_rahaa(1)
        b = self.maksukortti.ota_rahaa(200)
        self.assertEqual(True, (a == True and b == False))