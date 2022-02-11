from typing import List
from league_results_processor.dtos.simple_league_table_row import SimpleLeagueTableRow
from league_results_processor.file_writers.ifile_writer import IFileWriter

class SimpleFileWriter(IFileWriter):
    """docstring for SimpleFileWriter."""

    def write_to_file(self, output_file_path: str, league_rows: SimpleLeagueTableRow):
        output_lines: List[str] = []
        for row in league_rows:
            output_lines.append(self.file_formatter.get_formatted_output_line(row))
        with open(output_file_path, "w") as output_file:
            # Writing data to a file
            output_file.writelines(output_lines)