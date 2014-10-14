#module datastore

class DataStore(object):
    """abstract class for persistant storage of attributes accessed by engine. The real implementation of DataStore should implement all the specified methods to give a proper accessibility for engine"""
    def __init__(self):
        raise NotImplementedError()

    def pull(self):
        raise NotImplementedError()

    def push(self):
        raise NotImplementedError()
