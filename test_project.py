import pytest
import project as p

def test_convert_buy():
    assert p.convert_buy(1, 1) == 4.65
    assert p.convert_buy(10, 1) == 46.5

def test_convert_sell():
    assert p.convert_sell(1, 1) == 4.67
    assert p.convert_sell(10, 1) == 46.7


def test_check_currency():
    assert p.check_currency("usd") == 3
    assert p.check_currency("pln") == None