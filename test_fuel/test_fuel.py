from fuel import convert
from fuel import gauge
import pytest


def test_convert():
    assert convert("1/2") == 50


def test_ValueError():
    with pytest.raises(ValueError):
        convert("A/B")


def test_ValueErrorNeg():
    with pytest.raises(ValueError):
        convert("-2/4")


def test_ZeroDivision():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(50) == "50%"


def test_Empty():
    assert gauge(1) == "E"


def test_Full():
    assert gauge(99) == "F"
