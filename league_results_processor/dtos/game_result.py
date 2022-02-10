from league_results_processor.dtos.dto import DTO
from league_results_processor.dtos.team_statistic import team_statistic


class game_result(DTO):
    """docstring for ClassName."""
    def __init__(self, teamA: team_statistic, teamB: team_statistic):
        self.teamA = teamA
        self.teamB = teamB

    @property
    def teamA(self):
        return self._teamA

    @teamA.setter
    def teamA(self, value):
        self._teamA = value

    @property
    def teamB(self):
        return self._teamB

    @teamB.setter
    def teamB(self, value):
        self._teamB = value