from ..datastore_connector import DataStore
import pytest

ds=None 

def test_init():
    global ds
    with pytest.raises(NotImplementedError):
       ds=DataStore("user")
 
def test_methods():
    with pytest.raises(AttributeError):
        ds.pull()
    with pytest.raises(AttributeError):
        ds.push("unknown_data")
