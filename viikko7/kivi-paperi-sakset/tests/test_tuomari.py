from pelilogiikka.tuomari import Tuomari


def test_initial_scores():
    t = Tuomari()
    assert t.ekan_pisteet == 0
    assert t.tokan_pisteet == 0
    assert t.tasapelit == 0


def test_tuomari_counts_tie():
    t = Tuomari()
    t.kirjaa_siirto('k', 'k')
    assert t.tasapelit == 1
    assert t.ekan_pisteet == 0
    assert t.tokan_pisteet == 0


def test_tuomari_counts_first_win():
    t = Tuomari()
    t.kirjaa_siirto('k', 's')
    assert t.ekan_pisteet == 1
    assert t.tokan_pisteet == 0
    assert t.tasapelit == 0


def test_tuomari_counts_second_win():
    t = Tuomari()
    t.kirjaa_siirto('p', 's')
    assert t.ekan_pisteet == 0
    assert t.tokan_pisteet == 1
    assert t.tasapelit == 0


def test_tuomari_game_ends_at_five():
    t = Tuomari()
    # give first player 5 wins
    for _ in range(5):
        t.kirjaa_siirto('k', 's')

    assert t.onko_loppu(5)
    assert t.voittaja(5) == 1

    # second player reaches 5
    t2 = Tuomari()
    for _ in range(5):
        t2.kirjaa_siirto('s', 'k')

    assert t2.onko_loppu(5)
    assert t2.voittaja(5) == 2
