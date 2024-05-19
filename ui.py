import tkinter as tk
from tkinter import ttk
import random
import sv_ttk

class NovaUI:
    def __init__(self):
        self.root = tk.Tk()

    def add_button(self, text, action):
        bt = Button(self.root, text=text, height=1, width=7, command=action)
        bt.pack()

    def mainloop(self):
        self.root.mainloop()
