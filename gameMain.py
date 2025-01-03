import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance
from logic import generateNumbers, selectOperator, calculates

def buildFrameGame(window):
    for widget in window.winfo_children():
        widget.destroy()

    window.title("The Math Game")
    for i in range(6):
        window.grid_rowconfigure(i, weight=1)
    for i in range(11):
        window.grid_columnconfigure(i, weight=1)
    
    scoreLabel = tk.Label(
        window,
        text="Score:",
        font=("Comic Sans MS", 12, "bold"),
        fg="midnight blue"
    )
    scoreLabel.grid(row=0, column=1, pady=10, sticky="NE")
    
    score = tk.Label(
        window,
        text="000000",
        font=("Comic Sans MS", 12, "normal"),
        fg="black",
        bg="white"
    )
    score.grid(row=0, column=3, pady=10, sticky="NW")
    
   
    timeLabel = tk.Label(
        window,
        text="Time:",
        font=("Comic Sans MS", 12, "bold"),
        fg="midnight blue"
    )
    timeLabel.grid(row=0, column=5, pady=10, sticky="NE")
    
    time = tk.Label(
        window,
        text="00:00:00",  
        font=("Comic Sans MS", 12, "normal"),
        fg="black",
        bg="white"
    )
    time.grid(row=0, column=7, pady=10, sticky="NW")

    def on_enter(event):
        hover_image = ImageEnhance.Brightness(Image.open(event.widget.image_path)).enhance(0.5)
        btn_icon_hover = ImageTk.PhotoImage(hover_image.resize((25, 25)))
        event.widget.config(image=btn_icon_hover)
        event.widget.hover_image = btn_icon_hover

    def on_leave(event):
        event.widget.config(image=event.widget.original_image)

    help_icon_path = "C:/Users/Lorrany/Documents/game/img/help.png"
    help_image = Image.open(help_icon_path).resize((25, 25))
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
    helpButton.bind("<Enter>", on_enter)
    helpButton.bind("<Leave>", on_leave)

    pause_icon_path = "C:/Users/Lorrany/Documents/game/img/pause.png"
    pause_image = Image.open(pause_icon_path).resize((25, 25))
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
    pauseButton.bind("<Enter>", on_enter)
    pauseButton.bind("<Leave>", on_leave)

    num1, num2 = generateNumbers()
    operator = selectOperator()
    result = calculates(num1, num2, operator)

    value1 = tk.Label(
        window,
        text=num1,  
        font=("Graphik", 35, "normal"),
        fg="midnight blue",
    )
    value1.grid(row=2, column=2, pady=10, sticky="E")
    
    operatorLabel = tk.Label(
        window,
        text=operator,  
        font=("Graphik", 35, "normal"),
        fg="red3",
    )
    operatorLabel.grid(row=2, column=3, pady=10)
    
    value2 = tk.Label(
        window,
        text=num2,  
        font=("Graphik", 35, "normal"),
        fg="midnight blue",
    )
    value2.grid(row=2, column=4, pady=10, sticky="W")
    
    equalSimbol = tk.Label(
        window,
        text="=",  
        font=("Graphik", 35, "normal"),
        fg="midnight blue",
    )
    equalSimbol.grid(row=2, column=5, pady=10)
    
    resultValue = tk.Label(
        window,
        text=result,  
        font=("Graphik", 35, "normal"),
        fg="midnight blue",
    )
    resultValue.grid(row=2, column=6, pady=10, sticky="W")

    operator_buttons = [
        ("sum", "C:/Users/Lorrany/Documents/game/img/sum.png"),
        ("sub", "C:/Users/Lorrany/Documents/game/img/sub.png"),
        ("mult", "C:/Users/Lorrany/Documents/game/img/mult.png"),
        ("div", "C:/Users/Lorrany/Documents/game/img/div.png")
    ]

    for idx, (name, path) in enumerate(operator_buttons):
        icon_image = Image.open(path).resize((50, 50))
        operator_icon = ImageTk.PhotoImage(icon_image)

        def create_hover_handler(button, image_path):
            def on_enter(event):
                hover_image = ImageEnhance.Brightness(Image.open(image_path)).enhance(0.5)
                btn_icon_hover = ImageTk.PhotoImage(hover_image.resize((50, 50)))
                button.config(image=btn_icon_hover)
                button.hover_image = btn_icon_hover

            def on_leave(event):
                button.config(image=button.original_image)

            return on_enter, on_leave

        button = tk.Button(
            window,
            image=operator_icon,
            borderwidth=0,
            command=lambda n=name: print(f"{n} clicked")  
        )
        button.grid(row=3, column=3 + idx, pady=10, padx=5)
        button.image_path = path
        button.original_image = operator_icon  
        enter_handler, leave_handler = create_hover_handler(button, path)
        button.bind("<Enter>", enter_handler)
        button.bind("<Leave>", leave_handler)

    footerText = tk.Label(
        window,
        text="1.00v \nCreate by Marim, L.",
        font=("Graphik", 6),
        fg="gray14",
        justify="center"
    )
    footerText.grid(row=5, column=1, columnspan=9, pady=(10, 20))
