import tkinter as tk
from PIL import Image, ImageTk
from instructions import Instruct_Page
from utils import resetWindow, defineGrid, on_enter, on_leave, footerText
from functools import partial
import os

def validate_image(path):
    if not os.path.exists(path):
        print(f"Erro: Arquivo '{path}' não encontrado.")
        return False
    return True

class Home_Page:            
    def buildFrameHome(self, window):
        
        resetWindow(window)
        
        window.title("The Math Game")
        
        defineGrid(window, 3, 11)

        logo_path = "C:/Users/Lorrany/Documents/game/img/Math_Game.png"
        if validate_image(logo_path):
            image_logo = Image.open(logo_path).resize((260, 180))
            logo = ImageTk.PhotoImage(image_logo)
            titleImage = tk.Label(window, image=logo, borderwidth=0)
            titleImage.grid(row=0, column=0, pady=5, columnspan=11)
            titleImage.image = logo  
        
        sublogos = [
            ("C:/Users/Lorrany/Documents/game/img/b1.png", 1, 0, 10, "NE"),
            ("C:/Users/Lorrany/Documents/game/img/b2.png", 1, 10, 10, "NW"),
            ("C:/Users/Lorrany/Documents/game/img/b3.png", 1, 0, 10, "SE"),
            ("C:/Users/Lorrany/Documents/game/img/b4.png", 1, 10, 10, "SW")
        ]
        
        for i, (path, row, column, pady, sticky) in enumerate(sublogos):
            if validate_image(path):
                image = Image.open(path).resize((30, 30))
                img = ImageTk.PhotoImage(image)
                label = tk.Label(window, image=img, borderwidth=0)
                label.grid(row=row, column=column, pady=pady, sticky=sticky)
                label.image = img

        icon_path = "C:/Users/Lorrany/Documents/game/img/play.png"
        if validate_image(icon_path):
            image_icon = Image.open(icon_path).resize((100, 100))
            icon = ImageTk.PhotoImage(image_icon)

            instruct_page = Instruct_Page()
            playButton = tk.Button(
                window,
                image=icon,
                borderwidth=0,
                command=lambda: instruct_page.buildFrameInstructions(window)  
            )
            
            playButton.grid(row=1, column=1, pady=20, columnspan=9)
            playButton.image = icon
            
            playButton.bind("<Enter>", lambda event: on_enter(icon_path, 100, 100, playButton, event))
            playButton.bind("<Leave>", lambda event: on_leave(icon_path, 100, 100, playButton, event))

        labelBottom = footerText(window)
        labelBottom.grid(row=2, column=1, columnspan=9, pady=10)
