from jar import Jar
import pytest


def test_deposit():
    jar = Jar(5)
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_withdraw():
    jar = Jar(10)
    jar.deposit(10)
    jar.withdraw(9)
    assert str(jar) == "🍪"


def test_init():
    jar = Jar(10)
    assert str(jar) == ""


def test_str():
    with pytest.raises(ValueError):
        jar = Jar("cat")
