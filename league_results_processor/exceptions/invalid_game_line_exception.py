class InvalidGameLineException(Exception):
    """docstring for ClassName."""
    def __init__(self, message):
        super(InvalidGameLineException, self).__init__()
        self.message = message
