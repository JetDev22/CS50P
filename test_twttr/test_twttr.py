from twttr import shorten


def test_shorten():
    assert shorten("test") == "tst"
    assert shorten("Twitter") == "Twttr"
    assert shorten("Aeio") == ""
    assert shorten("test.") == "tst."
    assert shorten("t2est") == "t2st"
