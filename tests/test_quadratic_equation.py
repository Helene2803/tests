import pytest
from quadratic_equation import discriminant, solution

params = (
    (1, 8, 15, 4),
    (1, -13, 12, 121),
    (-4, 28, -49, 0),
    (1, 1, 1, -3)
)

@pytest.mark.parametrize(
    'a, b, c, expected',
    params
)

def test_discriminant(a, b, c, expected):
    assert discriminant(a, b, c) == expected

params = (
    (1, 8, 15, (-3, -5)),
    (1, -13, 12, (12, 1)),
    (-4, 28, -49, 3.5),
    (1, 1, 1, 'корней нет')
)

@pytest.mark.parametrize(
    'a, b, c, expected',
    params
)

def test_solution(a, b, c, expected):
    assert solution(a, b, c) == expected
