#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle, re

last_row = 0
user_input = ''
last_key = ''
last_value = ''
username = ''

# Function for saving a dictionary to a file

def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


# Function for loading a dictionary from a file

def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


# Creating a file containing a dictionary with data about locations and items if it doesn't exist

try:
    load_obj('item_location_data')
except:
    item_location_data = {}
    save_obj(item_location_data, 'item_location_data')

# Creating a file containing a dictionary with data about users and passwords if it doesn't exist

try:
    load_obj('users')
except:
    users = {}
    save_obj(users, 'users')


class Inventory(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self, width=100, height=100)
        
        container.pack(padx=5, pady=5, expand = True)

        container.grid_rowconfigure(3, weight=1)
        container.grid_columnconfigure(3, weight=1)

        self.frames = {}

        for F in (Login, Register, MainMenu, ItemsShow, LocationsShow, ItemsPrivate, LocationsConfirm):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=2, column=2, sticky="nsew")

        self.show_frame(Login)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.event_generate("<<ShowFrame>>")
        frame.tkraise()


class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.bind("<<ShowFrame>>", self.on_show_frame)

        global last_error_label

        label_empty_row = tk.Label(self).grid(row=0, column=1)

        label_header = tk.Label(self, text="LOGOWANIE", font='Arial 15 bold', width=60, height=5,
                                relief='groove').grid(row=1, column=0, columnspan=4)

        label_empty_row = tk.Label(self).grid(row=2, column=1)
        label_empty_col = tk.Label(self, width=8).grid(row=3, column=0)

        label_user = tk.Label(self, text="Login:", font='Arial 10', width=20, height=2, relief='groove').grid(row=3,
                                                                                                              column=1)
        input_user = tk.Entry(self)
        input_user.grid(row=3, column=2)

        label_empty_row = tk.Label(self).grid(row=4, column=1)

        label_pword = tk.Label(self, text="Hasło:", font='Arial 10', width=20, height=2, relief='groove').grid(row=5,
                                                                                                               column=1)

        input_pword = tk.Entry(self, show='*')
        input_pword.grid(row=5, column=2)

        last_error_label = tk.Label(self)
        last_error_label.grid(row=6, column=1)
        label_empty_row = tk.Label(self).grid(row=7, column=1)

        button_login = tk.Button(self, text="Zaloguj", font='Arial 10', width=30, height=4, relief='groove',
                                 command=lambda: log_in(input_user, input_pword)).grid(row=8, column=0, columnspan=4)

        button_register = tk.Button(self, text="Załóż konto", font='Arial 10', width=30, height=4, relief='groove',
                                    command=lambda: controller.show_frame(Register)).grid(row=9, column=0, columnspan=4)

        button_quit = tk.Button(self, text="Wyjście", font='Arial 10', width=30, height=4, relief='groove',
                                command=lambda: controller.destroy()).grid(row=10, column=0, columnspan=4)

        # Login function, checking if provided username is stored in the file alongside a matching password,
        # displays appropriate messages if something's wrong

        def log_in(input_user, input_password):

            def display_error(error_message):
                global last_error_label
                last_error_label.destroy()
                last_error_label = tk.Label(self, text=error_message)
                last_error_label.grid(row=6, column=2)

            global username

            provided_username = input_user.get()
            provided_password = input_password.get()

            data = load_obj('users')

            if provided_username in data.keys():
                if data[provided_username] == provided_password:
                    username = provided_username
                    controller.show_frame(MainMenu)
                else:
                    display_error("Błędne hasło")
            else:
                display_error("Użytkownik nie istnieje")

    def on_show_frame(self, event):

        global last_error_label
        last_error_label.destroy()


