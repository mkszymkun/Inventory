#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle
from file_access import FileAccess
from graphics import Graphics
from confirm_location_removal_logic import ConfirmLocationRemovalLogic


class ListOfLocationsLogic(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

    def add_location(self, input_location, output_list):
        output_list[input_location.lower()] = {}
        FileAccess.save_item_location_data(self, output_list)
        self.controller.show_frame("ListOfLocationsView")

    def display_location_delete_button(self, location, row):
        Graphics.location_delete_button(self, lambda: ListOfLocationsLogic.confirm_location_removal(self, location), row)

    def display_add_location_button(self, location_to_add, row):
        Graphics.add_location_button(self,
                lambda: ListOfLocationsLogic.add_location(self, location_to_add.get(), FileAccess.load_item_location_data(self)), row)

    def confirm_location_removal(self, location):
        self.location_to_delete = location
        self.controller.show_frame("ConfirmLocationRemovalView")
