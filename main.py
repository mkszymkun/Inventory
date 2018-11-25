#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle, re
from login import Login
from register import Register
from mainMenu import MainMenu
from itemsShow import ItemsShow
from locationsShow import LocationsShow
from itemsPrivate import ItemsPrivate
from itemsSearch import ItemsSearch
from itemsFound import ItemsFound
from locationsConfirm import LocationsConfirm


class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self, width=100, height=100)
        
        container.pack(padx=5, pady=5, expand=True)

        container.grid_rowconfigure(10, weight=1)
        container.grid_columnconfigure(10, weight=1)

        self.frames = {}

        def save_obj(obj, name):
            with open(name + '.pkl', 'wb') as f:
                pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

        def load_obj(name):
            with open(name + '.pkl', 'rb') as f:
                return pickle.load(f)

        try:
            load_obj('item_location_data')
        except:
            item_location_data = {}
            save_obj(item_location_data, 'item_location_data')

        try:
            load_obj('users')
        except:
            users = {}
            save_obj(users, 'users')

        for F in (Register, MainMenu, ItemsShow, LocationsShow, ItemsPrivate, ItemsSearch, ItemsFound, LocationsConfirm, Login):

            cont = F.__name__

            frame = F(container, self)

            self.frames[cont] = frame

            frame.grid(row=2, column=2, sticky="nsew")

        self.show_frame("Login")

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.event_generate("<<ShowFrame>>")
        frame.tkraise()

    def get_page(self, frame_class):
        return self.frames[frame_class]


app = Main()

app.mainloop()
