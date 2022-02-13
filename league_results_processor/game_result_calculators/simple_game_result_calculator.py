from league_results_processor.dtos.game_result import game_result
from league_results_processor.enums.team_result import TeamResult
from league_results_processor.game_result_calculators.igame_result_calculator import IGameResultCalculator

class SimpleGameResultCalculator(IGameResultCalculator):
    """docstring for ClassName."""
    def __init__(self):
        super(SimpleGameResultCalculator, self).__init__()

    def determine_game_result(self, game_result: game_result):
        if game_result.teamA.goals_scored > game_result.teamB.goals_scored:
            game_result.teamA.team_result = TeamResult.WIN
            game_result.teamB.team_result = TeamResult.LOSE
        elif game_result.teamA.goals_scored < game_result.teamB.goals_scored:
            game_result.teamA.team_result = TeamResult.LOSE
            game_result.teamB.team_result = TeamResult.WIN
        else:
            game_result.teamA.team_result = TeamResult.DRAW
            game_result.teamB.team_result = TeamResult.DRAW
