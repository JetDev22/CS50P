from numb3rs import validate


def test_Valid():
    assert validate("192.168.178.1") == True
    assert validate("255.255.255.255") == True


def test_Invalid():
    assert validate("199") == False
    assert validate("300.168.178.155") == False
    assert validate("192.168.178.300") == False


def test_String():
    assert validate("cat") == False
    assert validate("ip") == False
