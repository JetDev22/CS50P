from bank import value


def test_value():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("yo") == 100
    assert value("") == 100
    assert value("HelLo") == 0
