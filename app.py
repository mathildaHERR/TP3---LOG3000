from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    :role : Effectuer l'opération sur les deux chiffres de l'expression

    :param expr: Expression mathématique
    :return: Le résultat de l'opération entre les deux chiffres
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            ## Si op_pos != -1, alors on a déjà trouvé un opérateur, car op_pos a été changé
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    ## L'opérande 'left' comprend tout ce qui est gauche de l'opérateur
    left = s[:op_pos]
    ## L'opérande 'right' comprend tout ce qui est à droite de l'opérateur
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    ## Exécute l'opération de notre expression qui est à la position op_char dans OPS
    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    :role : Définire la logique de la calculatrice

    :return: Le template de la page index.html avec le résultat calculé
    """
    result = ""
    ## Le résultat est calculé seulement quand l'utilisateur soumet une requête ('POST')
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)