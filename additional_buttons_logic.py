#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
from graphics import Graphics
from file_access import FileAccess


class AdditionalButtonsLogic:

    chosen_location = ''
    chosen_item = ''
    caller = ''
    called = False

    def __init__(self, controller):

        self.controller = controller

    ####################################################################################################################

    # ListOfItemsLogic

    def print_buttons(self, key, item):

        Graphics.small_title_label(self, 'OPCJE')

        the_input_quantity = tk.Entry(self, width=3)
        the_input_quantity.grid(row=3, column=0)

        AdditionalButtonsLogic.display_items_operations_button(
            self, "+",
            lambda: AdditionalButtonsLogic.add_quantity_to_available(
                self, key, item, the_input_quantity), 3, 1)

        AdditionalButtonsLogic.display_items_operations_button(
            self, "-",
            lambda: AdditionalButtonsLogic.subtract_quantity_from_available(
                self, key, item, the_input_quantity), 3, 2)

        AdditionalButtonsLogic.display_items_operations_button_2(
            self, "Zarezerwuj",
            lambda: AdditionalButtonsLogic.reserve_quantity(
                self, key, item, the_input_quantity), 3, 3)

        Graphics.delete_item_button(
            self, "Usuń przedmiot",
            lambda: AdditionalButtonsLogic.delete_item(self, key, item))

        AdditionalButtonsLogic.display_reservations(self, key, item)

    def display_reservations(self, key, item):

        Graphics.reservations_label(self, "Rezerwacje:")
        reserved_row = 6

        for user in FileAccess.load_users_and_passwords_data(self).keys():
            reservation_data = FileAccess.load_obj(self, user)
            if key in reservation_data.keys():
                if item in reservation_data[key]:
                    reserved = int(reservation_data[key][item])
                    Graphics.reservation_label(
                        self, user, reserved, reserved_row)
                    reserved_row += 1

    def display_items_operations_button(self, text, command, row, col):
        Graphics.items_operations_button(self, text, command, row, col)

    def display_items_operations_button_2(self, text, command, row, col):
        Graphics.items_operations_button_2(self, text, command, row, col)

    def add_quantity_to_available(self, user_location,
                                  user_item, user_quantity):

        quantity = user_quantity.get()

        if quantity.isdecimal():
            output_list = FileAccess.load_item_location_data(self)
            output_list[user_location.lower()][user_item] = str(
                int(quantity)
                + int(output_list[user_location.lower()][user_item]))
            FileAccess.save_item_location_data(self, output_list)

            AdditionalButtonsLogic.called = True
            self.controller.show_frame("ListOfItemsView")

    def subtract_quantity_from_available(self, user_location,
                                         user_item, user_quantity):

        quantity = user_quantity.get()

        if quantity.isdecimal():
            output_list = FileAccess.load_item_location_data(self)

            if int(output_list[user_location.lower()][user_item]) \
                    - int(quantity) >= 0:
                output_list[user_location.lower()][user_item] = str(
                    int(output_list[user_location.lower()][user_item])
                    - int(quantity))
            else:
                output_list[user_location.lower()].pop(user_item)

            FileAccess.save_item_location_data(self, output_list)

            AdditionalButtonsLogic.called = True
            self.controller.show_frame("ListOfItemsView")

    def reserve_quantity(self, user_location, user_item, user_quantity):

        quantity = user_quantity.get()

        if quantity.isdecimal():
            private_list = FileAccess.load_user_data(self)

            if user_location.lower() not in private_list.keys():
                private_list[user_location.lower()] = {user_item: quantity}
            elif user_item not in private_list[user_location]:
                private_list[user_location.lower()][user_item] = quantity
            else:
                private_list[user_location.lower()][user_item] = str(
                    int(quantity)
                    + int(private_list[user_location.lower()][user_item]))

            FileAccess.save_user_data(self, private_list)

            AdditionalButtonsLogic.subtract_quantity_from_available(
                self, user_location, user_item, user_quantity)

    def delete_item(self, user_location, user_item):

        output_list = FileAccess.load_item_location_data(self)
        output_list[user_location.lower()].pop(user_item)
        FileAccess.save_item_location_data(self, output_list)

        for user in FileAccess.load_users_and_passwords_data(self).keys():
            reservation_data = FileAccess.load_obj(self, user)
            if user_location in reservation_data.keys():
                if user_item in reservation_data[user_location]:
                    reservation_data[user_location.lower()].pop(user_item)
            FileAccess.save_obj(self, reservation_data, user)

        AdditionalButtonsLogic.called = True
        self.controller.show_frame("ListOfItemsView")

