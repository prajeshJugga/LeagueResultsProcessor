from typing import List
from league_results_processor.dtos.simple_league_table_row import SimpleLeagueTableRow
from league_results_processor.file_writers.ioutput_file_formatter import IOutputFileFormatter

class IFileWriter:
    """docstring for IFileWriter."""

    def __init__(self, file_formatter: IOutputFileFormatter):
        self.file_formatter = file_formatter

    def write_to_file(self, output_file_path: str, league_rows: List[SimpleLeagueTableRow]):
        pass
