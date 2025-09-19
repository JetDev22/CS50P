from um import count


def test_Postive():
    assert count("um") == 1
    assert count("This um, is um test") == 2


def test_Negative():
    assert count("Nothing to see here") == 0
    assert count("Nope") == 0


def test_Embeded():
    assert count("Yummy um") == 1


def test_Case():
    assert count("Um") == 1
