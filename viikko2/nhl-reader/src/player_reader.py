import requests
from player import Player


class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url, timeout=10).json()

    def get_nationalities(self):
        nationalities = []

        for player_dict in self.response:
            player = Player(player_dict)
            if player.nationality not in nationalities:
                nationalities.append(player.nationality)

        return nationalities

    def get_players(self):
        players = []

        for player_dict in self.response:
            player = Player(player_dict)
            players.append(player)

        return players
