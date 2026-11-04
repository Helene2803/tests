import pytest
from palindrome import palindrome

params = (
    (['нажал кабан на баклажан'], ['нажал кабан на баклажан']),
    (['дом как комод'], []),
    (['рвал дед лавр'], ['рвал дед лавр']),
    (['азот калий и лактоза'], ['азот калий и лактоза']),
    (['а собака боса'], ['а собака боса']),
    (['тонет енот'], ['тонет енот']),
    (['карман мрак'], []),
    (['пуст суп'], ['пуст суп']),
    (['а роза упала на лапу азора'], ['а роза упала на лапу азора']),
    ([], [])
)

@pytest.mark.parametrize(
    'phrases, expected',
    params
)

def test_palindrome(phrases, expected):
    assert palindrome(phrases) == expected
