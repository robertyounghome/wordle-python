class Error(Exception):
    """ Base class for custom exceptions """
    pass 

class InvalidMask(Error):
    """ Raised when a mask is invalid. """
    pass 

class InvalidWord(Error):
    """ Raised when a word is invalid. """
    pass


