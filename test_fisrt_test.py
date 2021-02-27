
from config import CONFIG

def test_foo_bar():
       assert True

def test_get_conn_value():
    test_conn = CONFIG['Config']
    assert  test_conn != ''
