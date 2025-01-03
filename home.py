import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance
from instructions import buildFrameInstructions

def buildFrameHome(window):
    for widget in window.winfo_children():
        widget.destroy()

    window.title("The Math Game")
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    logo_path = "C:/Users/Lorrany/Documents/game/img/Math_Game.png"
    image_logo = Image.open(logo_path).resize((150, 150))
    logo = ImageTk.PhotoImage(image_logo)

    titleImage = tk.Label(window, image=logo, borderwidth=0)
    titleImage.grid(row=0, column=0, pady=10, columnspan=2)
    titleImage.image = logo  

    def on_enter(event):
        hover_image = ImageEnhance.Brightness(image_icon).enhance(0.5)
        play_icon_hover = ImageTk.PhotoImage(hover_image)
        playButton.config(image=play_icon_hover)
        playButton.image = play_icon_hover

    def on_leave(event):
        playButton.config(image=icon)
        playButton.image = icon

    icon_path = "C:/Users/Lorrany/Documents/game/img/play.png"
    image_icon = Image.open(icon_path).resize((100, 100))
    icon = ImageTk.PhotoImage(image_icon)

    playButton = tk.Button(
        window,
        image=icon,
        borderwidth=0,
        command=lambda: buildFrameInstructions(window)  
    )
    playButton.grid(row=1, column=0, pady=20, columnspan=2)
    playButton.image = icon
    playButton.bind("<Enter>", on_enter)
    playButton.bind("<Leave>", on_leave)

    footerText = tk.Label(
        window,
        text="1.00v \nCreate by Marim, L.",
        font=("Graphik", 6),
        fg="gray14"
    )
    footerText.grid(row=3, column=0, pady=10, columnspan=2)
