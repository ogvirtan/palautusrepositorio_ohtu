from tekoaly.tekoaly import Tekoaly


def test_tekoaly_cycles():
    t = Tekoaly()
    assert t.anna_siirto() == "p"
    assert t.anna_siirto() == "s"
    assert t.anna_siirto() == "k"
    # cycles again
    assert t.anna_siirto() == "p"
