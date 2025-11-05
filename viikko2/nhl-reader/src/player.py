class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.teams = dict['team']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.points = self.goals+self.assists

    def __str__(self):
        return f"{self.name:20} team {self.teams:15} {str(self.goals)} + {str(self.assists)} = {str(self.points)}"
