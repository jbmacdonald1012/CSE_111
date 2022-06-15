from address import extract_city, \
    extract_state, extract_zipcode
import pytest

def test_extract_city():
    extract_city('455 W 5th S, Rexburg, Idaho, 83440') == 'Rexburg'
    extract_city('3319 Addison Ave E, Kimberly, Idaho, 83341') == 'Kimberly'
    extract_city('118 Upper Bay Rd, Sanbornton, New Hampshire, 03269') == 'Sanbornton'
    extract_city('750 S Gateway Dr, River Heights, Utah, 84321') == 'River Heights'



def test_extract_state():
    extract_state('455 W 5th S, Rexburg, Idaho, 83440') == 'Idaho'
    extract_state('3319 Addison Ave E, Kimberly, Idaho, 83341') == 'Idaho'
    extract_state('118 Upper Bay Rd, Sanbornton, New Hampshire, 03269') == 'New Hampshire'
    extract_state('750 S Gateway Dr, River Heights, Utah, 84321') == 'Utah'


def test_extract_zipcode():
    extract_zipcode('455 W 5th S, Rexburg, Idaho, 83440') == '83440'
    extract_zipcode('3319 Addison Ave E, Kimberly, Idaho, 83341') == '83341'
    extract_zipcode('118 Upper Bay Rd, Sanbornton, New Hampshire, 03269') == '03269'
    extract_zipcode('750 S Gateway Dr, River Heights, Utah, 84321') == '84321'


pytest.main(["-v", "--tb=line", "-rN", __file__])