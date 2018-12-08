#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle
from file_access import FileAccess
from graphics import Graphics
from confirm_location_removal_logic import ConfirmLocationRemovalLogic
from list_of_locations_view import ListOfLocationsView


class ConfirmLocationRemovalView(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):

        location_to_delete = self.controller.get_page("ListOfLocationsView").location_to_delete

        tk.Label(self, text="USUNĄĆ {}?".format(location_to_delete.upper()),font='Arial 15 bold', width=60, height=5, relief='groove').grid(row=1, column=1)

        Graphics.empty_row(self, 2, 1)

        Graphics.warning(self, "Cała zawartość magazynu zostanie usunięta.", 3, 1)

        ConfirmLocationRemovalLogic.button_delete_location(self, "Usuń", location_to_delete, 8)

        ConfirmLocationRemovalLogic.button_go_back(self, "Wróć", 9)
