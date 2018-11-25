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

        username = self.controller.get_page("Login").username

        label_username = tk.Label(self, text='Logged in as: {}'.format(username)).grid(row=0, column=1, sticky='w')

        label_header = tk.Label(self, text="MENU", font='Arial 15 bold', width=60, height=5, relief='groove').grid(row=1, column=1)
        
        empty_row(2,1)

        button_items = tk.Button(self, text="Materiały", font='Arial 10', width=60, height=6, relief='groove',
                            command=lambda: self.controller.show_frame("ItemsShow")).grid(row=3,column=1)

        button_items_search = tk.Button(self, text="Wyszukiwarka", font='Arial 10', width=60, height=6, relief='groove',
                                 command=lambda: self.controller.show_frame("ItemsSearch")).grid(row=4, column=1)

        button_locations = tk.Button(self, text="Magazyny", font='Arial 10', width=60, height=6, relief='groove',
                            command=lambda: self.controller.show_frame("LocationsShow")).grid(row=5, column=1)

        button_private = tk.Button(self, text="Moje rezerwacje", font='Arial 10', width=60, height=6, relief='groove',
                                     command=lambda: self.controller.show_frame("ItemsPrivate")).grid(row=6, column=1)

        empty_row(7,1)

        button_quit = tk.Button(self, text="Wyloguj", font='Arial 10', width=30, height=4, relief='groove',
                            command=lambda: self.controller.show_frame("Login")).grid(row=8, column=1)
