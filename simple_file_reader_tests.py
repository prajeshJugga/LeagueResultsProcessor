import sys
import os
from typing import List
import unittest

from league_results_processor.file_objects.ifile_object import ifile_object
from league_results_processor.file_readers.simple_file_reader import SimpleFileReader

# Import the current working directory to import modules from an upper directory
# sys.path.append(os.path.join(os.getcwd()))

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

class simple_file_reader_tests(unittest.TestCase):
    """docstring for ClassName."""

    def successfully_read_file(self, file_path, expected_lines: List[ifile_object], file_reader: SimpleFileReader):
        # Arrange
        # Act
        actual_lines: List[ifile_object] = file_reader.read_file(file_path=file_path)
        # Assert
        self.maxDiff = None
        self.assertEqual(len(expected_lines), len(actual_lines))
        for index, value in enumerate(expected_lines):
            # print(index, value.file_line)
            self.assertEqual(value.file_line, actual_lines[index].file_line)

    def test_successfully_read_small_well_formatted_file(self):
        # Arrange
        file_reader: SimpleFileReader = SimpleFileReader()
        root_directory = self.get_root_directory()
        file_path = os.path.join(root_directory, 'valid_small_file.txt')
        # Act and Assert
        self.successfully_read_file(file_path=file_path, expected_lines=self.get_expected_lines_small_file(), file_reader=file_reader)

    def get_expected_lines_small_file(self) -> List[ifile_object]:
        return [
            ifile_object("Lions 3, Snakes 3"),
            ifile_object("Tarantulas 1, FC Awesome 0"),
            ifile_object("Lions 1, FC Awesome 1"),
            ifile_object("Tarantulas 3, Snakes 1"),
            ifile_object("Lions 4, Grouches 0")
        ]

    def get_root_directory(self):
        root_directory = os.path.join(os.getcwd(), "tests", "sample_files")
        return root_directory

if __name__ == '__main__':
    unittest.main()
