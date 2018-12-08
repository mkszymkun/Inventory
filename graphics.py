#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle


class Graphics(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    def empty_row(self, row, col):
        tk.Label(self).grid(row=row, column=col)

    def login_label(self, text, row, col):
        tk.Label(self, text=text, font='Arial 10', width=20, height=2, relief='groove').grid(row=row,
                                                                                                 column=col)

    def login_button(self, text, commands, row):
        tk.Button(self, text=text, font='Arial 10', width=30, height=4, relief='groove',
                  command=commands).grid(row=row, column=0, columnspan=4)

    def menu_button(self, text, command, row):
        tk.Button(self, text=text, font='Arial 10', width=50, height=6, relief='groove',
                  command=command).grid(row=row, column=1)

    def menu_header(self):
        tk.Label(self, text="MENU", font='Arial 15 bold', width=30, height=5).grid(
        row=1, column=1)

    def login_header(self, text):
        tk.Label(self, text=text, font='Arial 15 bold', width=60, height=5,
                 relief='groove').grid(row=1, column=0, columnspan=4)

    def display_login_error(self, error_message):
        self.last_error_label.destroy()
        self.last_error_label = tk.Label(self, text=error_message)
        self.last_error_label.grid(row=6, column=2)

    def display_registration_error(self, error_message):
        self.last_error_label.destroy()
        self.last_error_label = tk.Label(self, text=error_message)
        self.last_error_label.grid(row=8, column=2)

    def add_location_button(self, command, row):
        tk.Button(self, text="Dodaj nowy", width=30, relief='groove',
                                       command=command).grid(row=row + 2, column=1)

    def warning(self, text, row, col):
        tk.Label(self, text=text, font='Arial 10', width=55, height=5).grid(
            row=row, column=col)

    def button(self, text, commands, row):
        tk.Button(self, text=text, font='Arial 10', width=30, height=4, relief='groove',
                  command=commands).grid(row=row, column=0, columnspan=4)

    def location_label(self, key, row):
        tk.Label(self, text=key.upper(), width=50, height=2, font='Arial 10 bold',
                                  relief='groove').grid(row=row, column=0)

    def location_delete_button(self, command, row):
        tk.Button(self, text="Usuń", width=30, height=2, relief='groove',
                                 command=command).grid(row=row, column=1)

    def items_operations_button(self, text, command, row, col):
        tk.Button(self, text=text, relief='groove', command=command).grid(row=row, column=col)



    def location_name_button_colored(self, text, command, row):
        tk.Button(self, text=text, width=20, height=3, relief='groove', bg='blue',
                  command=command).grid(row=row, column=0, rowspan=2, sticky='w')

    def location_name_button(self, text, command, row):
        tk.Button(self, text=text, width=20, height=3, relief='groove',
                  command=command).grid(row=row, column=0, rowspan=2, sticky='w')



    def item_name_button_colored(self, k, v, reserved_and_available, reserved, command, row):
        tk.Button(self, text="{}  -  {} / {}  ({})".format(k, v, reserved_and_available, reserved), width=25,
                    relief='groove', bg='blue', command=command).grid(row=row, column=1, columnspan=2)

    def item_name_button(self, k, v, reserved_and_available, reserved, command, row):
        tk.Button(self, text="{}  -  {} / {}  ({})".format(k, v, reserved_and_available, reserved), width=25,
                    relief='groove', command=command).grid(row=row, column=1, columnspan=2)


    def adding_new_item_label(self, text, row, col):
        tk.Label(self, text=text).grid(row=row, column=col)

    def adding_new_item_button(self, text, command, row):
        tk.Button(self, text=text, relief='groove', command=command).grid(row=row, column=3, columnspan=1, sticky='w')


    def reserved_item_name_button_colored(self, item, reserved, available, command, row):
        tk.Button(self, text="{}  -  {} szt. ({})".format(item, reserved, available), width=25,
                    relief='groove', bg='blue', command=command).grid(row=row, column=2, sticky='w')

    def reserved_item_name_button(self, item, reserved, available, command, row):
        tk.Button(self, text="{}  -  {} szt. ({})".format(item, reserved, available), width=25,
                    relief='groove', command=command).grid(row=row, column=2, sticky='w')

    def search_results_label(self, item):
        tk.Label(self, text="WYNIKI DLA \"{}\"".format(item), font='Arial 15 bold', width=60, height=5,
                                relief='groove').grid(row=1, column=0, columnspan=2)

    def search_button(self, command):
        tk.Button(self, text="Szukaj", width=50, height=3, relief='groove',
                                  command=command).grid(row=4,column=0,columnspan=4)


    def small_title_label(self, text):
        tk.Label(self, text=text, font="Arial 10", width=30, relief='groove').grid(row=1, column=0,
                                                                                              columnspan=4)

    def delete_item_button(self, text, command):
        tk.Button(self, text=text, relief='groove', width=20,
                  command=command).grid(row=4, column=0, columnspan=4)

    def reservations_label(self, text):
        tk.Label(self, text=text).grid(row=5, column=3, columnspan=4)

    def reservation_label(self, user, reserved, row):
        tk.Label(self, text="{} - {}".format(user, reserved)).grid(row=row, column=3, columnspan=4)
