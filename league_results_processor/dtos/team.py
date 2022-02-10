from league_results_processor.dtos.dto import DTO

class Team(DTO):
    """docstring for ClassName."""
    def __init__(self, name):
        super(Team, self).__init__()
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
