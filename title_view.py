#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk


class TitleView(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        label_header = tk.Label(
            self, text="INVENTORY MANAGER", font='Arial 15 bold',
            width=130, height=5, relief='groove').grid(row=1, column=0)
