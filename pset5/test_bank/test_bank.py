from bank import value
from bank_wrong import value_wrong


# this is the correct function. regardless of the case the function returns the correct amounts
def test_correct_function():
    assert value("HELLO") == 0
    assert value("HEY") == 20
    assert value("WHAT'S UP?") == 100


#tests for the "wrong" function

def test_wrong_function_case():
    assert value_wrong("HEY") == 20 # this test fails because the function is case sensitive. It should be built to be case-insensitive.

def test_wrong_function_value():
    assert value_wrong("hello") == 0 # this test fails because the return value "hello" is wrongly coded to return 100 instead of zero

'''
Psuedo/notes




'''