class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.bind("<<ShowFrame>>", self.on_show_frame)

        global last_error_label

        label_empty_row = tk.Label(self).grid(row=0, column=0)

        label_header = tk.Label(self, text="REJESTRACJA", font='Arial 15 bold', width=60, height=5,
                                relief='groove').grid(row=1, column=0, columnspan=4)

        label_empty_row = tk.Label(self).grid(row=2, column=1)
        label_empty_col = tk.Label(self, width=8).grid(row=3, column=0)

        label_user = tk.Label(self, text="Login:", font='Arial 10', width=20, height=2, relief='groove').grid(row=3,
                                                                                                              column=1)
        input_user = tk.Entry(self)
        input_user.grid(row=3, column=2)

        label_empty_row = tk.Label(self).grid(row=4, column=1)

        label_pword = tk.Label(self, text="Hasło:", font='Arial 10', width=20, height=2, relief='groove').grid(row=5,
                                                                                                               column=1)
        input_pword = tk.Entry(self, show='*')
        input_pword.grid(row=5, column=2)

        label_empty_row = tk.Label(self).grid(row=6, column=1)

        label_pword2 = tk.Label(self, text="Powtórz hasło:", font='Arial 10', width=20, height=2, relief='groove').grid(
            row=7,
            column=1)

        input_pword2 = tk.Entry(self, show='*')
        input_pword2.grid(row=7, column=2)

        last_error_label = tk.Label(self)
        last_error_label.grid(row=8, column=1)
        label_empty_row = tk.Label(self).grid(row=9, column=1)

        button_register = tk.Button(self, text="Zarejestruj", font='Arial 10', width=30, height=4, relief='groove',
                                    command=lambda: register_user(input_user, input_pword, input_pword2)).grid(row=10,
                                                                                                              column=0,
                                                                                                              columnspan=4)

        button_quit = tk.Button(self, text="Wróć", font='Arial 10', width=30, height=4, relief='groove',
                                command=lambda: controller.show_frame(Login)).grid(row=11, column=0, columnspan=4)

        # Registration function, adding a new entry to the dictionary with username as a key and
        # password as a value

        def register_user(input_user, input_password, input_password_repeat):

            provided_username = input_user.get()
            provided_password = input_password.get()
            provided_password_repeat = input_password_repeat.get()

            def display_error(error_message):
                global last_error_label
                last_error_label.destroy()
                last_error_label = tk.Label(self, text=error_message)
                last_error_label.grid(row=8, column=2)

            valid_username = False

            if len(provided_username) < 6:
                display_error("Nazwa za krótka (min 6)")
            elif len(provided_username) >= 6:

                if not provided_username.isalnum():
                    display_error("Hasło musi zawierać litery i cyfry")

                else:
                    data = load_obj('users')
                    if provided_username in data.keys():
                        display_error("Nazwa zajęta")
                    else:
                        valid_username = True

            if valid_username:

                if len(provided_password) < 6:
                    display_error("Za krótkie hasło (min 6)")
                elif len(provided_password) >= 6:

                    includes_letter = False
                    includes_number = False
                    invalid_character = False

                    for char in provided_password:
                        if char.isalpha():
                            includes_letter = True
                        elif char.isdecimal():
                            includes_number = True
                        else:
                            invalid_character = True
                    if not includes_letter or not includes_number:
                        display_error("Hasło musi zawierać litery i cyfry")
                    elif not invalid_character:
                        data = load_obj('users')
                        if provided_password != provided_password_repeat:
                            display_error("Hasła nie są jednakowe")
                        else:
                            data[provided_username] = provided_password
                            userdata = {}
                            save_obj(userdata, provided_username)
                            save_obj(data, 'users')
                            controller.show_frame(Login)

    def on_show_frame(self, event):

        global last_error_label
        last_error_label.destroy()


class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):

        global username

        label_username = tk.Label(self, text='Logged in as: {}'.format(username)).grid(row=0, column=1, sticky='w')

        label_header = tk.Label(self, text="MENU", font='Arial 15 bold', width=60, height=5, relief='groove').grid(row=1, column=1)
        
        label_empty_row = tk.Label(self).grid(row=2,column=1)

        button_items = tk.Button(self, text="Materiały", font='Arial 10', width=60, height=8, relief='groove',
                            command=lambda: self.controller.show_frame(ItemsShow)).grid(row=3,column=1)

        button_locations = tk.Button(self, text="Magazyny", font='Arial 10', width=60, height=8, relief='groove',
                            command=lambda: self.controller.show_frame(LocationsShow)).grid(row=4, column=1)

        button_private = tk.Button(self, text="Moje rezerwacje", font='Arial 10', width=60, height=8, relief='groove',
                                     command=lambda: self.controller.show_frame(ItemsPrivate)).grid(row=5, column=1)

        label_empty_row = tk.Label(self).grid(row=6,column=1)

        button_quit = tk.Button(self, text="Wyloguj", font='Arial 10', width=30, height=4, relief='groove',
                            command=lambda: self.controller.show_frame(Login)).grid(row=7, column=1)


