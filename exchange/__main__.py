#!/usr/bin/env python3
from gui import Application
import tkinter as tk


if __name__=="__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()