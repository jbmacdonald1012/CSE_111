from address import extract_city, \
    extract_state, extract_zipcode
import pytest

def test_extract_city():
    extract_city('455 W 5th S, Rexburg, Idaho, 83440') == 'Rexburg'

def test_extract_state():
    extract_state('455 W 5th S, Rexburg, Idaho, 83440') == 'Idaho'

def test_extract_zipcode():
    extract_zipcode('455 W 5th S, Rexburg, Idaho, 83440') == '83440'

pytest.main(["-v", "--tb=line", "-rN", __file__])