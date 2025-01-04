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

def defineTime():
    m = 0
    s = 0
    c = 0
    run = False
    return m,s,c,run

def start_timer(run):
    if not run:
        run = True
        updateTime()

def updateTime(m,s,c,run,label,win):
    if run:
        c += 1
        if c == 100:
            c = 0
            s += 1
        if s == 60:
            s = 0
            m += 1

        label.config(text=f"{m:02}:{s:02}:{c:02}")

        win.after(10,updateTime)
    