class ItemsPrivate(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):

        main_row = 3
        global last_row
        global last_key
        global username
        data = load_obj(username)

        for widget in self.winfo_children():
            widget.destroy()

        label_username = tk.Label(self, text='Logged in as: {}'.format(username)).grid(row=0, column=0, sticky='w')

        label_header = tk.Label(self, text="MOJE REZERWACJE", font='Arial 15 bold', width=60, height=5,
                                relief='groove').grid(row=1, column=0, columnspan=7)
        label_empty_row = tk.Label(self).grid(row=2, column=1)

        # Function selecting a location (a dictionary key) after pressing a button

        def choose_location(key):

            global last_value
            global last_key
            global last_row
            last_key = key
            row = 2

            data = load_obj(username)

            self.controller.show_frame(ItemsPrivate)

            row += 1

            label_empty_row = tk.Label(self).grid(row=row,column=1)

            # Printing entries from a nested dictionary provided to choose_location function.
            # That means printing names of the items and their quantities for a given location.

            for k, v in data[key].items():

                data_all = load_obj('item_location_data')
                available = 0
                if key in data_all.keys():
                    if k in data_all[key]:
                        available = int(data_all[key][k])

                if k == last_value:

                    label_item_quantity = tk.Button(self, text="{}  -  {} szt. ({})".format(k, v, available), width=25, relief='groove',
                                                    bg='blue',
                                                    command=lambda i=row, j=k: print_buttons(i, key, j)).grid(row=row,
                                                                                                             column=2,
                                                                                                             sticky='w')
                    last_value = ''
                    row += 1
                else:
                    label_item_quantity = tk.Button(self, text="{}  -  {} szt. ({})".format(k, v, available), width=25, relief='groove',
                                                    command=lambda i=row, j=k: print_buttons(i, key, j)).grid(row=row,
                                                                                                             column=2,
                                                                                                             sticky='w')
                    row += 1

            label_empty_row = tk.Label(self).grid(row=row, column=1)

            row += 1

            # Function for displaying buttons to change values of reserved items

            def print_buttons(row, key, item):

                global last_value
                last_value = item

                self.controller.show_frame(ItemsPrivate)
                choose_location(key)

                label_header = tk.Label(self, text='Zmiana ilości', font="Arial 10", width=30, relief='groove').grid(
                    row=2, column=3, columnspan=4)

                the_input_quantity = tk.Entry(self, width=3)

                the_input_quantity.grid(row=3, column=3)

                label_undo_reserve_quantity = tk.Button(self, text="Odłóż", relief='groove', font="Arial 10", width=8,
                                          command=lambda i=k: undo_reserve_quantity(key, item, the_input_quantity)).grid(
                    row=3,
                    column=4, columnspan=1)

                label_use_some = tk.Button(self, text="Zabierz", relief='groove', font="Arial 10", width=8,
                                          command=lambda i=k: use_some(key, item,
                                                                                    the_input_quantity)).grid(
                    row=3,
                    column=5, columnspan=2)

                label_undo_reserve = tk.Button(self, text="Odłóż wszystkie", relief='groove', width=20,
                                         command=lambda i=k: undo_reserve(key, item)).grid(
                    row=4,
                    column=3, columnspan=4)

                label_use_all = tk.Button(self, text="Zabierz wszystkie", relief='groove', width=20,
                                         command=lambda i=k: use_all(key, item)).grid(
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

                    self.controller.show_frame(ItemsPrivate)
                    choose_location(user_location)

            # Function for 'using an amount' of an item - subtracting given quantity from the global
            # and user's dictionary

            def use_some(user_location, user_item, user_quantity):

                quantity = user_quantity.get()
                if quantity.isdecimal():
                    private_list = load_obj(username)
                    if int(private_list[user_location][user_item]) - int(quantity) > 0:
                        private_list[user_location][user_item] = str(int(private_list[user_location][user_item]) - int(quantity))
                    else:
                        private_list[user_location].pop(user_item)
                    save_obj(private_list, username)

                    self.controller.show_frame(ItemsPrivate)
                    choose_location(user_location)

            # Function for 'using' an item - removing it from user's dictionary
            # and subtracting user's reserved quantity from the global dictionary

            def use_all(user_location, user_item):

                private_list = load_obj(username)
                private_list[user_location].pop(user_item)
                save_obj(private_list, username)

                self.controller.show_frame(ItemsPrivate)
                choose_location(user_location)

            # Function for 'putting back and amount' of an item, subtracting given amount from user's dictionary
            # and adding it to the global dictionary

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

            # Function for 'putting back' an item, removing it from user's dictionary
            # and adding user's reserved quantity to the global dictionary

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
                self.controller.show_frame(ItemsPrivate)
                choose_location(user_location)

        # Printing buttons for choosing a location (key from a dictionary)

        for key in data.keys():
            if key == last_key:
                label0 = tk.Button(self, text=key.upper(), width=20, height=3, relief='groove', bg='blue',
                                   command=lambda i=key: choose_location(i)).grid(row=main_row, column=0, rowspan=2,
                                                                                 sticky='w')
                last_key = ''
                main_row += 2
            else:
                label0 = tk.Button(self, text=key.upper(), width=20, height=3, relief='groove',
                                   command=lambda i=key: choose_location(i)).grid(row=main_row, column=0, rowspan=2,
                                                                                 sticky='w')
                main_row += 2

        label_empty_row = tk.Label(self).grid(row=19, column=1)

        button_back = tk.Button(self, text="Wróć", width=30, height=3, relief='groove',
                                command=lambda: self.controller.show_frame(MainMenu)).grid(row=20, column=0,
                                                                                           columnspan=7)


class ItemsShow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):

        row = 3
        main_row = 3
        global last_row
        global last_key
        data = load_obj('item_location_data')
    
        for widget in self.winfo_children():
            widget.destroy()

        global username

        label_username = tk.Label(self, text='Logged in as: {}'.format(username)).grid(row=0, column=0, sticky='w')

        label_header = tk.Label(self, text="LISTA MATERIAŁÓW", font='Arial 15 bold', width=60, height=5, relief='groove').grid(row=1, column=0, columnspan=7)
        label_empty_row = tk.Label(self).grid(row=2,column=1)

        # Function selecting a location (a dictionary key) after pressing a button

        def choose_location(key):

            global last_value
            global last_key
            global last_row
            last_key = key
            row = 2
            
            data = load_obj('item_location_data')

            self.controller.show_frame(ItemsShow)

            row += 1

            # Printing entries from a nested dictionary provided to choose_location function.
            # That means printing names of the items and their quantities for a given location.

            for k, v in data[key].items():

                reserved = 0
                reserved_and_available = int(data[key][k])
                for user in load_obj('users').keys():
                    reservation_data = load_obj(user)
                    if key in reservation_data.keys():
                        if k in reservation_data[key]:
                            reserved_and_available += int(reservation_data[key][k])
                reserved = reserved_and_available - int(data[key][k])

                if k == last_value:
                    label_item_quantity = tk.Button(self, text = "{}  -  {} / {}  ({})".format(k, v, reserved_and_available, reserved), width = 25, relief='groove', bg='blue',
                                command=lambda i=row, j=k: print_buttons(i, key, j)).grid(row=row, column=2, sticky='w')
                    last_value = ''
                    row += 1
                else:
                    label_item_quantity = tk.Button(self, text = "{}  -  {} / {}  ({})".format(k, v, reserved_and_available, reserved), width = 25, relief='groove',
                                command=lambda i=row, j=k: print_buttons(i, key, j)).grid(row=row, column=2, sticky='w')
                    row += 1

            label_empty_row = tk.Label(self).grid(row=row,column=1)

            row += 1

            # Buttons for adding a new item to the dictionary

            label_item = tk.Label(self, text = "Nazwa:").grid(row=main_row,column=2)
            label_quantity = tk.Label(self, text = "Ilość:").grid(row=main_row,column=3)

            row += 1
            the_input_item = tk.Entry(self, width=25)
            the_input_item.grid(row=main_row+1,column=2, sticky='w')
            the_input_quantity = tk.Entry(self, width=5)
            the_input_quantity.grid(row=main_row+1,column=3)
            label_add_item = tk.Button(self, text = "Dodaj nowy", relief='groove',
                        command=lambda: add_item(key, the_input_item, the_input_quantity)).grid(row=main_row+1,column=4,columnspan=3, sticky='w')

            # Function for displaying buttons to change values of a given key in a nested dictionary.
            # Displaying an entry widget and buttons to add, subtract and reserve
            # Displaying a button to remove an item

            def print_buttons(row, key, item):

                global last_value
                last_value = item

                self.controller.show_frame(ItemsShow)
                choose_location(key)

                label_header = tk.Label(self, text = 'Zmiana ilości', font="Arial 10", width=30, relief='groove').grid(row=2,column=3,columnspan=4)

                the_input_quantity = tk.Entry(self, width=3)
                the_input_quantity.grid(row=3,column=3)
                label_add = tk.Button(self, text = "+", relief='groove',
                            command=lambda i=k: add_quantity(key, item, the_input_quantity)).grid(row=3,column=4)
                the_input_remove = tk.Entry(self, width=3)
                label_subtract = tk.Button(self, text = "-", relief='groove',
                            command=lambda i=k: subtract_quantity(key, item, the_input_quantity)).grid(row=3,column=5)
                label_reserve = tk.Button(self, text="Zarezerwuj", relief='groove',
                                         command=lambda i=k: reserve_quantity(key, item, the_input_quantity)).grid(row=3,
                                                                                                                 column=6)
                label_delete = tk.Button(self, text="Usuń przedmiot", relief='groove', width=20,
                                          command=lambda i=k: delete_item(key, item)).grid(
                    row=4,
                    column=3, columnspan=4)

                # Displaying a list of reservations for a chosen item

                label_reservations = tk.Label(self, text="Rezerwacje:").grid(row=5, column=3, columnspan=4)
                reserved_row = 6

                for user in load_obj('users').keys():
                    reservation_data = load_obj(user)
                    if key in reservation_data.keys():
                        if item in reservation_data[key]:
                            reserved = int(reservation_data[key][item])
                            label_reserved = tk.Label(self, text = "{} - {}".format(user, reserved)).grid(row=reserved_row, column=3, columnspan=4)
                            reserved_row += 1

            # Function for adding a new entry to a nested dictionary.
            # Adding a new item and its quantity

            def add_item(user_location, user_item, user_quantity):

                quantity = user_quantity.get()
                if quantity.isdecimal():
                    output_list = load_obj('item_location_data')
                    output_list[user_location.lower()][user_item.get()] = quantity
                    save_obj(output_list, 'item_location_data')
                    self.controller.show_frame(ItemsShow)
                    choose_location(user_location)

            # Function for changing value of an entry in a nested dictionary.
            # Adding an int to items quantity

            def add_quantity(user_location, user_item, user_quantity):
                
                quantity = user_quantity.get()
                if quantity.isdecimal():
                    output_list = load_obj('item_location_data')
                    output_list[user_location.lower()][user_item] = str(int(quantity) + int(output_list[user_location.lower()][user_item]))
                    save_obj(output_list, 'item_location_data')
                    self.controller.show_frame(ItemsShow)
                    choose_location(user_location)

            # Function for changing value of an entry in a nested dictionary.
            # Subtracting an int from items quantity.

            def subtract_quantity(user_location, user_item, user_quantity):
                
                quantity = user_quantity.get()
                if quantity.isdecimal():
                    output_list = load_obj('item_location_data')

                    if int(output_list[user_location.lower()][user_item]) - int(quantity) > 0:
                        output_list[user_location.lower()][user_item] = str(int(output_list[user_location.lower()][user_item]) - int(quantity))
                    else:
                        output_list[user_location.lower()].pop(user_item)

                    save_obj(output_list, 'item_location_data')
                    self.controller.show_frame(ItemsShow)
                    choose_location(user_location)

            # Function for reserving a value of an entry in a nested dictionary.
            # Adding an int or creating an entry in user's private list of items

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

            # Function for deleting an entry from a nested dictionary.
            # Removing an item from a 'global' dictionary and from all private lists of users

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

                self.controller.show_frame(ItemsShow)
                choose_location(user_location)

        # Printing buttons for choosing a key from a dictionary.

        for key in data.keys():
            if key == last_key:
                label0 = tk.Button(self, text = key.upper(), width=20, height=3, relief='groove', bg='blue',
                                    command=lambda i=key: choose_location(i)).grid(row=main_row, column=0, rowspan=2, sticky='w')
                last_key = ''
                main_row += 2
            else:
                label0 = tk.Button(self, text = key.upper(), width=20, height=3, relief='groove',
                                    command=lambda i=key: choose_location(i)).grid(row=main_row, column=0, rowspan=2, sticky='w')
                main_row += 2

        label_empty_row = tk.Label(self).grid(row=19, column=1)

        button_back = tk.Button(self, text="Wróć", width=30, height=3, relief='groove',
                        command=lambda: self.controller.show_frame(MainMenu)).grid(row=20, column=0, columnspan=7)


