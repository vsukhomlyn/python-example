import pytest
from app.max2num.max2num import max2num


@pytest.mark.parametrize(
    'first, second, answer',
    [
        (1, 2, 2),
        (10, 30, 30),
        (-10, 2, 2),
    ]
)
def test_plus(first: int, second: int, answer: int):
    assert answer == max2num(first, second)


def test_plus_exception():
    with pytest.raises(TypeError):
        max2num(10, 's')
    with pytest.raises(TypeError):
        max2num('asd', 2)
    with pytest.raises(TypeError):
        max2num(10.2, 2)
