from tekoaly.tekoaly_parannettu import TekoalyParannettu


def test_memory_and_behavior():
    t = TekoalyParannettu(3)
    assert t._vapaa_muisti_indeksi == 0
    t.aseta_siirto('k')
    assert t._vapaa_muisti_indeksi == 1
    t.aseta_siirto('p')
    assert t._vapaa_muisti_indeksi == 2
    # now enough history for decision logic
    t.aseta_siirto('k')
    assert t._vapaa_muisti_indeksi == 3
    # internal memory should contain the last three moves
    assert t._muisti[0] in ('k','p','s')
    assert t._muisti[1] in ('k','p','s')
    assert t._muisti[2] in ('k','p','s')
    # calling anna_siirto should return one of the valid moves
    out = t.anna_siirto()
    assert out in ('k','p','s')
