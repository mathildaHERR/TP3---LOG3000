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

- Tests pour `add(a, b)` : cas positifs, négatifs et zéro.
- Tests pour `subtract(a, b)` : vérifie l'implémentation actuelle (retourne `b - a`).
- Tests pour `multiply(a, b)` : l'implémentation actuelle effectue une puissance (`a ** b`).
- Tests pour `divide(a, b)` : division entière (`a // b`) et vérification que la division par zéro lève une exception.
