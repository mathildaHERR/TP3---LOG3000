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
	(2, 3, 2/3),
	(13, 2, 13/2),
	(62, 4, 62/4),
	(-20, 3, -20/3),
	(0, 24, 0/24)
])
def test_divide_real_division(a, b, expected):
	"""`divide(a, b)` doit effectuer une division réelle (a / b).

	Les résultats sont comparés avec `pytest.approx` pour tenir compte
	d'éventuelles représentations flottantes.
	"""
	assert divide(a, b) == pytest.approx(expected)


def test_divide_by_zero_raises():
	"""On vérifie que la division par zéro lève une erreur."""
	with pytest.raises(ZeroDivisionError):
		divide(4, 0)

