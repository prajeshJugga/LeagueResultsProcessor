from typing import List
from league_results_processor.dtos.game_result import game_result
from league_results_processor.dtos.team import Team
from league_results_processor.dtos.team_statistic import team_statistic
from league_results_processor.enums.team_result import TeamResult
from league_results_processor.exceptions.invalid_game_line_exception import InvalidGameLineException
from league_results_processor.file_objects.ifile_object import ifile_object
from league_results_processor.file_objects.simple_game_results_line import simple_game_results_line
from league_results_processor.file_processors.ifile_processor import ifile_processor
from league_results_processor.game_result_calculators.igame_result_calculator import IGameResultCalculator
from league_results_processor.game_result_calculators.simple_game_result_calculator import SimpleGameResultCalculator

class simple_file_processor(ifile_processor):
    """docstring for ClassName."""
    # def __init__(self):
    #     super(simple_file_processor, self).__init__()
        #self.game_result_calculator = game_result_calculator

    def process_file(self, input_file_objects: List[simple_game_results_line]) -> List[game_result]:
        game_results = []
        for value in input_file_objects:
            team_result_lines = self.__get_team_result_strings(value)
            game_result_obj = game_result(
                teamA = self.__get_team_result(team_result_line=team_result_lines[0]),
                teamB = self.__get_team_result(team_result_line=team_result_lines[-1])
            )
            self.game_result_calculator.determine_game_result(game_result=game_result_obj)
            game_results.append(game_result_obj)
        return game_results

    def __get_team_result_strings(self, game_result: simple_game_results_line) -> List[str]:
        team_result_strings : List(str) = game_result.file_line.split(',')
        for value in team_result_strings:
            value = value.strip()
        return team_result_strings
        # return list((lambda x:x.strip(), team_result_strings))

    def __get_team_name(self, team_result_string: str) -> str:
        return team_result_string[0:len(team_result_string) - 1].strip()

    def __get_goals_scored(self, team_result_string: str) -> int:
        goal_string = team_result_string[-1]
        if goal_string.isdigit():
            return int(goal_string)
        raise InvalidGameLineException("This result contains an invalid score.")

    def __get_team_result(self, team_result_line: str) -> team_statistic:
        return team_statistic(
            team=Team(self.__get_team_name(team_result_string=team_result_line)),
            goals_scored=self.__get_goals_scored(team_result_string=team_result_line),
            team_result=TeamResult.NOT_CALCULATED
        )
