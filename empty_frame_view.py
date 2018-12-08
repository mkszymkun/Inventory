#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle


class EmptyFrameView(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, width=70, height=10).grid(
            row=0, column=0)

    def on_show_frame(self, event):

        # tk.Label(text='empty').pack()

        tk.Label(self, width=70, height=10).grid(
            row=0, column=0)
