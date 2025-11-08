import pytest
from operators import add, subtract, multiply, divide

@pytest.mark.parametrize("a,b,expected", [
	(1, 2, 3),
	(-1, 1, 0),
	(0, 0, 0),
])
def test_add(a, b, expected):
	"""Vérifie l'addition simple."""
	assert add(a, b) == expected


def test_subtract_order():
	"""La fonction `subtract(a,b)` renvoie actuellement `b - a`."""
	assert subtract(2, 5) == 3
	assert subtract(-1, 1) == 2


@pytest.mark.parametrize("a,b,expected", [
	(2, 3, 6),
	(3, 2, 6),
    (6, 4, 24)
])
def test_multiply(a, b, expected):
	"""`multiply` doit réaliser une multiplication."""
	assert multiply(a, b) == expected


def test_divide_integer_floor():
	"""`divide(a,b)` doit effectuer une division entière."""
	assert divide(7, 2) == 3
	assert divide(2, 7) == 0


def test_divide_by_zero_raises():
	"""On vérifie que la division par zéro lève une erreur."""
	with pytest.raises(ZeroDivisionError):
		divide(4, 0)

