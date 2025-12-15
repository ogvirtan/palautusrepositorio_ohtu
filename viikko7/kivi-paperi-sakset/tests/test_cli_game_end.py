from pelimuodot.kps import KiviPaperiSakset


class DummyGame(KiviPaperiSakset):
    def __init__(self, first_moves, second_moves):
        self.first_moves = list(first_moves)
        self.second_moves = list(second_moves)
        self._idx = 0

    def _ensimmaisen_siirto(self):
        if self._idx < len(self.first_moves):
            val = self.first_moves[self._idx]
            return val
        return "x"  # invalid to stop

    def _toisen_siirto(self, ensimmaisen_siirto):
        if self._idx < len(self.second_moves):
            val = self.second_moves[self._idx]
            self._idx += 1
            return val
        return "x"


def test_cli_game_ends_when_player_reaches_five():
    # first player will win each round (k beats s), five rounds
    first = ["k"] * 10
    second = ["s"] * 10

    g = DummyGame(first, second)
    g.pelaa()

    # after play, the instance should have a tuomari and it should report a winner
    assert hasattr(g, "tuomari")
    assert g.tuomari.onko_loppu(5)
    assert g.tuomari.voittaja(5) == 1
