from .engine import Data

import ConfigParser
import os

__private_home__=os.path.expanduser("~")+os.path.sep+".Broadcaster"
__data_file__=__private_home__+os.path.sep+"data.ini"


def build_data(r_data, sector):
    """builds and returns Data instance from persistant storage"""
    data=Data()
    if r_data.has_section(sector):
        for k,v in r_data.items(sector):
            data.set(k,v)
    else:
        pass
    return data

def get_data_from_file(file):
    """returns the ConfigParser object with contents of file"""
    if check_file(file):
        r_data=ConfigParser.ConfigParser()
        r_data.read(file)
        return r_data
    else:
        raise Exception

def check_file(file):
    """checks whether file is already present, if not one is created."""
    try:
        path=os.path.dirname(file)
        if not os.path.isfile(file):
            if not os.path.exists(path):
                os.makedirs(path)
            new_f=open(file,"w")
            new_f.close()
        return True
    except Exception:
        return False

def pull(user):
    """returns the data object associated datastore"""
    pass

def push(data):
    """saves the data object passed to the datastore. this will replace the old data. returns True if succeeded"""
    pass


__data_raw__=get_data_from_file(__data_file__)
