from ..datastore import DataStore

ds=None

def test_init():
    global ds
    ds=DataStore("mydata")

def test_pull():
    data=ds.pull()

def test_push():
    ds.push()
