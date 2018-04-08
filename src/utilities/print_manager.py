

class PrintManager(object):
    """Object in charge of redirecting the output of print operations
       to the right location. This allows to either print to standard
       output and error, to files or to strings in the memory for unit
       test purposes
    """
    def __init__(self, arg):
        super(PrintManager, self).__init__()
        self.arg = arg
