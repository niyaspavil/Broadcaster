from .. import file_store_connector as fsc

ds=None
data=None

def test_init():
    global ds
    ds=fsc.DataStore("user")

def test_pull():
    global data
    data=ds.pull()

def test_push():
    ds.push(data)
