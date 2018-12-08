#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle
from file_access import FileAccess
from graphics import Graphics
from additional_buttons_view import AdditionalButtonsView
from additional_buttons_logic import AdditionalButtonsLogic
from search_for_items_logic import SearchForItemsLogic


class ItemsSearchResultsLogic(tk.Frame):

    last_chosen_item = ''
    last_chosen_location = ''
    item_row = 3
    location_row = 3

    reserved = 0
    reserved_and_available = 0
    available = 0

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

    def select_search_result(self, item, location):

        ItemsSearchResultsLogic.last_chosen_item = item
        ItemsSearchResultsLogic.last_chosen_location = location
        self.controller.show_frame("ItemsSearchResultsView")

        AdditionalButtonsLogic.chosen_item = item
        AdditionalButtonsLogic.chosen_location = location
        AdditionalButtonsLogic.caller = "ItemsSearchResultsLogic"
        self.controller.show_frame("AdditionalButtonsView")

    def calculate(self, item, location):

        item_location_data = FileAccess.load_item_location_data(self)

        ItemsSearchResultsLogic.reserved = 0
        ItemsSearchResultsLogic.available = int(item_location_data[location][item])
        ItemsSearchResultsLogic.reserved_and_available = ItemsSearchResultsLogic.available

        for user in FileAccess.load_obj(self, 'users').keys():
            users_reservations = FileAccess.load_obj(self, user)
            if location in users_reservations.keys():
                if item in users_reservations[location]:
                    ItemsSearchResultsLogic.reserved_and_available += int(users_reservations[location][item])

        ItemsSearchResultsLogic.reserved = ItemsSearchResultsLogic.reserved_and_available - int(item_location_data[location][item])

    def display_item_name_button(self, item, location):

        row = ItemsSearchResultsLogic.item_row
        full_quantity = ItemsSearchResultsLogic.reserved_and_available
        reserved_quantity = ItemsSearchResultsLogic.reserved
        available_quantity = ItemsSearchResultsLogic.available

        if item == ItemsSearchResultsLogic.last_chosen_item and location == ItemsSearchResultsLogic.last_chosen_location:
            Graphics.item_name_button_colored(self, item, available_quantity, full_quantity, reserved_quantity,
                                              lambda: ItemsSearchResultsLogic.select_search_result(self, item,
                                                                                                    location), row)

            ItemsSearchResultsLogic.last_chosen_item = ''
            ItemsSearchResultsLogic.item_row += 1

        else:
            Graphics.item_name_button(self, item, available_quantity, full_quantity, reserved_quantity,
                                      lambda: ItemsSearchResultsLogic.select_search_result(self, item, location),
                                      row)

            ItemsSearchResultsLogic.item_row += 1

    def display_results(self):

        item = SearchForItemsLogic.item_to_find
        data = FileAccess.load_item_location_data(self)

        for location in data.keys():

            for listed_item in data[location].keys():

                if item in listed_item:
                    ItemsSearchResultsLogic.calculate(self, listed_item, location)

                    Graphics.login_label(self, location, ItemsSearchResultsLogic.location_row, 0)
                    ItemsSearchResultsLogic.location_row += 1

                    ItemsSearchResultsLogic.display_item_name_button(self, listed_item, location)

