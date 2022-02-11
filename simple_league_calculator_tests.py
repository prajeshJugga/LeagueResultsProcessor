import os
import sys
from typing import List
import unittest
from league_results_processor.dtos.game_points import GamePoints

from league_results_processor.dtos.game_result import game_result
from league_results_processor.dtos.simple_league_table_row import SimpleLeagueTableRow
from league_results_processor.dtos.team import Team
from league_results_processor.dtos.team_statistic import team_statistic
from league_results_processor.enums.team_result import TeamResult
from league_results_processor.league_calculators.ileague_table_calculator import ILeagueTableCalculator
from league_results_processor.league_calculators.simple_league_table_calculator import SimpleLeagueTableCalculator


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

class simple_file_processor_tests(unittest.TestCase):
    """docstring for ClassName."""
# Calculate_League_Table(List<GameResultDTO> inputGameDetails, List<SimpleLeagueTableRowDTO> expectedLeagueTable, ILeagueTableCalculator<GameResultDTO, SimpleLeagueTableRowDTO> simpleLeagueTableCalculator)

    def calculate_league_table(self, game_results: List[game_result], expected_league_table: List[SimpleLeagueTableRow], league_calculator: ILeagueTableCalculator):
        # Arrange
        # Act
        actual_league_table: List[SimpleLeagueTableRow] = league_calculator.get_league_table(game_results)
        # Assert
        self.assertEqual(len(expected_league_table), len(actual_league_table))
        for index, value in enumerate(expected_league_table):
            self.assertEqual(value.team.name, actual_league_table[index].team.name)
            self.assertEqual(value.points, actual_league_table[index].points)
            self.assertEqual(value.league_position, actual_league_table[index].league_position)

    def test_calculates_correct_positions_for_teams_with_different_points(self):
        # Arrange
        game_results = self.get_different_game_results()
        game_points = GamePoints(3, 1, 0)
        league_calculator = SimpleLeagueTableCalculator(game_points)
        # Act and Assert
        self.calculate_league_table(game_results=game_results, expected_league_table=self.get_expected_league_table_for_different_results(), league_calculator=league_calculator)

    def test_calculates_correct_positions_for_teams_with_the_same_points(self):
        # Arrange
        game_results = self.get_game_results_where_teams_have_same_points()
        game_points = GamePoints(3, 1, 0)
        league_calculator = SimpleLeagueTableCalculator(game_points)
        # Act and Assert
        self.calculate_league_table(game_results=game_results, expected_league_table=self.get_expected_league_table_for_teams_that_have_same_points(), league_calculator=league_calculator)


    def get_different_game_results(self) -> List[game_result]:
        return [
            game_result(
                teamA=team_statistic(team=Team("Lions"), goals_scored=3, team_result=TeamResult.DRAW),
                teamB=team_statistic(team=Team("Snakes"), goals_scored=3, team_result=TeamResult.DRAW)
            ),
            game_result(
                teamA=team_statistic(team=Team("Tarantulas"), goals_scored=1, team_result=TeamResult.WIN),
                teamB=team_statistic(team=Team("FC Awesome"), goals_scored=0, team_result=TeamResult.LOSE)
            ),
            game_result(
                teamA=team_statistic(team=Team("Lions"), goals_scored=1, team_result=TeamResult.DRAW),
                teamB=team_statistic(team=Team("FC Awesome"), goals_scored=1, team_result=TeamResult.DRAW)
            ),
            game_result(
                teamA=team_statistic(team=Team("Tarantulas"), goals_scored=3, team_result=TeamResult.WIN),
                teamB=team_statistic(team=Team("Snakes"), goals_scored=1, team_result=TeamResult.LOSE)
            ),
            game_result(
                teamA=team_statistic(team=Team("Lions"), goals_scored=4, team_result=TeamResult.WIN),
                teamB=team_statistic(team=Team("Grouches"), goals_scored=0, team_result=TeamResult.LOSE)
            )
        ]

    def get_expected_league_table_for_different_results(self) -> List[SimpleLeagueTableRow]:
        return [
            SimpleLeagueTableRow(Team("Tarantulas"), points=6, games_played=2, league_position=1),
            SimpleLeagueTableRow(Team("Lions"), points=5, games_played=3, league_position=2),
            SimpleLeagueTableRow(Team("FC Awesome"), points=1, games_played=2, league_position=3),
            SimpleLeagueTableRow(Team("Snakes"), points=1, games_played=2, league_position=3),
            SimpleLeagueTableRow(Team("Grouches"), points=0, games_played=1, league_position=5)
        ]


    def get_game_results_where_teams_have_same_points(self) -> List[game_result]:
        return [
            game_result(
                teamA=team_statistic(team=Team("Lions"), goals_scored=3, team_result=TeamResult.DRAW),
                teamB=team_statistic(team=Team("Snakes"), goals_scored=3, team_result=TeamResult.DRAW)
            ),
            game_result(
                teamA=team_statistic(team=Team("Tarantulas"), goals_scored=1, team_result=TeamResult.DRAW),
                teamB=team_statistic(team=Team("FC Awesome"), goals_scored=1, team_result=TeamResult.DRAW)
            ),
            game_result(
                teamA=team_statistic(team=Team("Cheetahs"), goals_scored=1, team_result=TeamResult.DRAW),
                teamB=team_statistic(team=Team("Dogs"), goals_scored=1, team_result=TeamResult.DRAW)
            ),
            game_result(
                teamA=team_statistic(team=Team("Eagles"), goals_scored=3, team_result=TeamResult.DRAW),
                teamB=team_statistic(team=Team("Dolphins"), goals_scored=3, team_result=TeamResult.DRAW)
            ),
            game_result(
                teamA=team_statistic(team=Team("Buffalos"), goals_scored=4, team_result=TeamResult.DRAW),
                teamB=team_statistic(team=Team("Bulls"), goals_scored=4, team_result=TeamResult.DRAW)
            )
        ]

    def get_expected_league_table_for_teams_that_have_same_points(self) -> List[SimpleLeagueTableRow]:
        return [
            SimpleLeagueTableRow(Team("Buffalos"), points=1, games_played=1, league_position=1),
            SimpleLeagueTableRow(Team("Bulls"), points=1, games_played=1, league_position=1),
            SimpleLeagueTableRow(Team("Cheetahs"), points=1, games_played=1, league_position=1),
            SimpleLeagueTableRow(Team("Dogs"), points=1, games_played=1, league_position=1),
            SimpleLeagueTableRow(Team("Dolphins"), points=1, games_played=1, league_position=1),
            SimpleLeagueTableRow(Team("Eagles"), points=1, games_played=1, league_position=1),
            SimpleLeagueTableRow(Team("FC Awesome"), points=1, games_played=1, league_position=1),
            SimpleLeagueTableRow(Team("Lions"), points=1, games_played=1, league_position=1),
            SimpleLeagueTableRow(Team("Snakes"), points=1, games_played=1, league_position=1),
            SimpleLeagueTableRow(Team("Tarantulas"), points=1, games_played=1, league_position=1)
        ]

if __name__ == '__main__':
    unittest.main()
