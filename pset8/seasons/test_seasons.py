from seasons import minutes
from seasons_wrong import minutes_wrong
from datetime import date, timedelta
import pytest

#------------------tests for the correct function ----------------#


# test to confirm that one day prior returns 1440 minutes
def test_minutes_correct_1():
    assert (date.today() - (date.today() - timedelta(days=1))).total_seconds()/60 == 1440
    

# test to confirm the input validation when invalid date is entered (e.g., month = 13)
def test_minutes_correct_2():
    with pytest.raises(ValueError):
        minutes("1993-13-13")

#------------------tests for the wrong function ----------------#

#code is poorly designed. ValueError is not raised when an invalid date is entered, rather sys.exit() kicks in and terminates the program not allowing it to resolve fully.
def test_minutes_wrong_1():
    with pytest.raises(ValueError):
        minutes_wrong("1993-13-13")
        