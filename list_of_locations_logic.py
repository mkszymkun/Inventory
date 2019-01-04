#!/usr/bin/python3

# Inventory - inventory management program

from file_access import FileAccess
from graphics import Graphics


class ListOfLocationsLogic:

    def __init__(self, controller):

        self.controller = controller

    def display_location_delete_button(self, location, row):
        Graphics.location_delete_button(
            self, lambda: ListOfLocationsLogic.confirm_location_removal(
                self, location), row)

    def confirm_location_removal(self, location):
        self.location_to_delete = location
        self.controller.show_frame("ConfirmLocationRemovalView")

    def display_add_location_button(self, location_to_add, row):
        Graphics.add_location_button(
            self, lambda: ListOfLocationsLogic.add_location(
                self, location_to_add.get(),
                FileAccess.load_item_location_data(self)), row)

    def add_location(self, input_location, output_list):
        output_list[input_location.lower()] = {}
        FileAccess.save_item_location_data(self, output_list)
        self.controller.show_frame("ListOfLocationsView")
