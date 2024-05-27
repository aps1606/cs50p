from um import count
from um_wrong import count_wrong


#------tests for the correct function --------#


def test_um_correct_1():
    assert count("um thanks for the album") == 1

def test_um_correct_2():
    assert count("um....thanks um....cerebellum and umbrealla") == 2

def test_um_correct_3():
    assert count("     ......humour.....cerebrum......") == 0




#------tests for the wrong function --------#

# below test fails because the regex expression is not accounting for word boundaries using \b
def test_um_wrong_1():
    assert count_wrong("um thanks for the album") == 1

def test_um_wrong_2():
    assert count_wrong("um hummm um ") == 2

