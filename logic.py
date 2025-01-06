import random
from tkinter import messagebox

class Operating_Data:
    @staticmethod
    def startGame(game_page_instance, window):
        count=1
        max=20
        score=0
        while count<=max:
            game_page_instance.buildFrameGame(window,count)
            window.wait_variable(window.continue_game)
            
            if not window.running:
                messagebox.showinfo("Jogo encerrado","Voce saiu do jogo.")
                break
            
            score+=random.randint(10,100)
            count+=1
        
        if count>max:
            messagebox.showinfo("Fim de jogo", f"Parabéns! Você completou o jogo com {score} pontos.")
        

        
    @staticmethod
    def startMatch(count,max):
        return count,max
    
    @staticmethod
    def startTime():
        m=00
        s=00
        h=00
        return m,s,h


class Functional_Data:
    @staticmethod
    def generateNumbers():
        return random.randint(0, 9), random.randint(0, 9)
    
    @staticmethod
    def selectOperator():
        return random.choice(["+", "-", "/", "*"])
    
    @staticmethod
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

