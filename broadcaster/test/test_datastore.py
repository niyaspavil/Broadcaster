from ..datastore_connector import DataStore

ds=None
data=None

def test_init():
    global ds
    ds=DataStore("user")

def test_pull():
    global data
    data=ds.pull()

def test_push():
    ds.push(data)
