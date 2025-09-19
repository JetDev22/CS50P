from plates import is_valid


def test_correct():
    assert is_valid("CS50") == True


def test_leadingZero():
    assert is_valid("CS05") == False


def test_lastChar():
    assert is_valid("CS50P") == False


def test_symbol():
    assert is_valid("PI3.14") == False


def test_length():
    assert is_valid("H") == False


def test_numericBegin():
    assert is_valid("5556") == False
