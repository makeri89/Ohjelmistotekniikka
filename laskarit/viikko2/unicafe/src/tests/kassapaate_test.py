import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        
    def test_rahamaara_ja_lounaiden_maara_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_kateismaksu_edullisesti_onnistuu(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(maksu,60)
        self.assertEqual(self.kassapaate.edulliset, 1)
        
    def test_kateismaksu_edullisesti_epaonnistuu(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(maksu,200)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kateismaksu_maukkaasti_onnistuu(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(maksu,0)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        
    def test_kateismaksu_maukkaasti_onnistuu_isommalla_summalla(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(40000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(maksu,39600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        
    def test_kateismaksu_maukkaasti_epaonnistuu(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(maksu,300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_lounaiden_maara_kasvaa_oikein_usealla_veloituksella(self):
        for _ in range(10):
            self.kassapaate.syo_maukkaasti_kateisella(400)
            self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset,10)
        self.assertEqual(self.kassapaate.maukkaat, 10)
        
    def test_lounaiden_maara_ei_kasva_usealla_epaonnistuneella_veloituksella(self):
        for _ in range(10):
            self.kassapaate.syo_maukkaasti_kateisella(300)
            self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
    def test_korttimaksu_edullisesti_toimii(self):
        maksu = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(str(self.maksukortti), 'saldo: 7.6')
        self.assertEqual(maksu, True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_korttimaksu_edullisesti_epaonnistuu(self):
        self.maksukortti.ota_rahaa(800)
        maksu = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(str(self.maksukortti), 'saldo: 2.0')
        self.assertEqual(maksu, False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_korttimaksu_maukkaasti_toimii(self):
        maksu = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(str(self.maksukortti), 'saldo: 6.0')
        self.assertEqual(maksu, True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_korttimaksu_maukkaasti_epaonnistuu(self):
        self.maksukortti.ota_rahaa(800)
        maksu = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(str(self.maksukortti), 'saldo: 2.0')
        self.assertEqual(maksu, False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_kortille_rahan_lataus_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)
        self.assertEqual(str(self.maksukortti), 'saldo: 15.0')
        
    def test_kortilla_rahan_lataus_ei_onnistu_negatiivisella_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.maksukortti), 'saldo: 10.0')