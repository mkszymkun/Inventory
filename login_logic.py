#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle
from file_access import FileAccess
from graphics import Graphics


class LoginLogic(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

    def log_in(self, username_input_field, password_input_field):

        provided_username = username_input_field.get()
        provided_password = password_input_field.get()

        users_and_passwords_data = FileAccess.load_users_and_passwords_data(self)

        if provided_username in users_and_passwords_data.keys():
            if users_and_passwords_data[provided_username] == provided_password:
                self.username = provided_username
                self.controller.show_frame("MenuView")
                self.controller.show_frame("EmptyFrameBot")
                self.controller.show_frame("Title")
            else:
                Graphics.display_login_error(self, "Błędne hasło")
        else:
            Graphics.display_login_error(self, "Użytkownik nie istnieje")
