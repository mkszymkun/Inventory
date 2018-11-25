#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle

class Register(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        def header(text):
            tk.Label(self, text=text, font='Arial 15 bold', width=60, height=5,
                     relief='groove').grid(row=1, column=0, columnspan=4)

        def empty_row(row, col):
            tk.Label(self).grid(row=row, column=col)

        def label(text, row, col):
            tk.Label(self, text=text, font='Arial 10', width=20, height=2, relief='groove').grid(row=row,
                                                                                                     column=col)

        empty_row(0,0)
        header("REJESTRACJA")

        empty_row(2, 1)
        label("Login:", 3, 1)

        input_user = tk.Entry(self)
        input_user.grid(row=3, column=2)

        empty_row(4, 1)

        label("Hasło:", 5, 1)

        input_pword = tk.Entry(self, show='*')
        input_pword.grid(row=5, column=2)

        empty_row(6, 1)

        label("Powtórz hasło:", 7, 1)

        input_pword2 = tk.Entry(self, show='*')
        input_pword2.grid(row=7, column=2)

        self.last_error_label = tk.Label(self)
        self.last_error_label.grid(row=8, column=1)
        empty_row(9, 1)

        button_register = tk.Button(self, text="Zarejestruj", font='Arial 10', width=30, height=4, relief='groove',
                                    command=lambda: register_user(input_user, input_pword, input_pword2)).grid(row=10,
                                                                                                              column=0,
                                                                                                              columnspan=4)

        button_quit = tk.Button(self, text="Wróć", font='Arial 10', width=30, height=4, relief='groove',
                                command=lambda: controller.show_frame("Login")).grid(row=11, column=0, columnspan=4)

        def save_obj(obj, name):
            with open(name + '.pkl', 'wb') as f:
                pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

        def load_obj(name):
            with open(name + '.pkl', 'rb') as f:
                return pickle.load(f)

        def register_user(input_user, input_password, input_password_repeat):

            provided_username = input_user.get()
            provided_password = input_password.get()
            provided_password_repeat = input_password_repeat.get()

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
                            controller.show_frame("Login")

        def display_error(error_message):
            self.last_error_label.destroy()
            self.last_error_label = tk.Label(self, text=error_message)
            self.last_error_label.grid(row=8, column=2)

    def on_show_frame(self, event):

        self.last_error_label.destroy()
