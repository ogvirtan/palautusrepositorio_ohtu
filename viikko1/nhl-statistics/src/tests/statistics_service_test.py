import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_palvelu_on_olemassa(self):
        self.assertNotEqual(self.stats, None)

    def test_palvelulla_on_lukija(self):
        self.assertNotEqual(self.stats.reader, None)

    def test_uudella_palvelulla_oikea_maara_pelaajia(self):
        self.assertEqual(len(self.stats._players), 5)
    
    def test_search_toimii_jos_haettava_olemassa(self):
        self.assertAlmostEqual(self.stats.search("Gretzky"), self.stats._players[-1])

    def test_search_toimii_jos_haettava_ei_ole_olemassa(self):
        self.assertEqual(self.stats.search("Selanne"), None)
    
    def test_team_toimii_jos_haettava_olemassa(self):
        self.assertAlmostEqual(self.stats.team("EDM"), [pelaaja for pelaaja in self.stats._players if pelaaja.team == "EDM"])

    def test_team_toimii_jos_haettava_ei_ole_olemassa(self):
        self.assertEqual(self.stats.search("DAL"), None)

    def test_top_palauttaa_vain_parhaan_pelaajan_syotteella_0(self):
        self.assertEqual(len(self.stats.top(0)), 1)

    def test_top_jarjestaa_listan_oikein(self):
        pelaajat = self.stats.top(2)
        self.assertAlmostEqual([pelaaja.name for pelaaja in pelaajat], ["Gretzky", "Lemieux", "Yzerman"])

