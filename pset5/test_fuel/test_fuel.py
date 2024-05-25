from fuel import convert, gauge
from fuel_wrong import convert_wrong, gauge_wrong
import pytest


# Test to check that convert raises a ValueError if X and Y are not ints
def test_convert_1(): 
    with pytest.raises(ValueError):
        convert("cat/dog")

# Test to check that convert raises a ZeroDivision if X and Y are not valid inputs
def test2_convert_2():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

# Test to check if gauge returns E and F correctly
def test_gauge_1():
    assert gauge(0) == "E"
    assert gauge(0.5) == "E"
    assert gauge(99.5) == "F"
    assert gauge(100) == "F"

# Test to check that gauge returns the correct % for a sample
def test_gauge_2():
    assert gauge(50) == "50%"


#------------------------Tests on wrong functions------------------#

# The below tests are for the convert and gauge functions from the "wrong" file, hence are meant to fail


# fraction of 4/5 should output 80% but test fails and raises a Value error instead because this is not being checked for in the wrong file
def test_convert_wrong_1():
    assert convert_wrong("4/5") == 80

# E and F are interchanged in the wrong gauge function
def test_gauge_wrong_1():
    assert gauge_wrong(99.5) == "F"
    assert gauge_wrong(0.5) == "E"

# gauge function does not display a %
def test_gauge_wrong_2():
    assert gauge_wrong(80) == "80%" 


