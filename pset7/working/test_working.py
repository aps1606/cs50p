from working import convert
from working_wrong import convert_wrong
import pytest


## --------- tests for the correct function ------------ ##

# checks that 12:00 is converted correctly
def test_correct_1():
    assert convert("12:00 AM to 4 PM") == "00:00 to 16:00"

# checks that minutes cannot be > 59
def test_correct_2():
    with pytest.raises(ValueError): 
        convert("4:65 PM to 1 AM")


## --------- tests for the wrong function ------------ ##

# below test fails because it ignores the minutes section of the time
def test_wrong_1():
    assert convert_wrong("1:25 AM to 3:35 AM") == "01:25 to 03:35" 


# below test should have raised a ValueError as the hours section has 3 digits, but it does not as the code is incorrect.
def test_wrong_2():
    with pytest.raises(ValueError):
        convert_wrong("222:05 PM to 09:55 AM")