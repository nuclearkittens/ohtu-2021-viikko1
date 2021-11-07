import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    # lisätyt testit alla
    def test_negatiivinen_tilavuus(self):
        self.varasto = Varasto(-2)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_negatiivinen_saldo(self):
        self.varasto = Varasto(3, -2)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_saldo_suurempi_kuin_tilavuus(self):
        self.varasto = Varasto(3, 6)
        self.assertAlmostEqual(self.varasto.tilavuus, self.varasto.saldo)

    def test_lisaa_negatiivinen(self):
        alkusaldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-2)
        self.assertAlmostEqual(self.varasto.saldo, alkusaldo)

    def test_lisaa_liikaa(self):
        lisattava = self.varasto.paljonko_mahtuu() + 1
        self.varasto.lisaa_varastoon(lisattava)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ota_negatiivinen(self):
        otettu = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(otettu, 0)

    def test_ota_liikaa_palauttaa_kaikki(self):
        alkusaldo = self.varasto.saldo
        otettava = alkusaldo + 1
        otettu = self.varasto.ota_varastosta(otettava)
        self.assertAlmostEqual(otettu, alkusaldo)

    def test_ota_liikaa_nollaa(self):
        self.varasto.ota_varastosta(self.varasto.saldo+1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str_palauttaa_merkkijonon(self):
        oletettu = f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}"
        self.assertEqual(str(self.varasto), oletettu)
