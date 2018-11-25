#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle


class Login(tk.Frame):

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

        empty_row(0, 1)
        header("LOGOWANIE")

        empty_row(2, 1)
        label("Login:", 3, 1)

        input_username = tk.Entry(self)
        input_username.grid(row=3, column=2)

        empty_row(4, 1)
        label("Hasło:", 5, 1)

        input_pword = tk.Entry(self, show='*')
        input_pword.grid(row=5, column=2)

        self.last_error_label = tk.Label(self)
        self.last_error_label.grid(row=6, column=1)
        empty_row(7, 1)

        button_login = tk.Button(self, text="Zaloguj", font='Arial 10', width=30, height=4, relief='groove',
                                 command=lambda: log_in(input_username, input_pword)).grid(row=8, column=0, columnspan=4)

        button_register = tk.Button(self, text="Załóż konto", font='Arial 10', width=30, height=4, relief='groove',
                                    command=lambda: controller.show_frame("Register")).grid(row=9, column=0, columnspan=4)

        button_quit = tk.Button(self, text="Wyjście", font='Arial 10', width=30, height=4, relief='groove',
                                command=lambda: controller.destroy()).grid(row=10, column=0, columnspan=4)

        def log_in(input_user, input_password):

            provided_username = input_user.get()
            provided_password = input_password.get()

            data = load_obj('users')

            if provided_username in data.keys():
                if data[provided_username] == provided_password:
                    self.username = provided_username
                    controller.show_frame("MainMenu")
                else:
                    display_error("Błędne hasło")
            else:
                display_error("Użytkownik nie istnieje")

        def display_error(error_message):
            self.last_error_label.destroy()
            self.last_error_label = tk.Label(self, text=error_message)
            self.last_error_label.grid(row=6, column=2)

        def load_obj(name):
            with open(name + '.pkl', 'rb') as f:
                return pickle.load(f)


    def on_show_frame(self, event):

        self.last_error_label.destroy()
