from league_results_processor.dtos.dto import DTO
from league_results_processor.dtos.team import Team
from league_results_processor.enums.team_result import team_result


class team_statistic(DTO):
    """docstring for ClassName."""
    # def __init__(self, team: team, goals_scored: int,  goals_conceded: int, team_result: team_result):
    def __init__(self, team: Team, goals_scored: int,  team_result: team_result):
        super(team_statistic, self).__init__()
        self.team = team
        self.goals_scored = goals_scored
        # self.goals_conceded = goals_conceded
        self.team_result = team_result

    @property
    def team(self) -> Team:
        return self._team

    @team.setter
    def team(self, value):
        self._team = value

    @property
    def goals_scored(self):
        return self._goals_scored

    @goals_scored.setter
    def goals_scored(self, value):
        self._goals_scored = value

    @property
    def goals_conceded(self):
        return self._goals_conceded

    @goals_conceded.setter
    def goals_conceded(self, value):
        self._goals_conceded = value

    @property
    def team_result(self):
        return self._team_result

    @team_result.setter
    def team_result(self, value):
        self._team_result = value
