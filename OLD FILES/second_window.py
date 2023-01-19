from tkinter import *


class SecondWindow:
    def __init__(self, first, width, height, title="NewApp", resizable=(False, False), icon=None):
        self.second = Toplevel(first)
        self.second.title(title)
        self.second.geometry(f"{width}x{height}+200+200")
        self.second.resizable(resizable[0], resizable[1])
        if icon:
            self.second.iconbitmap(icon)
        self.second.configure(background='Grey')
        self.second.grab_set()
        self.second.focus_set()
        self.second.wait_window()