########################################################################################################################

    # ItemsSearchResultsLogic

    def print_buttons_search(self, location, item):

        Graphics.small_title_label(self, 'OPCJE')

        the_input_quantity = tk.Entry(self, width=3)
        the_input_quantity.grid(row=3, column=0)

        AdditionalButtonsLogic.display_items_operations_button(
            self, "+", lambda: AdditionalButtonsLogic.add_quantity_search(
                self, location, item, the_input_quantity), 3, 1)

        AdditionalButtonsLogic.display_items_operations_button(
            self, "-", lambda: AdditionalButtonsLogic.subtract_quantity_search(
                self, location, item, the_input_quantity), 3, 2)

        AdditionalButtonsLogic.display_items_operations_button_2(
            self, "Zarezerwuj",
            lambda: AdditionalButtonsLogic.reserve_quantity_search(
                self, location, item, the_input_quantity), 3, 3)

        Graphics.delete_item_button(
            self, "Usuń przedmiot",
            lambda: AdditionalButtonsLogic.delete_item(self, location, item))

    def add_quantity_search(self, user_location, user_item, user_quantity):

        quantity = user_quantity.get()
        if quantity.isdecimal():
            output_list = FileAccess.load_item_location_data(self)
            output_list[user_location.lower()][user_item] = str(
                int(quantity)
                + int(output_list[user_location.lower()][user_item]))
            FileAccess.save_item_location_data(self, output_list)
            self.controller.show_frame("ItemsSearchResultsView")

    def subtract_quantity_search(self, user_location,
                                 user_item, user_quantity):

        quantity = user_quantity.get()
        if quantity.isdecimal():
            output_list = FileAccess.load_item_location_data(self)

            if int(output_list[user_location.lower()][user_item]) \
                    - int(quantity) > 0:
                output_list[user_location.lower()][user_item] = str(
                    int(output_list[user_location.lower()][user_item])
                    - int(quantity))
            else:
                output_list[user_location.lower()].pop(user_item)

            FileAccess.save_item_location_data(self, output_list)
            self.controller.show_frame("ItemsSearchResultsView")

    def reserve_quantity_search(self, user_location, user_item, user_quantity):

        quantity = user_quantity.get()
        if quantity.isdecimal():
            private_list = FileAccess.load_user_data(self)

            if user_location.lower() not in private_list.keys():
                private_list[user_location.lower()] = {user_item: quantity}
            elif user_item not in private_list[user_location]:
                private_list[user_location.lower()][user_item] = quantity
            else:
                private_list[user_location.lower()][user_item] = str(
                    int(quantity)
                    + int(private_list[user_location.lower()][user_item]))

            FileAccess.save_user_data(self, private_list)
            AdditionalButtonsLogic.subtract_quantity_search(
                self, user_location, user_item, user_quantity)
            self.controller.show_frame("ItemsSearchResultsView")

    def delete_item_search(self, user_location, user_item):

        output_list = FileAccess.load_item_location_data(self)
        output_list[user_location.lower()].pop(user_item)
        FileAccess.save_item_location_data(self, output_list)

        for user in FileAccess.load_users_and_passwords_data(self).keys():
            reservation_data = FileAccess.load_user_data(self)
            if user_location in reservation_data.keys():
                if user_item in reservation_data[user_location]:
                    reservation_data[user_location.lower()].pop(user_item)
            FileAccess.save_user_data(self, reservation_data)
            self.controller.show_frame("ItemsSearchResultsView")

