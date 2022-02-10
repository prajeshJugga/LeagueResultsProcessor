from math import exp
import sys
import os
from typing import List
import unittest
from league_results_processor.dtos.game_result import game_result
from league_results_processor.dtos.team import Team
from league_results_processor.dtos.team_statistic import team_statistic
from league_results_processor.enums.team_result import team_result

from league_results_processor.file_objects.ifile_object import ifile_object
from league_results_processor.file_processors.simple_file_processor import simple_file_processor
from league_results_processor.file_readers.simple_file_reader import simple_file_reader

# Import the current working directory to import modules from an upper directory
# sys.path.append(os.path.join(os.getcwd()))

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

class simple_file_processor_tests(unittest.TestCase):
    """docstring for ClassName."""

    def test_successfully_process_a_small_set_of_file_lines(self):
        # Arrange
        input_file_lines: List[ifile_object] = self.get_input_lines_small_file()
        expected_results: List[game_result] = self.get_expected_small_results_set()
        file_processor = simple_file_processor()
        # Act
        game_results_list : List[game_result] = file_processor.process_file(input_file_objects=input_file_lines)
        # Assert
        self.assertEqual(len(expected_results), len(game_results_list))
        for index, value in enumerate(expected_results):
            self.assertEqual(value.teamA.team.name, game_results_list[index].teamA.team.name)

    def get_input_lines_small_file(self) -> List[ifile_object]:
        return [
            ifile_object("Lions 3, Snakes 3"),
            ifile_object("Tarantulas 1, FC Awesome 0"),
            ifile_object("Lions 1, FC Awesome 1"),
            ifile_object("Tarantulas 3, Snakes 1"),
            ifile_object("Lions 4, Grouches 0")
        ]

    def get_expected_small_results_set(self) -> List[game_result]:
        return [
            game_result(
                teamA=team_statistic(team=Team("Lions"), goals_scored=3, team_result=team_result.DRAW),
                teamB=team_statistic(team=Team("Snakes"), goals_scored=3, team_result=team_result.DRAW)
            ),
            game_result(
                teamA=team_statistic(team=Team("Tarantulas"), goals_scored=1, team_result=team_result.WIN),
                teamB=team_statistic(team=Team("FC Awesome"), goals_scored=0, team_result=team_result.LOSE)
            ),
            game_result(
                teamA=team_statistic(team=Team("Lions"), goals_scored=3, team_result=team_result.WIN),
                teamB=team_statistic(team=Team("FC Awesome"), goals_scored=1, team_result=team_result.LOSE)
            ),
            game_result(
                teamA=team_statistic(team=Team("Tarantulas"), goals_scored=1, team_result=team_result.DRAW),
                teamB=team_statistic(team=Team("Snakes"), goals_scored=1, team_result=team_result.DRAW)
            ),
            game_result(
                teamA=team_statistic(team=Team("Lions"), goals_scored=4, team_result=team_result.WIN),
                teamB=team_statistic(team=Team("Grouches"), goals_scored=0, team_result=team_result.LOSE)
            )
        ]


if __name__ == '__main__':
    unittest.main()
