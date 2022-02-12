import os
import sys
import unittest

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

class simple_file_reader_tests(unittest.TestCase):
    """docstring for ClassName."""

    def test_writes_file_successfully(arg):
        pass

    def get_root_directory(self):
        root_directory = os.path.join(os.getcwd(), "tests", "output_files")
        return root_directory

if __name__ == '__main__':
    unittest.main()
