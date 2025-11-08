import pytest
from app import calculate


@pytest.mark.parametrize("expr,expected", [
    ("1 + 2", 3.0),        # add: 1.0 + 2.0 -> 3.0
    ("2*3", 6.0),          # multiply attendu: 2 * 3 -> 6.0
    ("7/2", 3.5),          # divide attendu: 7.0 / 2.0 -> 3.5
    ("5-2", 3.0),          # subtract attendu: 5.0 - 2.0 -> 3.0
])
def test_calculate_valid_expressions(expr, expected):
    """Vérifie que `calculate` évalue correctement des expressions simples.
    """
    result = calculate(expr)
    assert result == pytest.approx(expected)


@pytest.mark.parametrize("expr", [
    "",          # expression vide
    "1+2+3",     # plusieurs opérateurs non autorisés
    "+1",        # opérateur en début
    "1+",        # opérateur en fin
    "a+b",       # opérandes non numériques
])
def test_calculate_invalid_expressions(expr):
    """S'assure que les formats invalides lèvent `ValueError`.

    `calculate` normalise la chaîne et valide : présence d'un seul
    opérateur, opérandes numériques, et position correcte de l'opérateur.
    """
    with pytest.raises(ValueError):
        calculate(expr)


def test_calculate_non_string_input():
    """La fonction doit rejeter des entrées non-chaînes (type guard).

    Le code lève `ValueError` si l'argument n'est pas une chaîne non vide.
    """
    with pytest.raises(ValueError):
        calculate(None)
