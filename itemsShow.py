#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle


class ItemsShow(tk.Frame):

    last_value = ''
    last_key = ''

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):

        def save_obj(obj, name):
            with open(name + '.pkl', 'wb') as f:
                pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

        def load_obj(name):
            with open(name + '.pkl', 'rb') as f:
                return pickle.load(f)

        def header(text):
            tk.Label(self, text=text, font='Arial 15 bold', width=60, height=5,
                     relief='groove').grid(row=1, column=0, columnspan=7)

        def empty_row(row, col):
            tk.Label(self).grid(row=row, column=col)

        def label(text, row, col):
            tk.Label(self, text=text, font='Arial 10', width=20, height=2, relief='groove').grid(row=row,
                                                                                                     column=col)

        def choose_location(key):

            self.last_key = key
            row = 2
            
            data = load_obj('item_location_data')

            self.controller.show_frame("ItemsShow")

            row += 1

            for k, v in data[key].items():

                reserved = 0
                reserved_and_available = int(data[key][k])
                for user in load_obj('users').keys():
                    reservation_data = load_obj(user)
                    if key in reservation_data.keys():
                        if k in reservation_data[key]:
                            reserved_and_available += int(reservation_data[key][k])
                reserved = reserved_and_available - int(data[key][k])

                if k == self.last_value:
                    label_item_quantity = tk.Button(self, text = "{}  -  {} / {}  ({})".format(k, v, reserved_and_available, reserved), width = 25, relief='groove', bg='blue',
                                command=lambda i=row, j=k: print_buttons(i, key, j)).grid(row=row, column=2, sticky='w')
                    self.last_value = ''
                    row += 1
                else:
                    label_item_quantity = tk.Button(self, text = "{}  -  {} / {}  ({})".format(k, v, reserved_and_available, reserved), width = 25, relief='groove',
                                command=lambda i=row, j=k: print_buttons(i, key, j)).grid(row=row, column=2, sticky='w')
                    row += 1

            empty_row(row, 1)

            row += 1

            label_item = tk.Label(self, text = "Nazwa:").grid(row=main_row,column=2)
            label_quantity = tk.Label(self, text = "Ilość:").grid(row=main_row,column=3)

            row += 1
            the_input_item = tk.Entry(self, width=25)
            the_input_item.grid(row=main_row+1,column=2, sticky='w')
            the_input_quantity = tk.Entry(self, width=5)
            the_input_quantity.grid(row=main_row+1,column=3)
            label_add_item = tk.Button(self, text = "Dodaj nowy", relief='groove',
                        command=lambda: add_item(key, the_input_item, the_input_quantity)).grid(row=main_row+1,column=4,columnspan=3, sticky='w')

        def print_buttons(row, key, item):

            self.last_value = item

            self.controller.show_frame("ItemsShow")
            choose_location(key)

            label_header = tk.Label(self, text = 'Zmiana ilości', font="Arial 10", width=30, relief='groove').grid(row=2,column=3,columnspan=4)

            the_input_quantity = tk.Entry(self, width=3)
            the_input_quantity.grid(row=3,column=3)
            label_add = tk.Button(self, text = "+", relief='groove',
                        command=lambda: add_quantity(key, item, the_input_quantity)).grid(row=3,column=4)
            the_input_remove = tk.Entry(self, width=3)
            label_subtract = tk.Button(self, text = "-", relief='groove',
                        command=lambda: subtract_quantity(key, item, the_input_quantity)).grid(row=3,column=5)
            label_reserve = tk.Button(self, text="Zarezerwuj", relief='groove',
                                     command=lambda: reserve_quantity(key, item, the_input_quantity)).grid(row=3,
                                                                                                             column=6)
            label_delete = tk.Button(self, text="Usuń przedmiot", relief='groove', width=20,
                                      command=lambda: delete_item(key, item)).grid(
                row=4,
                column=3, columnspan=4)

            label_reservations = tk.Label(self, text="Rezerwacje:").grid(row=5, column=3, columnspan=4)
            reserved_row = 6

            for user in load_obj('users').keys():
                reservation_data = load_obj(user)
                if key in reservation_data.keys():
                    if item in reservation_data[key]:
                        reserved = int(reservation_data[key][item])
                        label_reserved = tk.Label(self, text = "{} - {}".format(user, reserved)).grid(row=reserved_row, column=3, columnspan=4)
                        reserved_row += 1

        def add_item(user_location, user_item, user_quantity):

            quantity = user_quantity.get()
            if quantity.isdecimal():
                output_list = load_obj('item_location_data')
                output_list[user_location.lower()][user_item.get()] = quantity
                save_obj(output_list, 'item_location_data')
                self.controller.show_frame("ItemsShow")
                choose_location(user_location)

        def add_quantity(user_location, user_item, user_quantity):

            quantity = user_quantity.get()
            if quantity.isdecimal():
                output_list = load_obj('item_location_data')
                output_list[user_location.lower()][user_item] = str(int(quantity) + int(output_list[user_location.lower()][user_item]))
                save_obj(output_list, 'item_location_data')
                self.controller.show_frame("ItemsShow")
                choose_location(user_location)

        def subtract_quantity(user_location, user_item, user_quantity):

            quantity = user_quantity.get()
            if quantity.isdecimal():
                output_list = load_obj('item_location_data')

                if int(output_list[user_location.lower()][user_item]) - int(quantity) >= 0:
                    output_list[user_location.lower()][user_item] = str(int(output_list[user_location.lower()][user_item]) - int(quantity))
                else:
                    output_list[user_location.lower()].pop(user_item)

                save_obj(output_list, 'item_location_data')
                self.controller.show_frame("ItemsShow")
                choose_location(user_location)

        def reserve_quantity(user_location, user_item, user_quantity):

            quantity = user_quantity.get()
            if quantity.isdecimal():
                private_list = load_obj(username)

                if user_location.lower() not in private_list.keys():
                    private_list[user_location.lower()] = {user_item:quantity}
                elif user_item not in private_list[user_location]:
                    private_list[user_location.lower()][user_item] = quantity
                else:
                    private_list[user_location.lower()][user_item] = str(
                        int(quantity) + int(private_list[user_location.lower()][user_item]))

                save_obj(private_list, username)
                subtract_quantity(user_location, user_item, user_quantity)

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

            self.controller.show_frame("ItemsShow")
            choose_location(user_location)

        for widget in self.winfo_children():
            widget.destroy()

        row = 3
        main_row = 3

        data = load_obj('item_location_data')

        username = self.controller.get_page("Login").username

        label_username = tk.Label(self, text='Logged in as: {}'.format(username)).grid(row=0, column=0, sticky='w')

        header("LISTA MATERIAŁÓW")
        empty_row(2, 1)

        for key in data.keys():
            if key == self.last_key:
                label0 = tk.Button(self, text = key.upper(), width=20, height=3, relief='groove', bg='blue',
                                    command=lambda i=key: choose_location(i)).grid(row=main_row, column=0, rowspan=2, sticky='w')
                self.last_key = key
                main_row += 2
            else:
                label0 = tk.Button(self, text = key.upper(), width=20, height=3, relief='groove',
                                    command=lambda i=key: choose_location(i)).grid(row=main_row, column=0, rowspan=2, sticky='w')
                main_row += 2

        empty_row(19, 1)

        button_back = tk.Button(self, text="Wróć", width=30, height=3, relief='groove',
                        command=lambda: self.controller.show_frame("MainMenu")).grid(row=20, column=0, columnspan=7)
