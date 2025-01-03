import random

def startMatch():
    c=1
    m=20
    return c,m

def generateNumbers():
    return random.randint(0, 9), random.randint(0, 9)

def selectOperator():
    return random.choice(["+", "-", "/", "*"])

def calculates(a, b, operator):
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


