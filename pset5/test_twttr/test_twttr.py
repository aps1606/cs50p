from twttr import shorten
from twttr_wrong import shorten_wrong
import pytest


# testing the function imported from the "correct" twittr code file - twttr.py
def test_correct_function():
    assert shorten("THiS IS CS50") == "THS S CS50"

# testing the function imported from the "wrong" twittr code file - twttr_wrong.py
def test_wrong_function():
    assert shorten_wrong("THiS IS CS50") == "THS S CS50"
