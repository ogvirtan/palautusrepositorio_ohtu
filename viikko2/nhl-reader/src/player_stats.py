from player import Player
from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
    
    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        filtered_players = filter(lambda p: p.nationality==nationality , players)
        return sorted(filtered_players, key=lambda p: p.points, reverse=True)