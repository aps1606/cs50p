from plates import is_valid
from plates_wrong import is_valid_wrong


## Tests for the "correct" is_valid function from the "correct" plates.py file


def test_1_isvalid_correct():
    # this test should pass as alphabet cannot follow numbers 
    assert is_valid("AA2AAA") == False

def test_2_isvalid_correct():
    # this test should pass as number plate is too long (>6 characters)
    assert is_valid("BBBBBBB") == False

def test_3_isvalid_correct():
    # this test should pass as 1st two characters of number plate have to be alphabets and cannot contain numbers
    assert is_valid("12ABCD") == False

def test_4_isvalid_correct():
    # this test should pass as the case of input should not matter
    assert is_valid("abcd12") == True


## Tests for the "wrong" is_valid_wrong function from the "wrong" plates_wrong.py file


def test_5_isvalid_wrong():
    # This test should fail as the program now wrongly allows for more than 6 characters to be on the numnber plate
    # i.e., the function is returning True even though it should actually return False.
    assert is_valid_wrong("ABCD123") == False

def test_6_isvalid_wrong():
    # This test should fail as the program now wrongly allows for the 1st 2 characters to be numbers when only alphabets are allowed, also alphabets are following numbers which is not allowed.
    # i.e., the function is returning True even though it should actually return False.
    assert is_valid_wrong("123456") == False

def test_7_isvalid_wrong():
    # This test should fail as the first number cannot be 0.
    # i.e., the function is returning True even though it should actually return False.
    assert is_valid_wrong("AB0123") == False

def test_8_isvalid_wrong():
    # This test should fail as alphabets cannot follow numbers.
    # i.e., the function is returning True even though it should actually return False.
    assert is_valid_wrong("AB12CD") == False


