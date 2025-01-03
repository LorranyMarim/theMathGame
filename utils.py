def resetWindow(window):
    for widget in window.winfo_children():
        widget.destroy()

def defineGrid(window,r,c):
    for i in range(r):
        window.grid_rowconfigure(i, weight=1)
    for i in range(c):
        window.grid_columnconfigure(i, weight=1)