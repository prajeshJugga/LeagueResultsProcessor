from tokenize import Double
from league_results_processor.dtos.team import Team


class LeagueTableRow(object):
    """docstring for ClassName."""
    def __init__(self, team: Team, points: Double, games_played: int, league_position: int):
        self.team = team
        self.points = points
        self.games_played = games_played
        self.league_position = league_position

    def __init__(self):
        pass

    @property
    def team(self) -> Team:
        return self._team

    @team.setter
    def team(self, value):
        self._team = value

    @property
    def points(self) -> Double:
        return self._points

    @points.setter
    def points(self, value):
        self._points = value

    @property
    def games_played(self) -> int:
        return self._games_played

    @games_played.setter
    def games_played(self, value):
        self._games_played = value

    @property
    def league_position(self) -> int:
        return self._league_position

    @league_position.setter
    def league_position(self, value):
        self._league_position = value
