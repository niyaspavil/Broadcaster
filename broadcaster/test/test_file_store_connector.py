from .. import file_store_connector as fsc
import shutil, os, ConfigParser

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

def test_check_file():
    assert fsc.check_file("/tmp/test/test_file")==True
    assert fsc.check_file("test")==False
    shutil.rmtree("/tmp/test")

def test_get_data_from_file():
    data_r=fsc.get_data_from_file(os.path.dirname(__file__)+os.path.sep+"test_data"+os.path.sep+"data.ini")
    assert isinstance(data_r, ConfigParser.ConfigParser)==True
    assert data_r.get("neo","user")=="neo"
    assert data_r.get("neo","timestamp")=="999"
