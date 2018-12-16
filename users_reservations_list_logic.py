#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
from file_access import FileAccess
from graphics import Graphics
from additional_buttons_logic import AdditionalButtonsLogic


class UsersReservationsListLogic(tk.Frame):

    last_chosen_item = ''
    last_chosen_location = ''

    locations_row = 3
    items_row = 3
    main_row = 3
    row = 3
    location_chosen = False

    available = 0
    reserved = 0

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

    def display_location_name_button(self, location):

        if location == UsersReservationsListLogic.last_chosen_location:
            Graphics.location_name_button_colored(self, location.upper(),
                                        lambda: UsersReservationsListLogic.choose_location(self, location), UsersReservationsListLogic.locations_row)
            UsersReservationsListLogic.last_chosen_location = location
            UsersReservationsListLogic.locations_row += 2
        else:
            Graphics.location_name_button(self, location.upper(),
                                        lambda: UsersReservationsListLogic.choose_location(self, location), UsersReservationsListLogic.locations_row)
            UsersReservationsListLogic.locations_row += 2

    def choose_location(self, location):

        UsersReservationsListLogic.last_chosen_location = location
        UsersReservationsListLogic.location_chosen = True
        self.controller.show_frame("UsersReservationsListView")

    def display_items_buttons(self):

        location = UsersReservationsListLogic.last_chosen_location
        UsersReservationsListLogic.location_chosen = False
        row = UsersReservationsListLogic.row

        item_location_data = FileAccess.load_user_data(self)

        UsersReservationsListLogic.row = 3

        for item, available_quantity in item_location_data[location].items():
            UsersReservationsListLogic.calculate(self, item, location)

            UsersReservationsListLogic.display_item_name_button(self, item, location)

        Graphics.empty_row(self, row, 1)

    def display_item_name_button(self, item, location):

        row = UsersReservationsListLogic.row
        reserved_quantity = UsersReservationsListLogic.reserved
        available_quantity = UsersReservationsListLogic.available

        if item == UsersReservationsListLogic.last_chosen_item:
            Graphics.reserved_item_name_button_colored(self, item, reserved_quantity, available_quantity,
                                                   lambda: UsersReservationsListLogic.display_item_options_buttons(self, item, location), row)
            UsersReservationsListLogic.last_chosen_item = ''
            UsersReservationsListLogic.row += 1

        else:
            Graphics.reserved_item_name_button(self, item, reserved_quantity, available_quantity,
                                                   lambda: UsersReservationsListLogic.display_item_options_buttons(self, item, location), row)
            UsersReservationsListLogic.row += 1

    def display_item_options_buttons(self, item, location):

        AdditionalButtonsLogic.chosen_item = item
        AdditionalButtonsLogic.chosen_location = location
        UsersReservationsListLogic.last_chosen_item = item
        UsersReservationsListLogic.choose_location(self, location)

        AdditionalButtonsLogic.caller = "UsersReservationsListLogic"
        self.controller.show_frame("AdditionalButtonsView")

    def calculate(self, item, location):

        reservation_data = FileAccess.load_user_data(self)
        UsersReservationsListLogic.reserved = int(reservation_data[location][item])

        item_location_data = FileAccess.load_item_location_data(self)
        UsersReservationsListLogic.available = int(item_location_data[location][item])
