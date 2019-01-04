#!/usr/bin/python3

# Inventory - inventory management program

from file_access import FileAccess
from graphics import Graphics


class ConfirmLocationRemovalLogic:

    def __init__(self, controller):

        self.controller = controller

    def remove_location(self, input_location, output_list):
        FileAccess.remove_location(self, input_location, output_list)
        self.controller.show_frame("ListOfLocationsView")

    def button_delete_location(self, text, user_input, row):
        Graphics.button(
            self, text, lambda: ConfirmLocationRemovalLogic.remove_location(
                self, user_input,
                FileAccess.load_item_location_data(self)), row)

    def button_go_back(self, text, row):
        Graphics.button(
            self, text,
            lambda: self.controller.show_frame("ListOfLocationsView"), row)

