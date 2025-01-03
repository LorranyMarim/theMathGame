import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance
from gameMain import buildFrameGame

def buildFrameInstructions(window):
    for widget in window.winfo_children():
        widget.destroy()

    window.title("The Math Game")
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)
    window.grid_rowconfigure(3, weight=1)
    window.grid_rowconfigure(4, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    title = tk.Label(
        window,
        text="Welcome to the instructions",
        font=("Graphik", 15, "bold"),
        justify="center"
    )
    title.grid(row=0, column=0, columnspan=2, pady=(20, 10))

    instructionsText = tk.Label(
        window,
        text="Click on the correct symbols to complete the equations as quickly as possible.\n\nGood luck!",
        font=("Graphik", 10),
        justify="center"
    )
    instructionsText.grid(row=1, column=0, columnspan=2, pady=(10, 20))

    icon_path = "C:/Users/Lorrany/Documents/game/img/go.png"
    image_icon = Image.open(icon_path).resize((100, 100))
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
    goButton.grid(row=3, column=0, pady=20, columnspan=2)
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
    footerText.grid(row=4, column=0, columnspan=2, pady=(10, 20))
