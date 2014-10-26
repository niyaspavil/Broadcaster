from .. import file_datastore as fsc
from .. import engine
import shutil, os, ConfigParser

data=None
r_data=None

def test_pull():
    global data
    pass

def test_push():
    pass

def test_check_file():
    assert fsc.check_file("/tmp/test/test_file")==True
    assert fsc.check_file("test")==False
    shutil.rmtree("/tmp/test")

def test_get_data_from_file():
    global r_data
    data_file=os.path.dirname(__file__)+os.path.sep+"test_data"+os.path.sep+"data.ini"
    conf=ConfigParser.ConfigParser()
    conf.add_section("neo")
    conf.set("neo","user","neo")
    conf.set("neo","timestamp","999")
    fsc.check_file(data_file)
    file=open(data_file, "w")
    conf.write(file)
    file.close()
    r_data=fsc.get_data_from_file(data_file)
    assert isinstance(r_data, ConfigParser.ConfigParser)==True
    assert r_data.get("neo","user")=="neo"
    assert r_data.get("neo","timestamp")=="999"

def test_build_data():
    global r_data
    data=fsc.build_data(r_data, "neo")
    assert isinstance(data, engine.Data)==True
    assert data.get("user")=="neo"
