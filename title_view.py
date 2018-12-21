#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
from tkinter import font as tkfont


class TitleView(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        font = tkfont.Font(family='Ubuntu', size=25, weight="bold")
        image = tk.PhotoImage(file="pictures/labels/title.png")
        label = tk.Label(text="INVENTORY MANAGER", font=font, image=image,
                         borderwidth='0', bg='#303030',  fg='white',
                         activebackground='#303030',  compound='center',
                         highlightbackground='#303030')
        label.image = image
        label.grid(row=0, column=0, columnspan=5)
