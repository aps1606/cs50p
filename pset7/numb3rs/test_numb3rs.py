from numb3rs import validate
from numb3rs_wrong import validate_wrong


# tests on the correct version of validate

def test_validate_correct_1():
    assert validate("256.1.1.1") == False


def test_validate_correct_2():
    assert validate("255.255.255.255") == True

# tests on the wrong version of validate

# The second byte is > 255 and the function should ideally return False. 
# But because this is the wrong function, it returns True and hence the test fails
def test_validate_wrong_1():
    assert validate_wrong("255.256.0.0") == False


# The 4th byte is comprised of alphabets and hence the function should ideally return False. 
# But because this is the wrong function, it returns True (regex wrongly written) and hence the test fails
def test_validate_wrong_2():
    assert validate_wrong("255.255.0.TEST") == False