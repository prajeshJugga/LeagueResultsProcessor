from math import exp
import sys
import os
from typing import List
import unittest
from league_results_processor.dtos.game_result import game_result
from league_results_processor.dtos.team import Team
from league_results_processor.dtos.team_statistic import team_statistic
from league_results_processor.enums.team_result import team_result
from league_results_processor.exceptions.invalid_game_line_exception import InvalidGameLineException

from league_results_processor.file_objects.ifile_object import ifile_object
from league_results_processor.file_processors.simple_file_processor import simple_file_processor
from league_results_processor.file_readers.simple_file_reader import simple_file_reader
from league_results_processor.game_result_calculators.igame_result_calculator import IGameResultCalculator
from league_results_processor.game_result_calculators.simple_game_result_calculator import SimpleGameResultCalculator

# Import the current working directory to import modules from an upper directory
# sys.path.append(os.path.join(os.getcwd()))

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

class simple_game_results_calculator_tests(unittest.TestCase):
    """docstring for ClassName."""

    def correctly_determines_result(self, simple_game_calculator: IGameResultCalculator, input_game_result: game_result, expected_game_result: game_result):
        # Arrange
        # simple_game_calculator = SimpleGameResultCalculator()
        # input_game_result = game_result(
        #     teamA=team_statistic(team=Team("Lions"), goals_scored=3, team_result=team_result.NOT_CALCULATED),
        #     teamB=team_statistic(team=Team("Snakes"), goals_scored=3, team_result=team_result.NOT_CALCULATED)
        # )
        # expected_draw_game_result = game_result(
        #     teamA=team_statistic(team=Team("Lions"), goals_scored=3, team_result=team_result.DRAW),
        #     teamB=team_statistic(team=Team("Snakes"), goals_scored=3, team_result=team_result.DRAW)
        # )
        # Act
        simple_game_calculator.determine_game_result(input_game_result)
        # Assert
        self.assertEqual(expected_game_result.teamA.team.name, input_game_result.teamA.team.name)
        self.assertEqual(expected_game_result.teamB.team.name, input_game_result.teamB.team.name)
        self.assertEqual(expected_game_result.teamA.goals_scored, input_game_result.teamA.goals_scored)
        self.assertEqual(expected_game_result.teamB.goals_scored, input_game_result.teamB.goals_scored)
        self.assertEqual(expected_game_result.teamA.team_result, input_game_result.teamA.team_result)
        self.assertEqual(expected_game_result.teamB.team_result, input_game_result.teamB.team_result)

    def test_correctly_determines_draw_result(self):
        # Arrange
        simple_game_calculator = SimpleGameResultCalculator()
        input_game_result = game_result(
            teamA=team_statistic(team=Team("Lions"), goals_scored=3, team_result=team_result.NOT_CALCULATED),
            teamB=team_statistic(team=Team("Snakes"), goals_scored=3, team_result=team_result.NOT_CALCULATED)
        )
        expected_draw_game_result = game_result(
            teamA=team_statistic(team=Team("Lions"), goals_scored=3, team_result=team_result.DRAW),
            teamB=team_statistic(team=Team("Snakes"), goals_scored=3, team_result=team_result.DRAW)
        )
        # Act and Assert
        self.correctly_determines_result(simple_game_calculator=simple_game_calculator, input_game_result=input_game_result, expected_game_result=expected_draw_game_result)

    def test_correctly_determines_win_result(self):
        # Arrange
        simple_game_calculator = SimpleGameResultCalculator()
        input_game_result = game_result(
            teamA=team_statistic(team=Team("Lions"), goals_scored=1, team_result=team_result.NOT_CALCULATED),
            teamB=team_statistic(team=Team("Snakes"), goals_scored=0, team_result=team_result.NOT_CALCULATED)
        )
        expected_draw_game_result = game_result(
            teamA=team_statistic(team=Team("Lions"), goals_scored=1, team_result=team_result.WIN),
            teamB=team_statistic(team=Team("Snakes"), goals_scored=0, team_result=team_result.LOSE)
        )
        # Act and Assert
        self.correctly_determines_result(simple_game_calculator=simple_game_calculator, input_game_result=input_game_result, expected_game_result=expected_draw_game_result)

    def test_correctly_determines_loss_result(self):
        # Arrange
        simple_game_calculator = SimpleGameResultCalculator()
        input_game_result = game_result(
            teamA=team_statistic(team=Team("Lions"), goals_scored=0, team_result=team_result.NOT_CALCULATED),
            teamB=team_statistic(team=Team("Snakes"), goals_scored=1, team_result=team_result.NOT_CALCULATED)
        )
        expected_draw_game_result = game_result(
            teamA=team_statistic(team=Team("Lions"), goals_scored=0, team_result=team_result.LOSE),
            teamB=team_statistic(team=Team("Snakes"), goals_scored=1, team_result=team_result.WIN)
        )
        # Act and Assert
        self.correctly_determines_result(simple_game_calculator=simple_game_calculator, input_game_result=input_game_result, expected_game_result=expected_draw_game_result)


if __name__ == '__main__':
    unittest.main()
