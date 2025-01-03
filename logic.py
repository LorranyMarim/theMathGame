import random

def generateNumbers():
    """Gera dois números aleatórios entre 0 e 9."""
    return random.randint(0, 9), random.randint(0, 9)

def selectOperator():
    """Seleciona um operador matemático aleatório."""
    return random.choice(["+", "-", "/", "*"])

def calculates(a, b, operator):
    """Realiza o cálculo baseado no operador fornecido."""
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return round(a / (b if b != 0 else 1), 2)
    else:
        raise ValueError("Operador inválido")


