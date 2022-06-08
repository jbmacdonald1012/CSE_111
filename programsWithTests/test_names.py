from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name('Ryan', 'Manthey') == 'Manthey; Ryan'

def test_extract_family_name():
    assert extract_family_name('Macdonald; Jason') == 'Macdonald'

def test_extract_given_name():
    assert extract_given_name('Baker; Celeste') == 'Celeste'


pytest.main(["-v", "--tb=line", "-rN", __file__])

