#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle


class MainMenu(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):

        def empty_row(row, col):
            tk.Label(self).grid(row=row, column=col)

        def button(text, width, frame, row):
            tk.Button(self, text=text, font='Arial 10', width=width, height=6, relief='groove',
                      command=lambda: self.controller.show_frame(frame)).grid(row=row, column=1)

        username = self.controller.get_page("Login").username

        label_username = tk.Label(self, text='Logged in as: {}'.format(username)).grid(row=0, column=1, sticky='w')

        label_header = tk.Label(self, text="MENU", font='Arial 15 bold', width=60, height=5, relief='groove').grid(row=1, column=1)
        
        empty_row(2,1)

        button("Materiały", 60, "ItemsShow", 3)

        button("Wyszukiwarka", 60, "ItemsSearch", 4)

        button("Magazyny", 60, "LocationsShow", 5)

        button("Moje rezerwacje", 60, "ItemsPrivate", 6)

        empty_row(7,1)

        button("Wyloguj", 30, "Login", 8)
