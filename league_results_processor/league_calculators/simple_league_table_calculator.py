from typing import List
from league_results_processor.dtos.game_points import GamePoints
from league_results_processor.dtos.game_result import game_result
from league_results_processor.dtos.simple_league_table_row import SimpleLeagueTableRow
from league_results_processor.dtos.team import Team
from league_results_processor.enums.team_result import TeamResult
from league_results_processor.league_calculators.ileague_table_calculator import ILeagueTableCalculator

class SimpleLeagueTableCalculator(ILeagueTableCalculator):
    """docstring for ClassName."""

    def get_league_table(self, game_results_list: List[game_result]) -> List[SimpleLeagueTableRow]:
        league_table_rows = []
        distinct_teams: List[Team] = self.__get_distinct_teams(game_results_list)
        for distinct_team in distinct_teams:
            league_table_row = SimpleLeagueTableRow(team=distinct_team, points=0, games_played=0, league_position=0)
            league_table_row.team = distinct_team
            teams_game_results: List[game_result] = self.__get_teams_results(game_results_list, distinct_team)
            for game in teams_game_results:
                self.__set_teams_points(distinct_team, game, league_table_row)
            league_table_rows.append(league_table_row)
        return self.__get_sorted_league_table(league_table_rows)

    def __get_sorted_league_table(self, league_rows: List[SimpleLeagueTableRow]):
        league_rows = sorted(league_rows, key=lambda x: (-x.points, x.team.name))
        previous_points: float = 0
        for index, value in enumerate(league_rows):
            # print("team: ", value.team.name, "points: ", value.points, "position: ", value.league_position)
            if self.__is_tied_on_points(previous_points, value):
                value.league_position = league_rows[index - 1].league_position
            else:
                value.league_position = index + 1
            previous_points = value.points
        return league_rows

    def __is_tied_on_points(self, previous_points: float, league_row: SimpleLeagueTableRow):
        return previous_points == league_row.points

    def __set_teams_points(self, team: Team, game_result: game_result, league_table_row: SimpleLeagueTableRow):
        if self.__is_same_team(team, game_result.teamA.team):
            league_table_row.points += self.__get_teams_points_for_result(team_result=game_result.teamA.team_result, game_points=self.game_points)
            league_table_row.games_played += 1
        elif self.__is_same_team(team, game_result.teamB.team):
            league_table_row.points += self.__get_teams_points_for_result(team_result=game_result.teamB.team_result, game_points=self.game_points)
            league_table_row.games_played += 1

    def __get_teams_points_for_result(self, team_result: TeamResult, game_points: GamePoints) -> float:
        points_dictionary = {
            TeamResult.WIN : game_points.win_points,
            TeamResult.DRAW : game_points.draw_points,
            TeamResult.LOSE : game_points.loss_points,
            TeamResult.NOT_CALCULATED : 0
        }
        return points_dictionary.get(team_result, 0)

    def __get_teams_results(self, game_results_list: List[game_result], distinct_team: Team) -> List[game_result]:
        return filter(lambda x: self.__is_same_team(x.teamA.team, distinct_team) or self.__is_same_team(x.teamB.team, distinct_team),game_results_list)

    def __get_distinct_teams(self, game_results_list: List[game_result]) -> List[Team]:
        distinct_teams: List[Team] = []
        for game_result_obj in game_results_list:
            if self.__is_distinct_team(distinct_teams, game_result_obj.teamA.team):
                distinct_teams.append(game_result_obj.teamA.team)
            if self.__is_distinct_team(distinct_teams, game_result_obj.teamB.team):
                distinct_teams.append(game_result_obj.teamB.team)
        return distinct_teams

    def __is_distinct_team(self, distinct_teams: List[Team], team: Team) -> bool:
        found_teams = list(filter(lambda x: self.__is_same_team(x, team),  distinct_teams))
        return len(found_teams) == 0

    def __is_same_team(self, first_team: Team, second_team: Team) -> bool:
        return first_team.name.casefold() == second_team.name.casefold()
