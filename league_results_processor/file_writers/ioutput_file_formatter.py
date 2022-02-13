from league_results_processor.dtos.league_table_row import LeagueTableRow
from league_results_processor.dtos.simple_league_table_row import SimpleLeagueTableRow

class IOutputFileFormatter:
    """docstring for IOutputFileFormatter."""
    def __init__(self):
        super(IOutputFileFormatter, self).__init__()

    def get_formatted_output_line(self, league_table_row: SimpleLeagueTableRow) -> str:
        pass