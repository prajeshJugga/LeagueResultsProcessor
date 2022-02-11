from typing import List
from league_results_processor.dtos.game_result import game_result

class IGameResultCalculator:
    """docstring for ClassName."""
    def __init__(self):
        super(IGameResultCalculator, self).__init__()

    def determine_game_result(self, game_result: game_result):
        pass
