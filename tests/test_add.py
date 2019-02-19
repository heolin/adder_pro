import pytest
from adder.lib import add


@pytest.mark.parametrize("a, b", [(1, 2), (3, 4)])
def test_adds_two_numbers(a, b):
    assert add(a, b) == (a + b)
