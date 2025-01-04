import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance
from gameMain import Game_Page
from utils import resetWindow, defineGrid, on_enter, on_leave, footerText
from functools import partial

class Instruct_Page:
    def buildFrameInstructions(self,window):
        
        resetWindow(window)
        
        window.title("The Math Game")
        
        defineGrid(window,3,11)


        title = tk.Label(
            window,
            text="Welcome to the instructions",
            font=("Graphik", 18, "bold"),
            justify="center"
        )
        title.grid(row=0, column=0, columnspan=11, pady=10)

        instructionsText = tk.Label(
            window,
            text="Click on the correct symbols to complete the equations as quickly as possible.\n\nGood luck!",
            font=("Graphik", 12),
            justify="center"
        )
        instructionsText.grid(row=1, column=0, columnspan=11, pady=10, sticky="N")

        icon_path = "C:/Users/Lorrany/Documents/game/img/go.png"
        
        image_icon = Image.open(icon_path).resize((120, 120))
        icon = ImageTk.PhotoImage(image_icon)

        goButton = tk.Button(
            window,
            image=icon,
            borderwidth=0,
            command=lambda: Game_Page.buildFrameGame(self,window)  
        )
        
        goButton.grid(row=1, column=0, pady=20, columnspan=11, sticky="S")
        goButton.image = icon
        
        goButton.bind("<Enter>", partial(on_enter, icon_path, 120, 120, goButton))
        goButton.bind("<Leave>", partial(on_leave, icon_path, 120, 120, goButton))

        labelBottom = footerText(window)
        labelBottom.grid(row=2, column=0, columnspan=11, pady=10)