class LocationsShow(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent, height=50)

        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):

        row = 3
        data = load_obj('item_location_data')

        def confirm_location_removal(key):
            global user_input
            user_input = key
            self.controller.show_frame(LocationsConfirm)

        def add_location(input_location, output_list):
            output_list[input_location.lower()] = {}
            save_obj(output_list, 'item_location_data')
            self.controller.show_frame(LocationsShow)
    
        for widget in self.winfo_children():
            widget.destroy()

        global username

        label_username = tk.Label(self, text='Logged in as: {}'.format(username)).grid(row=0, column=0, sticky='w')

        label_header = tk.Label(self, text="LISTA MAGAZYNÓW", font='Arial 15 bold', width=60, height=5, relief='groove').grid(row=1, column=0, columnspan=2)
        label_empty_row = tk.Label(self).grid(row=2,column=1)

        # A list of locations and buttons to delete them

        for key in data.keys():
            label_location = tk.Label(self, text = key.upper(), width=50, height=2, font='Arial 10 bold', relief='groove').grid(row=row,column=0)
            label_delete = tk.Button(self, text = "Usuń", width=30, height=2, relief='groove',
                                command=lambda i=key: confirm_location_removal(i)).grid(row=row, column=1)
            row +=1
            label_empty_row = tk.Label(self).grid(row=row,column=1)
            row +=1

        label_empty_row = tk.Label(self).grid(row=row,column=1)
        row +=1

        # Buttons for adding a new location

        the_input_add_location = tk.Entry(self, width=30)
        the_input_add_location.grid(row=row,column=0)
        label_add_location = tk.Button(self, text = "Dodaj nowy", width=30, relief='groove',
                            command=lambda: add_location(the_input_add_location.get(), load_obj('item_location_data'))).grid(row=row, column=1)

        row += 1
        label_empty_row = tk.Label(self).grid(row=row,column=1)
        row +=1

        button_back = tk.Button(self, text="Wróć", width=30, height=3, relief='groove',
                        command=lambda: self.controller.show_frame(MainMenu)).grid(row=row, column=0, columnspan=2) 


