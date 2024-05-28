from jar import Jar
import pytest

# testing capacity on __init__ initialisation instance method
def test_cookiejar_correct_1():
    cookiejar = Jar()
    assert cookiejar.capacity == 12


# testing __str__ instance method
def test_cookiejar_correct_2():
    cookiejar = Jar()
    cookiejar.deposit(2)
    assert str(cookiejar) == "🍪🍪"

# testing cookiejar.deposit() instance method. Also checking that deposit cannot exceed capacity
def test_cookiejar_correct_3():
    cookiejar = Jar()
    cookiejar.deposit(5)
    assert cookiejar.size == 5

    with pytest.raises(ValueError):
        cookiejar.deposit(13)


# testing cookiejar.withdraw() instance method
def test_cookiejar_correct_4():
    cookiejar = Jar()
    cookiejar.deposit(5)
    cookiejar.withdraw(2)
    assert cookiejar.size == 3

    with pytest.raises(ValueError):
        cookiejar.withdraw(13)


