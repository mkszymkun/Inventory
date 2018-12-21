#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
from login_logic import LoginLogic
from graphics import Graphics


class LoginView(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        Graphics.login_header(self, "LOGOWANIE")

        Graphics.empty_row(self, 2, 1)
        Graphics.login_label(self, "Login:", 3, 1)

        input_username = tk.Entry(self)
        input_username.grid(row=3, column=2)

        Graphics.empty_row(self, 4, 1)
        Graphics.login_label(self, "Hasło:", 5, 1)

        input_password = tk.Entry(self, show='*')
        input_password.grid(row=5, column=2)

        self.last_error_label = tk.Label(self,  bg='#303030')
        self.last_error_label.grid(row=6, column=1)

        Graphics.empty_row(self, 7, 1)
        Graphics.login_button(
            self, "Zaloguj", lambda: LoginLogic.log_in(
                self, input_username, input_password), 8)
        Graphics.login_button(
            self, "Załóż konto", lambda: controller.show_frame(
                "RegisterUserView"), 9)
        Graphics.login_button(self, "Wyjście",
                              lambda: controller.destroy(), 10)

        for i in range(11, 22):
            Graphics.empty_row(self, i, 1)


    def on_show_frame(self, event):

        self.last_error_label.destroy()
