import tkinter as tk
from PIL import Image, ImageTk
from logic import Operating_Data, Functional_Data
from utils import resetWindow, defineGrid, on_enter, on_leave, footerText
from functools import partial
import os

class Game_Page:
    def buildFrameGame(self,window,current_match):
        resetWindow(window)
        
        min,sec,hund = Operating_Data.startTime()
        
        window.title("The Math Game")
        
        defineGrid(window,4,11)
        window.grid_columnconfigure(1, minsize=60)
        window.grid_columnconfigure(3, minsize=60)
        window.grid_columnconfigure(5, minsize=60)
        window.grid_columnconfigure(7, minsize=60)
        window.grid_columnconfigure(9, minsize=60)

        
      
        
        matchLabel = tk.Label(
            window,
            text="Match ",
            font=("Comic Sans MS", 15, "bold"),
            fg="midnight blue"
        )
        matchLabel.grid(row=0, column=1, pady=10, sticky="E")

        matchs = tk.Label(
            window,
            text=f" {current_match} /20 ",  
            font=("Graphik", 15, "normal"),
            fg="midnight blue",
            bg="white"
        )
        matchs.grid(row=0, column=2, pady=10, sticky="W")
    
        scoreLabel = tk.Label(
            window,
            text="Score ",
            font=("Comic Sans MS", 15, "bold"),
            fg="midnight blue"
        )
        scoreLabel.grid(row=0, column=4, pady=10, sticky="E")

        score = tk.Label(
            window,
            text="00000",
            font=("Graphik", 15, "normal"),
            fg="midnight blue",
            bg="white"
        )
        score.grid(row=0, column=5, pady=10, sticky="W")

        timeLabel = tk.Label(
            window,
            text="Time ",
            font=("Comic Sans MS", 15, "bold"),
            fg="midnight blue"
        )
        timeLabel.grid(row=0, column=7, pady=10, sticky="E")

        time = tk.Label(
            window,
            text=f"{min}:{sec}:{hund}",  
            font=("Graphik", 15, "normal"),
            fg="midnight blue",
            bg="white"
        )
        time.grid(row=0, column=8, pady=10, sticky="W")

        help_icon_path = "C:/Users/Lorrany/Documents/game/img/help.png"
        help_image = Image.open(help_icon_path).resize((30, 30))
        help_icon = ImageTk.PhotoImage(help_image)

        helpButton = tk.Button(
            window,
            image=help_icon,
            borderwidth=0,
            command=lambda: print("Help clicked") 
        )
        
        helpButton.grid(row=0, column=9, pady=10, sticky="E")
        helpButton.image = help_icon
        
        helpButton.bind("<Enter>", partial(on_enter, help_icon_path, 30, 30, helpButton))
        helpButton.bind("<Leave>", partial(on_leave, help_icon_path, 30, 30, helpButton))

        pause_icon_path = "C:/Users/Lorrany/Documents/game/img/pause.png"
        pause_image = Image.open(pause_icon_path).resize((30, 30))
        pause_icon = ImageTk.PhotoImage(pause_image)

        pauseButton = tk.Button(
            window,
            image=pause_icon,
            borderwidth=0,
            command=lambda: print("Pause clicked") 
        )
        
        pauseButton.grid(row=0, column=10, pady=10, sticky="W")
        pauseButton.image = pause_icon
        
        pauseButton.bind("<Enter>", partial(on_enter, pause_icon_path, 30, 30, pauseButton))
        pauseButton.bind("<Leave>", partial(on_leave, pause_icon_path, 30, 30, pauseButton))

        num1, num2 = Functional_Data.generateNumbers()
        operator = Functional_Data.selectOperator()
        result = Functional_Data.calculates(num1, num2, operator)

        value1 = tk.Label(
            window,
            text=num1,  
            font=("Graphik", 50, "bold"),
            fg="midnight blue",
        )
        value1.grid(row=1, column=1, pady=10, sticky="SE")

        operatorLabel = tk.Label(
            window,
            text="?",  
            font=("Graphik", 50, "bold"),
            fg="red3",
            bg="white"
        )
        operatorLabel.grid(row=1, column=3, pady=10, sticky="S")

        value2 = tk.Label(
            window,
            text=num2,  
            font=("Graphik", 50, "bold"),
            fg="midnight blue",
        )
        value2.grid(row=1, column=5, pady=10, sticky="S")

        equalSimbol = tk.Label(
            window,
            text="=",  
            font=("Graphik", 50, "bold"),
            fg="midnight blue",
        )
        equalSimbol.grid(row=1, column=7, pady=10, sticky="S")

        resultValue = tk.Label(
            window,
            text=result,  
            font=("Graphik", 50, "bold"),
            fg="midnight blue",
        )
        resultValue.grid(row=1, column=9, pady=10, sticky="SW")

        operator_buttons = [
            ("C:/Users/Lorrany/Documents/game/img/sum.png", 2, 2, "sum"),
            ("C:/Users/Lorrany/Documents/game/img/sub.png", 2, 4, "sub"),
            ("C:/Users/Lorrany/Documents/game/img/mult.png", 2, 6, "mult"),
            ("C:/Users/Lorrany/Documents/game/img/div.png", 2, 8, "div")
        ]

        for path, row, column, op in operator_buttons:
            if not os.path.exists(path):
                print(f"Erro: Arquivo '{path}' não encontrado.")
                continue

            icon_image = Image.open(path).resize((70, 70))
            operator_icon = ImageTk.PhotoImage(icon_image)

            button = tk.Button(
                window,
                image=operator_icon,
                borderwidth=0,
                command=partial(self.handle_operator, window, op),
            )

            button.grid(row=row, column=column, pady=10, sticky="S")
            button.image = operator_icon

            button.bind("<Enter>", lambda event, p=path: on_enter(p, 70, 70, button, event))
            button.bind("<Leave>", lambda event, p=path: on_leave(p, 70, 70, button, event))

        labelBottom = footerText(window)
        labelBottom.grid(row=3, column=0, columnspan=11, pady=10)

    def handle_operator(self, window, operation):
        print(f"Operação escolhida: {operation}")
        window.continue_game.set(True)