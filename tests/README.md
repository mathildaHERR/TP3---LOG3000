# Tests unitaires

Ce répertoire contient des tests pytest pour le projet.

## Exécuter les tests

1. Depuis la racine du projet, installez pytest si nécessaire :

```powershell
python -m pip install -U pytest
```

2. Lancer la suite de tests :

```powershell
python -m pytest -q
```

## Résumé rapide

### `test_operators.py`

- Tests pour `add(a, b)` : vérifie que l'implémentation actuelle retourne bien une addition. Cas positifs, négatifs et zéro.
- Tests pour `subtract(a, b)` : vérifie que l'implémentation actuelle retourne bien une soustraction de a par b. Cas positifs, négatifs et zéro.
- Tests pour `multiply(a, b)` : vérifie que l'implémentation actuelle retourne bien une multiplication. Cas positifs, négatifs et zéro.
- Tests pour `divide(a, b)` : vérifie que l'implémentation actuelle retourne bien une division entière et vérification que la division par zéro lève une exception. Cas positifs, négatifs et zéro.