########################################################################################################################

    # UsersReservationsListLogic

    def print_buttons_private(self, key, item):

        Graphics.small_title_label(self, 'Zmiana ilości')

        the_input_quantity = tk.Entry(self, width=3)
        the_input_quantity.grid(row=3, column=0)

        AdditionalButtonsLogic.display_items_operations_button(
            self, "Odłóż",
            lambda: AdditionalButtonsLogic.undo_reserve_quantity(
                self, key, item, the_input_quantity), 3, 1)

        AdditionalButtonsLogic.display_items_operations_button_2(
            self, "Zabierz", lambda: AdditionalButtonsLogic.use_some(
                self, key, item, the_input_quantity), 3,2)

        AdditionalButtonsLogic.display_items_operations_button_2(
            self, "Odłóż wszystkie",
            lambda: AdditionalButtonsLogic.undo_reserve(
                self, key, item), 3, 3)

        Graphics.delete_item_button(
            self, "Zabierz wszystkie",
            lambda: AdditionalButtonsLogic.use_all(self, key, item))

    def subtract_quantity(self, user_location, user_item, user_quantity):

        quantity = user_quantity.get()
        if quantity.isdecimal():
            output_list = FileAccess.load_user_data(self)

            if int(output_list[user_location.lower()][user_item]) \
                    - int(quantity) > 0:
                output_list[user_location.lower()][user_item] = str(
                    int(output_list[user_location.lower()][user_item])
                    - int(quantity))
            else:
                output_list[user_location.lower()].pop(user_item)
                if output_list[user_location] == {}:
                    output_list.pop(user_location)
                    AdditionalButtonsLogic.chosen_location = ''
            FileAccess.save_user_data(self, output_list)

            AdditionalButtonsLogic.called = True
            self.controller.show_frame("UsersReservationsListView")

    def use_some(self, user_location, user_item, user_quantity):

        quantity = user_quantity.get()
        print(quantity)

        if quantity.isdecimal():
            private_list = FileAccess.load_user_data(self)
            if int(private_list[user_location][user_item]) - int(quantity) > 0:
                private_list[user_location][user_item] = str(
                    int(private_list[user_location][user_item])
                    - int(quantity))
            else:
                private_list[user_location].pop(user_item)
                if private_list[user_location] == {}:
                    private_list.pop(user_location)
                    AdditionalButtonsLogic.chosen_location = ''
            FileAccess.save_user_data(self, private_list)

            AdditionalButtonsLogic.called = True
            self.controller.show_frame("UsersReservationsListView")

    def use_all(self, user_location, user_item):

        private_list = FileAccess.load_user_data(self)
        private_list[user_location].pop(user_item)
        if private_list[user_location] == {}:
            private_list.pop(user_location)
            AdditionalButtonsLogic.chosen_location = ''
        FileAccess.save_user_data(self, private_list)

        AdditionalButtonsLogic.called = True
        self.controller.show_frame("UsersReservationsListView")

    def undo_reserve_quantity(self, user_location, user_item, user_quantity):

        quantity = user_quantity.get()

        if quantity.isdecimal():
            private_list = FileAccess.load_user_data(self)
            global_list = FileAccess.load_item_location_data(self)

            if user_location.lower() not in global_list.keys():
                global_list[user_location.lower()] = {user_item: quantity}
            elif user_item not in global_list[user_location]:
                global_list[user_location.lower()][user_item] = quantity
            else:
                global_list[user_location.lower()][user_item] = str(
                    int(quantity)
                    + int(global_list[user_location.lower()][user_item]))

            FileAccess.save_user_data(self, private_list)
            FileAccess.save_item_location_data(self, global_list)
            AdditionalButtonsLogic.subtract_quantity(
                self, user_location, user_item, user_quantity)

    def undo_reserve(self, user_location, user_item):

        output_list = FileAccess.load_user_data(self)
        quantity = output_list[user_location.lower()][user_item]
        output_list[user_location.lower()].pop(user_item)
        if output_list[user_location] == {}:
            output_list.pop(user_location)
            AdditionalButtonsLogic.chosen_location = ''
        FileAccess.save_user_data(self, output_list)

        global_list = FileAccess.load_item_location_data(self)

        if user_location.lower() not in global_list.keys():
            global_list[user_location.lower()] = {user_item: quantity}
        elif user_item not in global_list[user_location]:
            global_list[user_location.lower()][user_item] = quantity
        else:
            global_list[user_location.lower()][user_item] = str(
                int(quantity)
                + int(global_list[user_location.lower()][user_item]))

        FileAccess.save_item_location_data(self, global_list)

        AdditionalButtonsLogic.called = True
        self.controller.show_frame("UsersReservationsListView")
