from abc import ABC, abstractmethod
from pelilogiikka.tuomari import Tuomari

class KiviPaperiSakset(ABC):
    def pelaa(self):
        # keep tuomari on the instance so tests can inspect it
        self.tuomari = Tuomari()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self.tuomari)

            # stop when someone reaches 5 points
            if self.tuomari.onko_loppu(5):
                break

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        print("Kiitos!")
        print(self.tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    @abstractmethod
    def _toisen_siirto(self, ensimmaisen_siirto):
        pass

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"