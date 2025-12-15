from pelimuodot.kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from pelimuodot.kps_tekoaly import KPSTekoaly
from pelimuodot.kps_parempi_tekoaly import KPSParempiTekoaly

class Pelimuoto:
    def luo_peli(self, tyyppi):
        if tyyppi == 'a':
            return KPSPelaajaVsPelaaja()
        if tyyppi == 'b':
            return KPSTekoaly()
        if tyyppi == 'c':
            return KPSParempiTekoaly()

        return None