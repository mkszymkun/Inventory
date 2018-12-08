#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle
from file_access import FileAccess
from graphics import Graphics
from list_of_locations_logic import ListOfLocationsLogic


class ListOfLocationsView(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):
    
        for widget in self.winfo_children():
            widget.destroy()

        Graphics.login_header(self, "LISTA MAGAZYNÓW")
        Graphics.empty_row(self, 2, 1)

        row = 3

        locations_and_items_data = FileAccess.load_item_location_data(self)

        for location in locations_and_items_data.keys():
            Graphics.location_label(self, location, row)
            ListOfLocationsLogic.display_location_delete_button(self, location, row)
            row += 1
            Graphics.empty_row(self, row + 1, 1)

        location_to_add = tk.Entry(self, width=30)
        location_to_add.grid(row=row+2, column=0)

        ListOfLocationsLogic.display_add_location_button(self, location_to_add, row)

        Graphics.empty_row(self, row + 3, 1)
