from .. import file_store_connector as fsc
from .. import engine
import shutil, os, ConfigParser

ds=None
data=None
r_data=None

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
    global r_data
    r_data=fsc.get_data_from_file(os.path.dirname(__file__)+os.path.sep+"test_data"+os.path.sep+"data.ini")
    assert isinstance(r_data, ConfigParser.ConfigParser)==True
    assert r_data.get("neo","user")=="neo"
    assert r_data.get("neo","timestamp")=="999"

def test_build_data():
    global r_data
    data=fsc.build_data(r_data, "neo")
    assert isinstance(data, engine.Data)==True
    assert data.get("user")=="neo"
