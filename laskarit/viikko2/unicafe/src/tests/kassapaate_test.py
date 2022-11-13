import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti_rikas = Maksukortti(10000)
        self.maksukortti_koyha = Maksukortti(200)

    def test_alussa_rahaa_oikean_verran(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_alussa_maukkaita_myyty_nolla(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_alussa_edullisia_myyty_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_maukkaasti_lisaa_kassaan_jos_onnistuu(self):
        self.kassapaate.syo_maukkaasti_kateisella(600)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisosto_maukkaasti_palauttaa_oikean_verran_jos_onnistuu(self):
        palautus = self.kassapaate.syo_maukkaasti_kateisella(600)
        self.assertEqual(palautus, 200)

    def test_maukkaiden_maara_kasvaa_onnistuneella_kateisostolla(self):
        self.kassapaate.syo_maukkaasti_kateisella(600)
        self.assertEqual(self.kassapaate.maukkaat, 1)       

    def test_kateisosto_maukkaasti_ei_lisaa_kassaan_jos_epaonnistuu(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)  
    
    def test_kateisosto_maukkaasti_palauttaa_kaiken_jos_epaonnistuu(self):
        palautus = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(palautus, 200)

    def test_maukkaiden_maara_ei_kasva_epaonnistuneella_kateisostolla(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)     

    def test_kateisosto_edullisesti_lisaa_kassaan_jos_onnistuu(self):
        self.kassapaate.syo_edullisesti_kateisella(600)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisosto_edullisesti_palauttaa_oikean_verran_jos_onnistuu(self):
        palautus = self.kassapaate.syo_edullisesti_kateisella(600)
        self.assertEqual(palautus, 360)

    def test_edullisten_maara_kasvaa_onnistuneella_kateisostolla(self):
        self.kassapaate.syo_edullisesti_kateisella(600)
        self.assertEqual(self.kassapaate.edulliset, 1)       

    def test_kateisosto_edullisesti_ei_lisaa_kassaan_jos_epaonnistuu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)  
    
    def test_kateisosto_edullisesti_palauttaa_kaiken_jos_onnistuu(self):
        palautus = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(palautus, 200)

    def test_edullisten_maara_ei_kasva_epaonnistuneella_kateisostolla(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_lataus_kortille_lisaa_kassapaatteen_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti_rikas, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_negatiivinen_lataus_kortille_ei_lisaa_kassapaatteen_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti_rikas, -500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_negatiivinen_lataus_kortille_ei_lisaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti_rikas, -500)
        self.assertEqual(self.maksukortti_rikas.saldo, 10000)

    def test_lataus_kortille_lisaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti_rikas, 500)
        self.assertEqual(self.maksukortti_rikas.saldo, 10500)

    def test_maukkaat_onnistunut_korttiosto_palauttaa_true(self):
        palaute = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_rikas)
        self.assertEqual(palaute, True)

    def test_maukkaat_onnistunut_korttiosto_vahentaa_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_rikas)
        self.assertEqual(self.maksukortti_rikas.saldo, 9600)

    def test_maukkaat_onnistunut_korttiosto_lisaa_aterian(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_rikas)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaat_onnistunut_korttiosto_ei_lisaa_rahaa_kassaan(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_rikas)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaat_epaonnistunut_korttiosto_palauttaa_false(self):
        palaute = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_koyha)
        self.assertEqual(palaute, False)

    def test_maukkaat_epaonnistunut_korttiosto_ei_vahenna_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_koyha)
        self.assertEqual(self.maksukortti_koyha.saldo, 200)

    def test_maukkaat_epaonnistunut_korttiosto_ei_lisaa_ateriaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_koyha)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edulliset_onnistunut_korttiosto_palauttaa_true(self):
        palaute = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_rikas)
        self.assertEqual(palaute, True)

    def test_edulliset_onnistunut_korttiosto_vahentaa_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_rikas)
        self.assertEqual(self.maksukortti_rikas.saldo, 9760)

    def test_edulliset_onnistunut_korttiosto_lisaa_aterian(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_rikas)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edulliset_onnistunut_korttiosto_ei_lisaa_rahaa_kassaan(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_rikas)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_epaonnistunut_korttiosto_palauttaa_false(self):
        palaute = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_koyha)
        self.assertEqual(palaute, False)

    def test_edulliset_epaonnistunut_korttiosto_ei_vahenna_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_koyha)
        self.assertEqual(self.maksukortti_koyha.saldo, 200)

    def test_edulliset_epaonnistunut_korttiosto_ei_lisaa_ateriaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_koyha)
        self.assertEqual(self.kassapaate.edulliset, 0)