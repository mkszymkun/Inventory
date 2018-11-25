#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle


class LocationsConfirm(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):

        username = self.controller.get_page("Login").username

        def save_obj(obj, name):
            with open(name + '.pkl', 'wb') as f:
                pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

        def load_obj(name):
            with open(name + '.pkl', 'rb') as f:
                return pickle.load(f)

        def remove_location(input_location, output_list):
            output_list.pop(input_location.lower())
            save_obj(output_list, 'item_location_data')
            self.controller.show_frame("LocationsShow")

        label_username = tk.Label(self, text='Logged in as: {}'.format(username)).grid(row=0, column=1, sticky='w')

        user_input = self.controller.get_page("LocationsShow").user_input

        label_header = tk.Label(self, text="USUNĄĆ {}?".format(user_input.upper()),font='Arial 15 bold', width=60, height=5, relief='groove').grid(row=1, column=1)

        label_empty_row = tk.Label(self).grid(row=2,column=1)

        label_info = tk.Label(self, text="Cała zawartość magazynu zostanie usunięta.", font='Arial 10', width=55, height=5).grid(row=3, column=1)

        user_input = self.controller.get_page("LocationsShow").user_input

        button_delete = tk.Button(self, text="Usuń", width=30, height=3, relief='groove',
                        command=lambda: remove_location(user_input, load_obj('item_location_data'))).grid(row=8, column=1)

        button_back = tk.Button(self, text="Wróć", width=30, height=3, relief='groove',
                        command=lambda: self.controller.show_frame("LocationsShow")).grid(row=9, column=1)
