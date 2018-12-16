#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
from graphics import Graphics
from file_access import FileAccess


class RegisterUserLogic(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

    def register_user(self, username_input_field, password_input_field, password_repeat_input_field):

        provided_username = username_input_field.get()
        provided_password = password_input_field.get()
        provided_password_repeat = password_repeat_input_field.get()

        if RegisterUserLogic.check_username(self, provided_username):
            if RegisterUserLogic.check_password(self, provided_password, provided_password_repeat):
                users_and_passwords_data = FileAccess.load_users_and_passwords_data(self)
                users_and_passwords_data[provided_username] = provided_password
                FileAccess.save_users_and_passwords_data(self, users_and_passwords_data)
                users_private_list = {}
                FileAccess.save_obj(self, users_private_list, provided_username)
                self.controller.show_frame("LoginView")

    def check_username(self, username):

        if len(username) < 6:
            Graphics.display_registration_error(self, "Nazwa za krótka (min 6)")
        elif len(username) >= 6:

            if not username.isalnum():
                Graphics.display_registration_error(self, "Nazwa może zawierać litery i cyfry")

            else:
                users_and_passwords_data = FileAccess.load_users_and_passwords_data(self)
                if username in users_and_passwords_data.keys():
                    Graphics.display_registration_error(self, "Nazwa zajęta")
                else:
                    return True

    def check_password(self, password, password2):

        if len(password) < 6:
            Graphics.display_registration_error(self, "Hasło za krótkie (min 6)")

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
                Graphics.display_registration_error(self, "Hasło musi zawierać litery i cyfry")
            elif not invalid_character:
                if password != password2:
                    Graphics.display_registration_error(self, "Hasła nie są jednakowe")
                else:
                    return True
