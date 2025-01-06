import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance
import os

def resetWindow(window):
    for widget in window.winfo_children():
        widget.destroy()

def defineGrid(window, r, c):
    for i in range(r):
        window.grid_rowconfigure(i, weight=1)
    for i in range(c):
        window.grid_columnconfigure(i, weight=1)

def on_enter(img_path, x, y, btn, event):
    if not os.path.exists(img_path):
        print(f"Erro: Arquivo '{img_path}' não encontrado.")
        return
    original_img = Image.open(img_path).resize((x, y))
    hover_img = ImageEnhance.Brightness(original_img).enhance(0.5)
    btn_hover = ImageTk.PhotoImage(hover_img)
    btn.config(image=btn_hover)
    btn.image = btn_hover

def on_leave(img_path, x, y, btn, event):
    if not os.path.exists(img_path):
        print(f"Erro: Arquivo '{img_path}' não encontrado.")
        return
    original_img = Image.open(img_path).resize((x, y))
    btn_icon = ImageTk.PhotoImage(original_img)
    btn.config(image=btn_icon)
    btn.image = btn_icon

def footerText(win):
    footer = tk.Label(
        win,
        text="1.00v \nCreate by Marim, L.",
        font=("Arial", 6),  
        fg="gray14",
        justify="center"  
    )
    return footer
