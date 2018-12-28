#!/usr/bin/python3

# Inventory - inventory management program

from file_access import FileAccess
from graphics import Graphics


class LoginLogic:

    def __init__(self, controller):

        self.controller = controller

    def log_in(self, username):

        self.username = username
        self.controller.show_frame("MenuView")
        self.controller.show_frame("EmptyFrameBot")
        self.controller.show_frame("Title")

    def check_log_in_data(self, username_input_field, password_input_field):

        provided_username = username_input_field.get()
        provided_password = password_input_field.get()

        if LoginLogic.check_username_validity(self, provided_username):

            if LoginLogic.check_password_validity(self, provided_username,
                                               provided_password):
                LoginLogic.log_in(self, provided_username)

    def check_username_validity(self, username):

        users_and_passwords_data \
            = FileAccess.load_users_and_passwords_data(self)
        if username not in users_and_passwords_data.keys():
            Graphics.display_login_error(self, "Użytkownik nie istnieje")
            return False
        return True

    def check_password_validity(self, username, password):

        users_and_passwords_data \
            = FileAccess.load_users_and_passwords_data(self)
        if users_and_passwords_data[username] != password:
            Graphics.display_login_error(self, "Błędne hasło")
            return False
        return True