class LocationsConfirm(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, height=50)

        self.bind("<<ShowFrame>>", self.on_show_frame)

        # Function for deleting a location

        def remove_location(input_location, output_list):
            output_list.pop(input_location.lower())
            save_obj(output_list, 'item_location_data')
            controller.show_frame(LocationsShow)

        button_delete = tk.Button(self, text="Usuń", width=30, height=3, relief='groove',
                        command=lambda: remove_location(user_input, load_obj('item_location_data'))).grid(row=8, column=1)

        button_back = tk.Button(self, text="Wróć", width=30, height=3, relief='groove',
                        command=lambda: controller.show_frame(LocationsShow)).grid(row=9, column=1)

    def on_show_frame(self, event):

        # Warning and confirmation for removal of a location

        global username

        label_username = tk.Label(self, text='Logged in as: {}'.format(username)).grid(row=0, column=1, sticky='w')

        global user_input

        label_header = tk.Label(self, text="USUNĄĆ {}?".format(user_input.upper()),font='Arial 15 bold', width=60, height=5, relief='groove').grid(row=1, column=1)

        label_empty_row = tk.Label(self).grid(row=2,column=1)

        label_info = tk.Label(self, text="Cała zawartość magazynu zostanie usunięta.", font='Arial 10', width=55, height=5).grid(row=3, column=1)


app = Inventory()

app.mainloop()