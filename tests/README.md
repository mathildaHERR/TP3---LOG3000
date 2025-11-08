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

### `test_app.py`

- Cible la fonction `calculate(expr)` exportée par `app.py`.
- Vérifie les expressions valides (retour float) :
  - "1 + 2" -> 3.0
  - "2\*3" -> 6.0
  - "7/2" -> 3.5
  - "5-2" -> 3.0
- Vérifie les formats invalides lèvent `ValueError` :
  - Chaîne vide `""`
  - Plusieurs opérateurs `"1+2+3"`
  - Opérateur en début `"+1"`
  - Opérateur en fin `"1+"`
  - Opérandes non numériques `"a+b"`
- Vérifie que les entrées non-chaînes (ex. `None`) lèvent `ValueError`.
- Comportement attendu de `calculate` (pour le code testé) :
  - Normalise la chaîne (suppression d'espaces) et n'accepte qu'une seule opération binaire.
  - Vérifie que les deux opérandes sont numériques et que l'opérateur est bien placé entre elles.
  - Retourne toujours un float pour les résultats numériques.
