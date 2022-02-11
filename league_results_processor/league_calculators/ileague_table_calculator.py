from typing import List
from league_results_processor.dtos.game_points import GamePoints
from league_results_processor.dtos.game_result import game_result
from league_results_processor.dtos.league_table_row import LeagueTableRow


class ILeagueTableCalculator:
    """docstring for ClassName."""

    def __init__(self, game_points: GamePoints):
        self.game_points = game_points

    def get_league_table(self, game_results_list: List[game_result]) -> List[LeagueTableRow]:
        pass
