import sys
import os
from typing import List
import unittest
from league_results_processor.dtos.simple_league_table_row import SimpleLeagueTableRow
from league_results_processor.dtos.team import Team

from league_results_processor.file_objects.ifile_object import ifile_object
from league_results_processor.file_readers.simple_file_reader import SimpleFileReader
from league_results_processor.file_writers.simple_output_file_formatter import SimpleOutputFileFormatter

# Import the current working directory to import modules from an upper directory
# sys.path.append(os.path.join(os.getcwd()))

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

class simple_file_reader_tests(unittest.TestCase):
    """docstring for ClassName."""

    def test_correctly_formats_output_file_line_for_team_with_multiple_points(self):
        # Arrange
        league_output_line = SimpleLeagueTableRow(team=Team("Lions"), points=30, games_played=10, league_position=1)
        formatter = SimpleOutputFileFormatter()
        expected_output_line = "1. Lions, 30 pts"
        # Act
        actual_output_line = formatter.get_formatted_output_line(league_table_row=league_output_line)
        # Assert
        self.assertEqual(expected_output_line, actual_output_line)

    def test_correctly_formats_output_file_line_for_team_with_zero_points(self):
        # Arrange
        league_output_line = SimpleLeagueTableRow(team=Team("Lions"), points=0, games_played=3, league_position=20)
        formatter = SimpleOutputFileFormatter()
        expected_output_line = "20. Lions, 0 pts"
        # Act
        actual_output_line = formatter.get_formatted_output_line(league_table_row=league_output_line)
        # Assert
        self.assertEqual(expected_output_line, actual_output_line)

    def test_correctly_formats_output_file_line_for_team_with_single_point(self):
        # Arrange
        league_output_line = SimpleLeagueTableRow(team=Team("Lions"), points=1, games_played=4, league_position=14)
        formatter = SimpleOutputFileFormatter()
        expected_output_line = "14. Lions, 1 pt"
        # Act
        actual_output_line = formatter.get_formatted_output_line(league_table_row=league_output_line)
        # Assert
        self.assertEqual(expected_output_line, actual_output_line)

if __name__ == '__main__':
    unittest.main()
