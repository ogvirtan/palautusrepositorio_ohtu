class Player:# pylint: disable=too-few-public-methods
    def __init__(self, sk):
        self.name = sk["name"]
        self.nationality = sk["nationality"]
        self.teams = sk["team"]
        self.assists = sk["assists"]
        self.goals = sk["goals"]
        self.points = self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} team {self.teams:15} {str(self.goals)} + {str(self.assists)} = {str(self.points)}"
