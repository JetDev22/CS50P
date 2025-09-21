from project import portfolioValue, portfolioCost, dcaYield, calcROI, getRate
import pytest


def test_PortfolioValue():
    assert portfolioValue(1, 1000) == 1000
    with pytest.raises(SystemExit):
        portfolioValue(1, "1000")


def test_PortfolioCost():
    assert portfolioCost(1, 1000) == 1000
    with pytest.raises(SystemExit):
        portfolioValue("1", 1000)


def test_DCAYield():
    assert dcaYield(500, 1000) == 0.5
    with pytest.raises(SystemExit):
        dcaYield("500", 1000)


def test_calcROI():
    assert calcROI(1000, 500) == 100
    with pytest.raises(SystemExit):
        calcROI(1000, 0)


def test_getRate():
    with pytest.raises(KeyError):
        getRate("none")
