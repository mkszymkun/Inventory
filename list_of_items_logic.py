#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
from file_access import FileAccess
from graphics import Graphics
from additional_buttons_logic import AdditionalButtonsLogic


class ListOfItemsLogic:

    last_chosen_item = ''
    last_chosen_location = ''
    locations_row = 3
    row = 3
    location_chosen = False

    available = 0
    reserved = 0
    reserved_and_available = 0

    def __init__(self, controller):

        self.controller = controller

    def display_location_name_button(self, location):

        if location == ListOfItemsLogic.last_chosen_location:
            Graphics.location_name_button_colored(
                self, location.upper(),
                lambda: ListOfItemsLogic.choose_location(self, location),
                ListOfItemsLogic.locations_row)
            ListOfItemsLogic.last_chosen_location = location
            ListOfItemsLogic.locations_row += 2
        else:
            Graphics.location_name_button(
                self, location.upper(),
                lambda: ListOfItemsLogic.choose_location(self, location),
                ListOfItemsLogic.locations_row)
            ListOfItemsLogic.locations_row += 2

    def choose_location(self, location):

        ListOfItemsLogic.last_chosen_location = location
        ListOfItemsLogic.location_chosen = True
        self.controller.show_frame("ListOfItemsView")

    def display_items_buttons(self):

        location = ListOfItemsLogic.last_chosen_location
        ListOfItemsLogic.location_chosen = False
        row = ListOfItemsLogic.row

        item_location_data = FileAccess.load_item_location_data(self)

        ListOfItemsLogic.row = 3

        for item, available_quantity in item_location_data[location].items():
            ListOfItemsLogic.calculate(self, item, location)

            ListOfItemsLogic.display_item_name_button(self, item, location)

        Graphics.empty_row(self, row, 1)

        row += 1

        ListOfItemsLogic.display_new_item_buttons(self, location)

    def display_item_name_button(self, item, location):

        row = ListOfItemsLogic.row
        full_quantity = ListOfItemsLogic.reserved_and_available
        reserved_quantity = ListOfItemsLogic.reserved
        available_quantity = ListOfItemsLogic.available

        if item == ListOfItemsLogic.last_chosen_item:
            Graphics.item_name_button_colored(
                self, item, available_quantity,
                full_quantity, reserved_quantity,
                lambda: ListOfItemsLogic.display_item_options_buttons(
                    self, item, location), row)

            ListOfItemsLogic.last_chosen_item = ''
            ListOfItemsLogic.row += 1

        else:
            Graphics.item_name_button(
                self, item, available_quantity,
                full_quantity, reserved_quantity,
                lambda: ListOfItemsLogic.display_item_options_buttons(
                    self, item, location), row)

            ListOfItemsLogic.row += 1

    def display_item_options_buttons(self, item, location):

        AdditionalButtonsLogic.chosen_item = item
        AdditionalButtonsLogic.chosen_location = location
        ListOfItemsLogic.last_chosen_item = item
        ListOfItemsLogic.choose_location(self, location)

        AdditionalButtonsLogic.caller = "ListOfItemsLogic"
        self.controller.show_frame("AdditionalButtonsView")

    def calculate(self, item, location):

        item_location_data = FileAccess.load_item_location_data(self)

        ListOfItemsLogic.reserved = 0
        ListOfItemsLogic.available = int(item_location_data[location][item])
        ListOfItemsLogic.reserved_and_available = ListOfItemsLogic.available

        for user in FileAccess.load_obj(self, 'users').keys():
            users_reservations = FileAccess.load_obj(self, user)
            if location in users_reservations.keys():
                if item in users_reservations[location]:
                    ListOfItemsLogic.reserved_and_available \
                        += int(users_reservations[location][item])

        ListOfItemsLogic.reserved = ListOfItemsLogic.reserved_and_available \
                                    - int(item_location_data[location][item])

    def display_new_item_buttons(self, key):

        Graphics.adding_new_item_label(self, "Nazwa:",
                                       ListOfItemsLogic.locations_row, 1)
        Graphics.adding_new_item_label_2(self, "Ilość:",
                                       ListOfItemsLogic.locations_row, 2)

        the_input_item = tk.Entry(self, width=25)
        the_input_item.grid(row=ListOfItemsLogic.locations_row + 1,
                            column=1, sticky='w')

        the_input_quantity = tk.Entry(self, width=5)
        the_input_quantity.grid(row=ListOfItemsLogic.locations_row + 1,
                                column=2)

        Graphics.adding_new_item_button(
            self, "Dodaj nowy",
            lambda: ListOfItemsLogic.add_item(
                self, key, the_input_item, the_input_quantity),
            ListOfItemsLogic.locations_row + 1)

    def add_item(self, user_location, user_item, user_quantity):

        quantity = user_quantity.get()

        if quantity.isdecimal():
            output_list = FileAccess.load_item_location_data(self)
            output_list[user_location.lower()][user_item.get()] = quantity
            FileAccess.save_item_location_data(self, output_list)

            self.controller.show_frame("ListOfItemsView")
            ListOfItemsLogic.choose_location(self, user_location)
