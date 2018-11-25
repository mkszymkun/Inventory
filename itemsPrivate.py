#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle


class ItemsPrivate(tk.Frame):

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

        for widget in self.winfo_children():
            widget.destroy()

        username = self.controller.get_page("Login").username

        main_row = 3
        data = load_obj(username)

        label_username = tk.Label(self, text='Logged in as: {}'.format(username)).grid(row=0, column=0, sticky='w')

        label_header = tk.Label(self, text="MOJE REZERWACJE", font='Arial 15 bold', width=60, height=5,
                                relief='groove').grid(row=1, column=0, columnspan=7)
        label_empty_row = tk.Label(self).grid(row=2, column=1)

        def choose_location(key):

            self.last_key = key
            row = 2

            data = load_obj(username)

            self.controller.show_frame("ItemsPrivate")

            row += 1

            label_empty_row = tk.Label(self).grid(row=row,column=1)

            for k, v in data[key].items():

                data_all = load_obj('item_location_data')
                available = 0
                if key in data_all.keys():
                    if k in data_all[key]:
                        available = int(data_all[key][k])

                if k == self.last_value:

                    label_item_quantity = tk.Button(self, text="{}  -  {} szt. ({})".format(k, v, available), width=25, relief='groove',
                                                    bg='blue',
                                                    command=lambda i=row, j=k: print_buttons(i, key, j)).grid(row=row,
                                                                                                             column=2,
                                                                                                             sticky='w')
                    self.last_value = ''
                    row += 1
                else:
                    label_item_quantity = tk.Button(self, text="{}  -  {} szt. ({})".format(k, v, available), width=25, relief='groove',
                                                    command=lambda i=row, j=k: print_buttons(i, key, j)).grid(row=row,
                                                                                                             column=2,
                                                                                                             sticky='w')
                    row += 1

            label_empty_row = tk.Label(self).grid(row=row, column=1)

            row += 1

        def print_buttons(row, key, item):

            self.last_value = item

            self.controller.show_frame("ItemsPrivate")
            choose_location(key)

            label_header = tk.Label(self, text='Zmiana ilości', font="Arial 10", width=30, relief='groove').grid(
                row=2, column=3, columnspan=4)

            the_input_quantity = tk.Entry(self, width=3)

            the_input_quantity.grid(row=3, column=3)

            label_undo_reserve_quantity = tk.Button(self, text="Odłóż", relief='groove', font="Arial 10", width=8,
                                      command=lambda: undo_reserve_quantity(key, item, the_input_quantity)).grid(
                row=3,
                column=4, columnspan=1)

            label_use_some = tk.Button(self, text="Zabierz", relief='groove', font="Arial 10", width=8,
                                      command=lambda: use_some(key, item,
                                                                                the_input_quantity)).grid(
                row=3,
                column=5, columnspan=2)

            label_undo_reserve = tk.Button(self, text="Odłóż wszystkie", relief='groove', width=20,
                                     command=lambda: undo_reserve(key, item)).grid(
                row=4,
                column=3, columnspan=4)

            label_use_all = tk.Button(self, text="Zabierz wszystkie", relief='groove', width=20,
                                     command=lambda: use_all(key, item)).grid(
                row=5,
                column=3, columnspan=4)

        def subtract_quantity(user_location, user_item, user_quantity):

            quantity = user_quantity.get()
            if quantity.isdecimal():
                output_list = load_obj(username)

                if int(output_list[user_location.lower()][user_item]) - int(quantity) > 0:
                    output_list[user_location.lower()][user_item] = str(
                        int(output_list[user_location.lower()][user_item]) - int(quantity))
                else:
                    output_list[user_location.lower()].pop(user_item)
                save_obj(output_list, username)

                self.controller.show_frame("ItemsPrivate")
                choose_location(user_location)

        def use_some(user_location, user_item, user_quantity):

            quantity = user_quantity.get()
            if quantity.isdecimal():
                private_list = load_obj(username)
                if int(private_list[user_location][user_item]) - int(quantity) > 0:
                    private_list[user_location][user_item] = str(int(private_list[user_location][user_item]) - int(quantity))
                else:
                    private_list[user_location].pop(user_item)
                save_obj(private_list, username)

                self.controller.show_frame("ItemsPrivate")
                choose_location(user_location)

        def use_all(user_location, user_item):

            private_list = load_obj(username)
            private_list[user_location].pop(user_item)
            save_obj(private_list, username)

            self.controller.show_frame("ItemsPrivate")
            choose_location(user_location)

        def undo_reserve_quantity(user_location, user_item, user_quantity):

            quantity = user_quantity.get()
            if quantity.isdecimal():
                private_list = load_obj(username)
                global_list = load_obj('item_location_data')

                if user_location.lower() not in global_list.keys():
                    global_list[user_location.lower()] = {user_item: quantity}
                elif user_item not in global_list[user_location]:
                    global_list[user_location.lower()][user_item] = quantity
                else:
                    global_list[user_location.lower()][user_item] = str(
                        int(quantity) + int(global_list[user_location.lower()][user_item]))

                save_obj(private_list, username)
                save_obj(global_list, 'item_location_data')
                subtract_quantity(user_location, user_item, user_quantity)

        def undo_reserve(user_location, user_item):

            output_list = load_obj(username)
            quantity = output_list[user_location.lower()][user_item]
            output_list[user_location.lower()].pop(user_item)
            save_obj(output_list, username)

            global_list = load_obj('item_location_data')

            if user_location.lower() not in global_list.keys():
                global_list[user_location.lower()] = {user_item: quantity}
            elif user_item not in global_list[user_location]:
                global_list[user_location.lower()][user_item] = quantity
            else:
                global_list[user_location.lower()][user_item] = str(
                    int(quantity) + int(global_list[user_location.lower()][user_item]))

            save_obj(global_list, 'item_location_data')
            self.controller.show_frame("ItemsPrivate")
            choose_location(user_location)

        for key in data.keys():
            if key == self.last_key:
                label0 = tk.Button(self, text=key.upper(), width=20, height=3, relief='groove', bg='blue',
                                   command=lambda i=key: choose_location(i)).grid(row=main_row, column=0, rowspan=2,
                                                                                 sticky='w')
                self.last_key = ''
                main_row += 2
            else:
                label0 = tk.Button(self, text=key.upper(), width=20, height=3, relief='groove',
                                   command=lambda i=key: choose_location(i)).grid(row=main_row, column=0, rowspan=2,
                                                                                 sticky='w')
                main_row += 2

        label_empty_row = tk.Label(self).grid(row=19, column=1)

        button_back = tk.Button(self, text="Wróć", width=30, height=3, relief='groove',
                                command=lambda: self.controller.show_frame("MainMenu")).grid(row=20, column=0,
                                                                                           columnspan=7)
