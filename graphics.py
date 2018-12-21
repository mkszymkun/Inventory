#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
from tkinter import font as tkfont


class Graphics(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    def empty_row(self, row, col):
        label = tk.Label(self, bg='#303030', fg='white')
        label.grid(row=row, column=col)

    def login_label(self, text, row, col):
        font = tkfont.Font(family='Ubuntu', size=15, weight="bold")
        image = tk.PhotoImage(file="pictures/buttons/login_button.png")
        label = tk.Label(self, text=text, font=font, image=image, fg='white',
                           borderwidth='0', bg='#303030', compound='center')
        label.image = image
        label.grid(row=row, column=col)


    def login_button(self, text, commands, row):
        font = tkfont.Font(family='Ubuntu', size=15, weight="bold")
        image = tk.PhotoImage(file="pictures/buttons/login_button.png")
        button = tk.Button(self, text=text, font=font, image=image, fg='white',
                           borderwidth='0', bg='#303030', compound='center',
                           activebackground='#303030',
                           highlightbackground='#303030', command=commands)
        button.image = image
        button.grid(row=row, column=0, columnspan=4)

    # MENU

    def menu_button(self, text, command, row):
        font = tkfont.Font(family='Ubuntu', size=25, weight="bold")
        image = tk.PhotoImage(file="pictures/buttons/menu_button.png")
        button = tk.Button(self, text=text, image=image,
                           borderwidth='0', bg='#303030', font = font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030', command=command)
        button.image = image
        button.grid(row=row, column=1)

    def logout_button(self, text,command, row):
        font = tkfont.Font(family='Ubuntu', size=25, weight="bold")
        image = tk.PhotoImage(file="pictures/buttons/menu_button.png")
        button = tk.Button(self, text=text, image=image,
                           borderwidth='0', bg='#303030', font = font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030', command=command)
        button.image = image
        button.grid(row=row, column=1)

    def menu_header(self):
        font = tkfont.Font(family='Ubuntu', size=25, weight="bold")
        image = tk.PhotoImage(file="pictures/labels/menu_header.png")
        label = tk.Label(self, text="MENU", font=font, image=image,
                         borderwidth='0', bg='#303030',  fg='white',
                         activebackground='#303030',  compound='center',
                         highlightbackground='#303030')
        label.image = image
        label.grid(row=1, column=1)

    # LOGIN

    def login_header(self, text):
        font = tkfont.Font(family='Ubuntu', size=25, weight="bold")
        image = tk.PhotoImage(file="pictures/labels/login_header.png")
        label = tk.Label(self, text=text, font=font, image=image,
                         borderwidth='0', bg='#303030',  fg='white',
                         activebackground='#303030',  compound='center',
                         highlightbackground='#303030',
                 relief='groove')
        label.image = image
        label.grid(row=1, column=0, columnspan=4)

    def display_login_error(self, error_message):
        self.last_error_label.destroy()

        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/labels/error_label.png")
        self.last_error_label = tk.Label(self, text=error_message, font=font, image=image, fg='white',
                           borderwidth='0', bg='#303030', compound='center',
                           activebackground='#303030',
                           highlightbackground='#303030')
        self.last_error_label.image = image
        self.last_error_label.grid(row=6, column=2)


    def display_registration_error(self, error_message):
        self.last_error_label.destroy()
        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/labels/error_label.png")
        self.last_error_label = tk.Label(self, text=error_message, font=font, image=image, fg='white',
                                         borderwidth='0', bg='#303030', compound='center',
                                         activebackground='#303030',
                                         highlightbackground='#303030')
        self.last_error_label.image = image
        self.last_error_label.grid(row=8, column=2)

    def add_location_button(self, command, row):
        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/buttons/location_name.png")
        button = tk.Button(self, text="Dodaj nowy", image=image,
                           borderwidth='0', bg='#303030', font=font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030', command=command)
        button.image = image
        button.grid(row=row + 2, column=1)

    def warning(self, text, row, col):
        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/labels/warning.png")
        label = tk.Label(self, text=text, font=font, image=image,
                         borderwidth='0', bg='#303030',  fg='white',
                         activebackground='#303030',  compound='center',
                         highlightbackground='#303030',
                 relief='groove')
        label.image = image
        label.grid(row=row, column=col)

    def button(self, text, command, row):
        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/buttons/location_name.png")
        button = tk.Button(self, text=text, image=image,
                           borderwidth='0', bg='#303030', font=font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030', command=command)
        button.image = image
        button.grid(row=row, column=0, columnspan=4)

    def location_label(self, key, row):
        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/buttons/location_name.png")
        label = tk.Label(self, text=key.upper(), image=image,
                           borderwidth='0', bg='#303030', font=font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030')
        label.image = image
        label.grid(row=row, column=0)

    def location_delete_button(self, command, row):
        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/buttons/location_name.png")
        button = tk.Button(self, text="Usuń", image=image,
                           borderwidth='0', bg='#303030', font=font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030', command=command)
        button.image = image
        button.grid(row=row, column=1)

    def items_operations_button(self, text, command, row, col):
        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/buttons/ad_buttons_small.png")
        button = tk.Button(self, text=text, image=image,
                           borderwidth='0', bg='#303030', font=font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030', command=command)
        button.image = image
        button.grid(row=row, column=col)

    def items_operations_button_2(self, text, command, row, col):
        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/buttons/ad_buttons_medium.png")
        button = tk.Button(self, text=text, image=image,
                           borderwidth='0', bg='#303030', font=font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030', command=command)
        button.image = image
        button.grid(row=row, column=col)

    def location_name_button_colored(self, text, command, row):
        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/buttons/location_name_pressed.png")
        button = tk.Button(self, text=text, image=image,
                           borderwidth='0', bg='#303030', font=font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030', command=command)
        button.image = image
        button.grid(row=row, column=0, rowspan=2, sticky='w')

    def location_name_button(self, text, command, row):
        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/buttons/location_name.png")
        button = tk.Button(self, text=text, image=image,
                           borderwidth='0', bg='#303030', font=font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030', command=command)
        button.image = image
        button.grid(row=row, column=0, rowspan=2, sticky='w')

    def item_name_button_colored(self, k, v, reserved_and_available,
                                 reserved, command, row):
        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/buttons/item_name_pressed.png")
        button = tk.Button(self, text="{}  -  {} / {}  ({})".format(
            k, v, reserved_and_available, reserved), image=image,
                           borderwidth='0', bg='#303030', font=font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030', command=command)
        button.image = image
        button.grid(row=row, column=1, columnspan=2)

    def item_name_button(self, k, v, reserved_and_available, reserved,
                         command, row):
        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/buttons/item_name.png")
        button = tk.Button(self, text="{}  -  {} / {}  ({})".format(
            k, v, reserved_and_available, reserved), image=image,
                           borderwidth='0', bg='#303030', font=font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030', command=command)
        button.image = image
        button.grid(row=row, column=1, columnspan=2)

    def adding_new_item_label(self, text, row, col):
        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/labels/small_title.png")
        label = tk.Label(self, text=text, image=image,
                           borderwidth='0', bg='#303030', font=font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030')
        label.image = image
        label.grid(row=row, column=col)

    def adding_new_item_label_2(self, text, row, col):
        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/labels/small_title_2.png")
        label = tk.Label(self, text=text, image=image,
                           borderwidth='0', bg='#303030', font=font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030')
        label.image = image
        label.grid(row=row, column=col)

    def adding_new_item_button(self, text, command, row):
        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/labels/small_title.png")
        button = tk.Button(self, text=text, image=image,
                           borderwidth='0', bg='#303030', font=font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030', command=command)
        button.image = image
        button.grid(row=row, column=3, columnspan=1, sticky='w')

    def reserved_item_name_button_colored(self, item, reserved, available,
                                          command, row):
        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/buttons/item_name_pressed.png")
        button = tk.Button(self, text="{}  -  {} szt. ({})".format(
            item, reserved, available), image=image,
                           borderwidth='0', bg='#303030', font=font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030', command=command)
        button.image = image
        button.grid(row=row, column=2, sticky='w')

    def reserved_item_name_button(self, item, reserved, available,
                                  command, row):
        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/buttons/item_name.png")
        button = tk.Button(self, text="{}  -  {} szt. ({})".format(
            item, reserved, available), image=image,
                           borderwidth='0', bg='#303030', font=font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030', command=command)
        button.image = image
        button.grid(row=row, column=2, sticky='w')

    def search_results_label(self, item):
        font = tkfont.Font(family='Ubuntu', size=25, weight="bold")
        image = tk.PhotoImage(file="pictures/labels/login_header.png")
        label = tk.Label(self, text="WYNIKI DLA \"{}\"".format(item), font=font, image=image,
                         borderwidth='0', bg='#303030',  fg='white',
                         activebackground='#303030',  compound='center',
                         highlightbackground='#303030',
                 relief='groove')
        label.image = image
        label.grid(row=1, column=0, columnspan=2)

    def search_button(self, command):
        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/buttons/location_name.png")
        button = tk.Button(self, text='Szukaj', image=image,
                           borderwidth='0', bg='#303030', font=font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030', command=command)
        button.image = image
        button.grid(row=4, column=0, columnspan=4)

    def small_title_label(self, text):
        font = tkfont.Font(family='Ubuntu', size=25, weight="bold")
        image = tk.PhotoImage(file="pictures/labels/ad_buttons_header.png")
        label = tk.Label(self, text=text, image=image,
                           borderwidth='0', bg='#303030', font=font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030')
        label.image = image
        label.grid(row=1, column=0, columnspan=4)


    def delete_item_button(self, text, command):
        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/buttons/ad_buttons_big.png")
        button = tk.Button(self, text=text, image=image,
                           borderwidth='0', bg='#303030', font=font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030', command=command)
        button.image = image
        button.grid(row=4, column=0, columnspan=4)

    def reservations_label(self, text):
        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/buttons/ad_buttons_big.png")
        label = tk.Label(self, text=text, image=image,
                           borderwidth='0', bg='#303030', font=font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030')
        label.image = image
        label.grid(row=5, column=0, columnspan=4)

    def reservation_label(self, user, reserved, row):
        font = tkfont.Font(family='Ubuntu', size=15)
        image = tk.PhotoImage(file="pictures/buttons/ad_buttons_big.png")
        label = tk.Label(self, text="{} - {}".format(user, reserved), image=image,
                           borderwidth='0', bg='#303030', font=font, fg='white',
                           activebackground='#303030', compound='center',
                           highlightbackground='#303030')
        label.image = image
        label.grid(row=row, column=0, columnspan=4)
