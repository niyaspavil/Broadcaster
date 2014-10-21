from .datastore_connector import DataStore as ds

class DataStore(ds):
    """provides the persistent data storage on a single local file"""
    def __init__(self, user):
        """initialises the file store with the corresponding user"""
        pass

    def pull(self):
        """returns the data object associated datastore"""
        pass

    def push(self, data):
        """saves the data object passed to the datastore. this will replace the old data. returns True if succeeded"""
        pass

