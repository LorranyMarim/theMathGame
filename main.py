import tkinter as tk
from home import buildFrameHome

window = tk.Tk()
window.geometry("800x600")
window.title("The Math Game")

buildFrameHome(window)

window.mainloop()
