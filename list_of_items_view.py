#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle
from file_access import FileAccess
from graphics import Graphics
from list_of_items_logic import ListOfItemsLogic
from additional_buttons_logic import AdditionalButtonsLogic


class ListOfItemsView(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):

        for widget in self.winfo_children():
            widget.destroy()

        Graphics.login_header(self, "LISTA MATERIAŁÓW")
        Graphics.empty_row(self, 2, 1)

        locations_and_items_data = FileAccess.load_item_location_data(self)

        ListOfItemsLogic.locations_row = 3

        for location in locations_and_items_data.keys():
            ListOfItemsLogic.display_location_name_button(self, location)

        if AdditionalButtonsLogic.called:
            AdditionalButtonsLogic.called = False
            ListOfItemsLogic.location_chosen = True
            ListOfItemsLogic.chosen_location \
                = AdditionalButtonsLogic.chosen_location
            self.controller.show_frame("ListOfItemsView")

        if ListOfItemsLogic.location_chosen:
            ListOfItemsLogic.display_items_buttons(self)
