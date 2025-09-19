from working import convert
import pytest


def test_Whole():
    assert convert("3 AM to 5 PM") == "03:00 to 17:00"
    assert convert("4 PM to 3 AM") == "16:00 to 03:00"


def test_Partial():
    assert convert("3:30 AM to 5:30 PM") == "03:30 to 17:30"
    assert convert("4:00 PM to 3:25 AM") == "16:00 to 03:25"


def test_String():
    with pytest.raises(ValueError):
        convert("cat")


def test_wrongFormat():
    with pytest.raises(ValueError):
        convert("9 to 5")


def test_outOfRange():
    with pytest.raises(ValueError):
        convert("13 AM to 29 PM")
