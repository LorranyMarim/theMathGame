import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance
from instructions import buildFrameInstructions

def buildFrameHome(window):
    for widget in window.winfo_children():
        widget.destroy()

    window.title("The Math Game")
    for i in range(3):
        window.grid_rowconfigure(i, weight=1)
    for i in range(11):
        window.grid_columnconfigure(i, weight=1)

    logo_path = "C:/Users/Lorrany/Documents/game/img/Math_Game.png"
    image_logo = Image.open(logo_path).resize((260,180))
    logo = ImageTk.PhotoImage(image_logo)
    titleImage = tk.Label(window, image=logo, borderwidth=0)
    titleImage.grid(row=0, column=0, pady=5, columnspan=11)
    titleImage.image = logo  
    
    back_logo1 = "C:/Users/Lorrany/Documents/game/img/b1.png"
    sublogo1 = Image.open(back_logo1).resize((30,30))
    sublogoImg1 = ImageTk.PhotoImage(sublogo1)
    backGround1 = tk.Label(window, image=sublogoImg1, borderwidth=0)
    backGround1.grid(row=1, column=0, pady=10, sticky="NE")
    backGround1.image = sublogoImg1 
    
    back_logo2 = "C:/Users/Lorrany/Documents/game/img/b2.png"
    sublogo2 = Image.open(back_logo2).resize((30,30))
    sublogoImg2 = ImageTk.PhotoImage(sublogo2)
    backGround2 = tk.Label(window, image=sublogoImg2, borderwidth=0)
    backGround2.grid(row=1, column=10, pady=10, sticky="NW")
    backGround2.image = sublogoImg2 
    
    back_logo3 = "C:/Users/Lorrany/Documents/game/img/b3.png"
    sublogo3 = Image.open(back_logo3).resize((30,30))
    sublogoImg3 = ImageTk.PhotoImage(sublogo3)
    backGround3 = tk.Label(window, image=sublogoImg3, borderwidth=0)
    backGround3.grid(row=1, column=0, pady=10, sticky="SE")
    backGround3.image = sublogoImg3 
    
    back_logo4 = "C:/Users/Lorrany/Documents/game/img/b4.png"
    sublogo4 = Image.open(back_logo4).resize((30,30))
    sublogoImg4 = ImageTk.PhotoImage(sublogo4)
    backGround4 = tk.Label(window, image=sublogoImg4, borderwidth=0)
    backGround4.grid(row=1, column=10, pady=10, sticky="SW")
    backGround4.image = sublogoImg4 

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
    playButton.grid(row=1, column=1, pady=20, columnspan=9)
    playButton.image = icon
    playButton.bind("<Enter>", on_enter)
    playButton.bind("<Leave>", on_leave)

    footerText = tk.Label(
        window,
        text="1.00v \nCreate by Marim, L.",
        font=("Graphik", 6),
        fg="gray14",
        justify="center"
    )
    footerText.grid(row=2, column=1, columnspan=9, pady=10)
