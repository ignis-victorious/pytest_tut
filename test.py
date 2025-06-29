#  _______________
#  Import LIBRARIES
#  Import FILES
from main import add_some_numbers as add_some_numbers

#  _______________


# print(add_some_numbers)


def test_add_some_numbers() -> None:
    """Test with two positive integers."""
    # assert() To pass the test, Pytest wants everything inside the parenthesys 2b True!
    # assert True  # Other examples: False, 0, "Hello"
    # result: int = add_some_numbers(x=10, y=10)
    # assert result == 20
    assert add_some_numbers(x=10, y=10) == 20
    assert add_some_numbers(x=1, y=1) == 2
    assert add_some_numbers(x=10, y=100) == 110


def test_add_some_numbers_positive_integers() -> None:
    """
    Test with two positive integers.
    """
    result: int = add_some_numbers(x=2, y=3)
    assert result == 5


def test_add_some_numbers_negative_integers() -> None:
    """
    Test with two negative integers.
    """
    result: int = add_some_numbers(x=-5, y=-3)
    assert result == -8


def test_add_some_numbers_mixed_integers() -> None:
    """
    Test with a positive and a negative integer.
    """
    result: int = add_some_numbers(x=10, y=-7)
    assert result == 3


def test_add_some_numbers_with_zero() -> None:
    """
    Test with one number being zero.
    """
    result: int = add_some_numbers(x=0, y=7)
    assert result == 7
    result: int = add_some_numbers(x=5, y=0)
    assert result == 5
    result: int = add_some_numbers(x=0, y=0)
    assert result == 0


def test_add_some_numbers_large_numbers() -> None:
    """
    Test with large numbers to ensure no overflow issues (for typical int sizes).
    """
    result = add_some_numbers(x=1000000, y=2000000)
    assert result == 3000000
