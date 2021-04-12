import tkinter as tk
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
import random
from functools import partial

root1 = tk.Tk()


class new_window():
    def __init__(self, id):
        self.window = tk.Toplevel()



background_image1 = tk.PhotoImage(file = 'images\\email.png')
# have used a button not a label for me to make another tk window
background_button1 = tk.Button(root1, image = background_image1, command = partial(new_window,1))
background_button1.pack()
root1.mainloop()