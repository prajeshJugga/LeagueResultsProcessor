class InvalidArgumentsException(Exception):
    """docstring for ClassName."""
    def __init__(self, message):
        super(InvalidArgumentsException, self).__init__()
        self.message = message
