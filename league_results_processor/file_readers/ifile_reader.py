from typing import List
from league_results_processor.file_objects.ifile_object import ifile_object

class ifile_reader:
    """docstring for ClassName."""

    def read_file(self, file_path) -> List[ifile_object]:
        with open(file_path, 'r') as reader:
            # Further file processing goes here
            # return reader.readlines()
            file_objects: List[ifile_object] = []
            for line in reader.readlines():
                file_objects.append(ifile_object(line.strip()))
            return file_objects
