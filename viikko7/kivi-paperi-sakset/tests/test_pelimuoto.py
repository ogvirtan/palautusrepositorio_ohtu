from pelilogiikka.pelimuoto import Pelimuoto
from pelimuodot.kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from pelimuodot.kps_tekoaly import KPSTekoaly
from pelimuodot.kps_parempi_tekoaly import KPSParempiTekoaly


def test_luo_peli_returns_correct_instances():
    p = Pelimuoto()
    assert isinstance(p.luo_peli('a'), KPSPelaajaVsPelaaja)
    assert isinstance(p.luo_peli('b'), KPSTekoaly)
    assert isinstance(p.luo_peli('c'), KPSParempiTekoaly)
    assert p.luo_peli('x') is None


def test_onko_ok_siirto():
    p = Pelimuoto()
    peli = p.luo_peli('a')
    # protected method call on concrete instance
    assert peli._onko_ok_siirto('k')
    assert not peli._onko_ok_siirto('x')
