import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_alkusaldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataus_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.00 euroa")

    def test_ota_rahaa_vahentaa_saldoa_oikein(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_ota_rahaa_ei_toimi_jos_ei_tarpeeksi_saldoa(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_ota_rahaa_palauttaa_true_jos_tarpeeksi_rahaa(self):
        palaute = self.maksukortti.ota_rahaa(500)
        self.assertEqual(palaute, True)

    def test_ota_rahaa_palauttaa_false_jos_ei_tarpeeksi_rahaa(self):
        palaute = self.maksukortti.ota_rahaa(1500)
        self.assertEqual(palaute, False)
