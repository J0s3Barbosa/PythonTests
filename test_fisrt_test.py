
from config import CONFIG

def test_get_conn_value():
    test_conn = CONFIG['Config']
    assert  test_conn != ''
