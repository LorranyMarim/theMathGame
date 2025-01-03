import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance
from gameMain import buildFrameGame
from utils import resetWindow, defineGrid

class Instruct_Page:
    def buildFrameInstructions(self,window):
        
        resetWindow(window)
        
        window.title("The Math Game")
        
        row=3
        column=11
        defineGrid(window,row,column)


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

        def on_enter(event):
            hover_image = ImageEnhance.Brightness(image_icon).enhance(0.5)
            go_icon_hover = ImageTk.PhotoImage(hover_image)
            goButton.config(image=go_icon_hover)
            goButton.image = go_icon_hover

        def on_leave(event):
            goButton.config(image=icon)
            goButton.image = icon

        goButton = tk.Button(
            window,
            image=icon,
            borderwidth=0,
            command=lambda: buildFrameGame(window)  
        )
        goButton.grid(row=1, column=0, pady=20, columnspan=11, sticky="S")
        goButton.image = icon
        goButton.bind("<Enter>", on_enter)
        goButton.bind("<Leave>", on_leave)

        footerText = tk.Label(
            window,
            text="1.00v \nCreate by Marim, L.",
            font=("Graphik", 6),
            fg="gray14",
            justify="center"
        )
        footerText.grid(row=2, column=0, columnspan=11, pady=10)
