from tokenize import Double
from league_results_processor.dtos.league_table_row import LeagueTableRow
from league_results_processor.dtos.team import Team

class SimpleLeagueTableRow(LeagueTableRow):
    """docstring for ClassName."""
    def __init__(self, team: Team, points: Double, games_played: int, league_position: int):
        self.team = team
        self.points = points
        self.games_played = games_played
        self.league_position = league_position
