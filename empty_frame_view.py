#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk


class EmptyFrameView(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, width=70, height=10).grid(
            row=0, column=0)

    def on_show_frame(self, event):

        tk.Label(self, width=70, height=10).grid(
            row=0, column=0)
