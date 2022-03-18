import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(100000)


    def test_balance_correct(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_sold_correct(self):
        self.assertEqual(self.kassapaate.maukkaat + self.kassapaate.edulliset, 0)

    def test_purchase_sale6(self):
        a = self.kassapaate.syo_edullisesti_kateisella(800)
        self.assertEqual((self.kassapaate.kassassa_rahaa, a, self.kassapaate.edulliset), (100240, 560, 1))

    def test_purchase_succulent_meal(self):
        a = self.kassapaate.syo_maukkaasti_kateisella(800)
        self.assertEqual((self.kassapaate.kassassa_rahaa, a, self.kassapaate.maukkaat), (100400, 400, 1))

    def test_purchase_succulent2(self):
        a = self.kassapaate.syo_maukkaasti_kateisella(0)
        self.assertEqual((self.kassapaate.kassassa_rahaa, a, self.kassapaate.maukkaat), (100000, 0, 0))

    def test_purchase_sale_insufficient(self):
        a = self.kassapaate.syo_edullisesti_kateisella(1)
        self.assertEqual((self.kassapaate.kassassa_rahaa, a, self.kassapaate.edulliset), (100000, 1, 0))

    def test_purchase_succulent_insufficient(self):
        a = self.kassapaate.syo_maukkaasti_kateisella(1)
        self.assertEqual((self.kassapaate.kassassa_rahaa, a, self.kassapaate.maukkaat), (100000, 1, 0))
        self.assertEqual(a, 1)


    def test_purchase_sale(self):
        a = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(a, True)
        self.assertEqual(self.maksukortti.saldo, 99760)

    def test_purchase_sale2(self):
        self.maksukortti = Maksukortti(0)
        a = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(a, False)
        self.assertEqual(self.maksukortti.saldo, 0)

    def test_purchase_succulent(self):
        a = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(a, True)
        self.assertEqual(self.maksukortti.saldo, 99600)


    def test_purchase_succulent_insufficient_card(self):
        self.maksukortti = Maksukortti(1)
        a = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(a, False)
        self.assertEqual(self.maksukortti.saldo, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)


    def test_purchase_sale_insufficient_card(self):
        self.maksukortti = Maksukortti(1)
        a = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(a, False)
        self.assertEqual(self.maksukortti.saldo, 1)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_charging_card(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100000)
        self.assertEqual(self.maksukortti.saldo, 200000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 200000)

    def test_charging_card2(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)
        self.assertEqual(self.maksukortti.saldo, 100000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)