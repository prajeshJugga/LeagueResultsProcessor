from typing import List
from league_results_processor.dtos.simple_league_table_row import SimpleLeagueTableRow
from league_results_processor.file_writers.ifile_writer import IFileWriter

class SimpleFileWriter(IFileWriter):
    """docstring for SimpleFileWriter."""

    def write_to_file(self, output_file_path: str, league_rows: SimpleLeagueTableRow):
        output_lines: List[str] = []
        for index, row in enumerate(league_rows):
            line = self.file_formatter.get_formatted_output_line(row)
            if index != len(league_rows) - 1:
                line += '\n'
            output_lines.append(line)
        with open(output_file_path, "w") as output_file:
            # Writing data to a file
            output_file.writelines(output_lines)