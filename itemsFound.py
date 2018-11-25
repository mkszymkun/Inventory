#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle


class ItemsFound(tk.Frame):

    last_selected_item = ''
    last_selected_location = ''

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):

        def empty_row(row, col):
            tk.Label(self).grid(row=row, column=col)

        def save_obj(obj, name):
            with open(name + '.pkl', 'wb') as f:
                pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

        def load_obj(name):
            with open(name + '.pkl', 'rb') as f:
                return pickle.load(f)

        def select_search_result(location, item):

            self.last_selected_item = item
            self.last_selected_location = location
            self.controller.show_frame("ItemsFound")
            print_buttons(buttons_row, location, item)

        def print_buttons(row, key, item):

            label_header = tk.Label(self, text = 'Zmiana ilości', font="Arial 10", width=30, relief='groove').grid(row=row,column=0,columnspan=4)

            the_input_quantity = tk.Entry(self, width=3)
            the_input_quantity.grid(row=row+1,column=0)
            label_add = tk.Button(self, text = "+", relief='groove',
                        command=lambda: add_quantity(key, item, the_input_quantity)).grid(row=row+1,column=1)
            the_input_remove = tk.Entry(self, width=3)
            label_subtract = tk.Button(self, text = "-", relief='groove',
                        command=lambda: subtract_quantity(key, item, the_input_quantity)).grid(row=row+1,column=2)
            label_reserve = tk.Button(self, text="Zarezerwuj", relief='groove',
                                     command=lambda: reserve_quantity(key, item, the_input_quantity)).grid(row=row+1,
                                                                                                             column=3)
            label_delete = tk.Button(self, text="Usuń przedmiot", relief='groove', width=20,
                                      command=lambda: delete_item(key, item)).grid(
                row=row+2,
                column=0, columnspan=4)

        def add_quantity(user_location, user_item, user_quantity):

            quantity = user_quantity.get()
            if quantity.isdecimal():
                output_list = load_obj('item_location_data')
                output_list[user_location.lower()][user_item] = str(int(quantity) + int(output_list[user_location.lower()][user_item]))
                save_obj(output_list, 'item_location_data')
                self.controller.show_frame("ItemsFound")

        def subtract_quantity(user_location, user_item, user_quantity):

            quantity = user_quantity.get()
            if quantity.isdecimal():
                output_list = load_obj('item_location_data')

                if int(output_list[user_location.lower()][user_item]) - int(quantity) > 0:
                    output_list[user_location.lower()][user_item] = str(
                        int(output_list[user_location.lower()][user_item]) - int(quantity))
                else:
                    output_list[user_location.lower()].pop(user_item)

                save_obj(output_list, 'item_location_data')
                self.controller.show_frame("ItemsFound")

        def reserve_quantity(user_location, user_item, user_quantity):

            quantity = user_quantity.get()
            if quantity.isdecimal():
                private_list = load_obj(username)

                if user_location.lower() not in private_list.keys():
                    private_list[user_location.lower()] = {user_item: quantity}
                elif user_item not in private_list[user_location]:
                    private_list[user_location.lower()][user_item] = quantity
                else:
                    private_list[user_location.lower()][user_item] = str(
                        int(quantity) + int(private_list[user_location.lower()][user_item]))

                save_obj(private_list, username)
                subtract_quantity(user_location, user_item, user_quantity)
                self.controller.show_frame("ItemsFound")

        def delete_item(user_location, user_item):

            output_list = load_obj('item_location_data')
            output_list[user_location.lower()].pop(user_item)
            save_obj(output_list, 'item_location_data')

            for user in load_obj('users').keys():
                reservation_data = load_obj(user)
                if user_location in reservation_data.keys():
                    if user_item in reservation_data[user_location]:
                        reservation_data[user_location.lower()].pop(user_item)
                save_obj(reservation_data, user)
                self.controller.show_frame("ItemsFound")

        for widget in self.winfo_children():
            widget.destroy()

        item = self.controller.get_page("ItemsSearch").item_to_find

        column = 0

        main_row = 3

        data = load_obj('item_location_data')

        for location in data.keys():

            items_count = 0

            row = 5

            for listed_item in data[location].keys():

                if item in listed_item:
                    reserved = 0
                    reserved_and_available = int(data[location][listed_item])
                    quantity_all = reserved_and_available

                    for user in load_obj('users').keys():
                        reservation_data = load_obj(user)
                        if location in reservation_data.keys():
                            if listed_item in reservation_data[location]:
                                reserved_and_available += int(reservation_data[location][listed_item])

                    reserved = reserved_and_available - int(data[location][listed_item])

                    if self.last_selected_item == listed_item and self.last_selected_location == location:

                        label_item = tk.Button(self, text="{}  -  {} / {}  ({})".format(listed_item, quantity_all, reserved_and_available, reserved),
                                    relief='groove', width=18, bg='blue', command=lambda i=location, j=listed_item: select_search_result(i, j)).grid(row=row, column=column)
                        row += 1
                        main_row = row
                        items_count += 1

                    else:
                        label_item = tk.Button(self, text="{}  -  {} / {}  ({})".format(listed_item, quantity_all,
                                                                                        reserved_and_available,
                                                                                        reserved),
                                               relief='groove', width=18,
                                               command=lambda i=location, j=listed_item: select_search_result(i,
                                                                                                              j)).grid(
                            row=row, column=column)
                        row += 1
                        main_row = row
                        items_count += 1
            if items_count > 0:
                label_location = tk.Label(self, text=location.upper(), relief='groove', width=20).grid(row=3, column=column)
                label_empty_row = tk.Label(self).grid(row=4, column=1)

            column += 1

        username = self.controller.get_page("Login").username

        label_username = tk.Label(self, text='Logged in as: {}'.format(username)).grid(row=0, column=0, sticky='w')

        label_header = tk.Label(self, text="WYNIKI DLA \"{}\"".format(item), font='Arial 15 bold', width=60, height=5,
                                relief='groove').grid(row=1, column=0, columnspan=column)

        empty_row(2, 1)
        buttons_row = main_row + 1

        for i in range(main_row, main_row + 5):
            empty_row(i, 1)

        button_back = tk.Button(self, text="Wróć", width=30, height=3, relief='groove',
                                command=lambda: self.controller.show_frame("MainMenu")).grid(row=main_row+5, column=0,
                                                                                           columnspan=column)

