import tkinter as tk
from home import Home_Page

home_page = Home_Page()

def buildMain():
    window = tk.Tk()
    window.geometry("800x600")
    window.title("The Math Game")
    return window

window = buildMain()
home_page.buildFrameHome(window)

window.mainloop()
