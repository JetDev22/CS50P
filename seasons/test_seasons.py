from seasons import checkDate, convert
import pytest


def test_DateInput():
    with pytest.raises(SystemExit):
        checkDate("cat")
