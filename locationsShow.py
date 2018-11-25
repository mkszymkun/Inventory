#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle


class LocationsShow(tk.Frame):

    user_input = ''

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):

        def save_obj(obj, name):
            with open(name + '.pkl', 'wb') as f:
                pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

        def load_obj(name):
            with open(name + '.pkl', 'rb') as f:
                return pickle.load(f)

        def confirm_location_removal(key):
            self.user_input = key
            self.controller.show_frame("LocationsConfirm")

        def add_location(input_location, output_list):
            output_list[input_location.lower()] = {}
            save_obj(output_list, 'item_location_data')
            self.controller.show_frame("LocationsShow")
    
        for widget in self.winfo_children():
            widget.destroy()

        row = 3
        data = load_obj('item_location_data')

        username = self.controller.get_page("Login").username

        label_username = tk.Label(self, text='Logged in as: {}'.format(username)).grid(row=0, column=0, sticky='w')

        label_header = tk.Label(self, text="LISTA MAGAZYNÓW", font='Arial 15 bold', width=60, height=5, relief='groove').grid(row=1, column=0, columnspan=2)
        label_empty_row = tk.Label(self).grid(row=2, column=1)

        for key in data.keys():
            label_location = tk.Label(self, text = key.upper(), width=50, height=2, font='Arial 10 bold', relief='groove').grid(row=row,column=0)
            label_delete = tk.Button(self, text = "Usuń", width=30, height=2, relief='groove',
                                command=lambda i=key: confirm_location_removal(i)).grid(row=row, column=1)
            row +=1
            label_empty_row = tk.Label(self).grid(row=row+1,column=1)

        label_empty_row = tk.Label(self).grid(row=row+1,column=1)

        the_input_add_location = tk.Entry(self, width=30)
        the_input_add_location.grid(row=row+2, column=0)
        label_add_location = tk.Button(self, text = "Dodaj nowy", width=30, relief='groove',
                            command=lambda: add_location(the_input_add_location.get(), load_obj('item_location_data'))).grid(row=row+2, column=1)

        label_empty_row = tk.Label(self).grid(row=row+3, column=1)

        button_back = tk.Button(self, text="Wróć", width=30, height=3, relief='groove',
                        command=lambda: self.controller.show_frame("MainMenu")).grid(row=row+4, column=0, columnspan=2)

