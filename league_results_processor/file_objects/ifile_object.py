class ifile_object:
    def __init__(self, file_line):
        self.file_line = file_line

    @property
    def file_line(self):
        return self._file_line

    @file_line.setter
    def file_line(self, value):
        self._file_line = value