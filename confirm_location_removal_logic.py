#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
from file_access import FileAccess
from graphics import Graphics


class ConfirmLocationRemovalLogic(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

    def remove_location(self, input_location, output_list):
        output_list.pop(input_location.lower())
        FileAccess.save_item_location_data(self, output_list)
        self.controller.show_frame("ListOfLocationsView")

    def button_delete_location(self, text, user_input, row):
        Graphics.button(self, text, lambda: ConfirmLocationRemovalLogic.remove_location(self, user_input,
                                                                       FileAccess.load_item_location_data(self)),
                        row)

    def button_go_back(self, text, row):
        Graphics.button(self, text, lambda: self.controller.show_frame("ListOfLocationsView"), row)

