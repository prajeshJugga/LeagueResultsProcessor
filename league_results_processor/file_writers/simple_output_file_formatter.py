from league_results_processor.dtos.simple_league_table_row import SimpleLeagueTableRow
from league_results_processor.file_writers.ioutput_file_formatter import IOutputFileFormatter

class SimpleOutputFileFormatter(IOutputFileFormatter):
    """docstring for SimpleOutputFileFormatter."""
    def __init__(self):
        super(SimpleOutputFileFormatter, self).__init__()

    def get_formatted_output_line(self, league_table_row: SimpleLeagueTableRow) -> str:
        output_line = '{position}. {team}, {points} '.format(position=league_table_row.league_position, team=league_table_row.team.name, points=league_table_row.points)
        if league_table_row.points == 1:
            return output_line + 'pt'
        return output_line + 'pts'