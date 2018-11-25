#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle


class ItemsSearch(tk.Frame):

    item_to_find = ''

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):

        def find_item(user_input):

            item = user_input.get()

            self.item_to_find = item
            self.controller.show_frame("ItemsFound")

        for widget in self.winfo_children():
            widget.destroy()

        username = self.controller.get_page("Login").username

        label_username = tk.Label(self, text='Logged in as: {}'.format(username)).grid(row=0, column=0, sticky='w')

        label_header = tk.Label(self, text="WYSZUKIWARKA", font='Arial 15 bold', width=60, height=5,
                                relief='groove').grid(row=1, column=0, columnspan=2)
        label_empty_row = tk.Label(self).grid(row=2, column=1)

        # Buttons for adding a new location

        the_input_search = tk.Entry(self, width=50)
        the_input_search.grid(row=3, column=0, columnspan=2)

        button_search = tk.Button(self, text="Szukaj", width=50, height=3, relief='groove',
                                command=lambda: find_item(the_input_search)).grid(row=4, column=0,
                                                                                           columnspan=2)

        label_empty_row = tk.Label(self).grid(row=5, column=1)

        button_back = tk.Button(self, text="Wróć", width=30, height=3, relief='groove',
                                command=lambda: self.controller.show_frame("MainMenu")).grid(row=20, column=0,
                                                                                           columnspan=2)
