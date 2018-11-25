#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle


class Register(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        def save_obj(obj, name):
            with open(name + '.pkl', 'wb') as f:
                pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

        def load_obj(name):
            with open(name + '.pkl', 'rb') as f:
                return pickle.load(f)

        def button(text, commands, row):
            tk.Button(self, text=text, font='Arial 10', width=30, height=4, relief='groove',
                      command=commands).grid(row=row, column=0, columnspan=4)

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
        button("Zarejestruj", lambda: register_user(input_user, input_pword, input_pword2), 10)
        button("Wróć", lambda: controller.show_frame("Login"), 11)

        def check_username(username):

            if len(username) < 6:
                display_error("Nazwa za krótka (min 6)")
            elif len(username) >= 6:

                if not username.isalnum():
                    display_error("Hasło musi zawierać litery i cyfry")

                else:
                    data = load_obj('users')
                    if username in data.keys():
                        display_error("Nazwa zajęta")
                    else:
                        return True

        def check_password(username, password, password2):

            if len(password) < 6:
                display_error("Za krótkie hasło (min 6)")

            elif len(password) >= 6:

                includes_letter = False
                includes_number = False
                invalid_character = False

                for char in password:
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
                    if password != password2:
                        display_error("Hasła nie są jednakowe")
                    else:
                        data[username] = password
                        userdata = {}
                        save_obj(userdata, username)
                        save_obj(data, 'users')
                        controller.show_frame("Login")

        def register_user(input_user, input_password, input_password_repeat):

            provided_username = input_user.get()
            provided_password = input_password.get()
            provided_password_repeat = input_password_repeat.get()

            if check_username(provided_username):
                check_password(provided_username, provided_password, provided_password_repeat)

        def display_error(error_message):
            self.last_error_label.destroy()
            self.last_error_label = tk.Label(self, text=error_message)
            self.last_error_label.grid(row=8, column=2)

    def on_show_frame(self, event):

        self.last_error_label.destroy()
