import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance
from logic import generateNumbers, selectOperator, calculates, startMatch

def buildFrameGame(window):
    for widget in window.winfo_children():
        widget.destroy()

    window.title("The Math Game")
    for i in range(4):
        window.grid_rowconfigure(i, weight=1)
    for i in range(11):
        window.grid_columnconfigure(i, weight=1)
        
    currentMatch, maxMatch = startMatch()
    
    matchLabel = tk.Label(
        window,
        text="Match ",
        font=("Comic Sans MS", 15, "bold"),
        fg="midnight blue"
    )
    matchLabel.grid(row=0, column=1, pady=10, sticky="NE")

    matchs = tk.Label(
        window,
        text=f" {currentMatch} - {maxMatch} ",  
        font=("Graphik", 15, "normal"),
        fg="midnight blue",
        bg="white"
    )
    matchs.grid(row=0, column=2, pady=10, sticky="NW")
    
    scoreLabel = tk.Label(
        window,
        text="Score ",
        font=("Comic Sans MS", 15, "bold"),
        fg="midnight blue"
    )
    scoreLabel.grid(row=0, column=4, pady=10, sticky="NE")

    score = tk.Label(
        window,
        text="000000",
        font=("Graphik", 15, "normal"),
        fg="midnight blue",
        bg="white"
    )
    score.grid(row=0, column=5, pady=10, sticky="NW")

    timeLabel = tk.Label(
        window,
        text="Time ",
        font=("Comic Sans MS", 15, "bold"),
        fg="midnight blue"
    )
    timeLabel.grid(row=0, column=7, pady=10, sticky="NE")

    time = tk.Label(
        window,
        text="00:00:00",  
        font=("Graphik", 15, "normal"),
        fg="midnight blue",
        bg="white"
    )
    time.grid(row=0, column=8, pady=10, sticky="NW")

    

    def on_enterMin(event):
        hover_image = ImageEnhance.Brightness(Image.open(event.widget.image_path)).enhance(0.5)
        btn_icon_hover = ImageTk.PhotoImage(hover_image.resize((30, 30)))
        event.widget.config(image=btn_icon_hover)
        event.widget.hover_image = btn_icon_hover

    def on_leaveMin(event):
        event.widget.config(image=event.widget.original_image)

    help_icon_path = "C:/Users/Lorrany/Documents/game/img/help.png"
    help_image = Image.open(help_icon_path).resize((30, 30))
    help_icon = ImageTk.PhotoImage(help_image)

    helpButton = tk.Button(
        window,
        image=help_icon,
        borderwidth=0,
        command=lambda: print("Help clicked") 
    )
    helpButton.grid(row=0, column=9, pady=10, sticky="NE")
    helpButton.image_path = help_icon_path
    helpButton.original_image = help_icon 
    helpButton.bind("<Enter>", on_enterMin)
    helpButton.bind("<Leave>", on_leaveMin)

    pause_icon_path = "C:/Users/Lorrany/Documents/game/img/pause.png"
    pause_image = Image.open(pause_icon_path).resize((30, 30))
    pause_icon = ImageTk.PhotoImage(pause_image)

    pauseButton = tk.Button(
        window,
        image=pause_icon,
        borderwidth=0,
        command=lambda: print("Pause clicked") 
    )
    pauseButton.grid(row=0, column=10, pady=10, sticky="NW")
    pauseButton.image_path = pause_icon_path
    pauseButton.original_image = pause_icon  
    pauseButton.bind("<Enter>", on_enterMin)
    pauseButton.bind("<Leave>", on_leaveMin)

    num1, num2 = generateNumbers()
    operator = selectOperator()
    result = calculates(num1, num2, operator)

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

    def on_enterMax(event):
        hover_image = ImageEnhance.Brightness(Image.open(event.widget.image_path)).enhance(0.5)
        btn_icon_hover = ImageTk.PhotoImage(hover_image.resize((70, 70)))
        event.widget.config(image=btn_icon_hover)
        event.widget.hover_image = btn_icon_hover

    def on_leaveMax(event):
        event.widget.config(image=event.widget.original_image)
        
    operator_buttons = [
        ("sum", "C:/Users/Lorrany/Documents/game/img/sum.png", 2),
        ("sub", "C:/Users/Lorrany/Documents/game/img/sub.png", 4),
        ("mult", "C:/Users/Lorrany/Documents/game/img/mult.png", 6),
        ("div", "C:/Users/Lorrany/Documents/game/img/div.png", 8),
    ]

    for name, path, column in operator_buttons:
        icon_image = Image.open(path).resize((70, 70))
        operator_icon = ImageTk.PhotoImage(icon_image)

        button = tk.Button(
            window,
            image=operator_icon,
            borderwidth=0,
            command=lambda n=name: print(f"{n} clicked")  
        )
        button.grid(row=2, column=column, pady=10, sticky="S")
        button.image_path = path
        button.original_image = operator_icon
        button.bind("<Enter>", on_enterMax)
        button.bind("<Leave>", on_leaveMax)

    footerText = tk.Label(
        window,
        text="1.00v \nCreate by Marim, L.",
        font=("Graphik", 6),
        fg="gray14",
        justify="center"
    )
    footerText.grid(row=3, column=0, columnspan=11, pady=10)
