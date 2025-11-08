import pytest
from operators import add, subtract, multiply, divide

@pytest.mark.parametrize("a,b,expected", [
	(2, 3, 5),
	(3, 2, 5),
    (6, 4, 10),
    (2, -3, -1),
    (0, 24, 24)
])
def test_add(a, b, expected):
	"""Vérifie l'addition simple."""
	assert add(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
	(2, 3, -1),
	(3, 2, 1),
    (6, 4, 2),
    (2, -3, 5),
    (0, 24, -24)
])
def test_subtract(a, b, expected):
	"""`subtract(a,b)` doit renvoyer `a - b`."""
	assert subtract(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
	(2, 3, 6),
	(3, 2, 6),
    (6, 4, 24),
    (-2, 3, -6),
    (0, 24, 0)
])
def test_multiply(a, b, expected):
	"""`multiply` doit réaliser une multiplication."""
	assert multiply(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
	(2, 3, 0),
	(13, 2, 6),
    (62, 4, 15),
    (-20, 3, -7),
    (0, 24, 0)
])
def test_divide_integer_floor(a, b, expected):
	"""`divide(a,b)` doit effectuer une division entière."""
	assert divide(a, b) == expected


def test_divide_by_zero_raises():
	"""On vérifie que la division par zéro lève une erreur."""
	with pytest.raises(ZeroDivisionError):
		divide(4, 0)

