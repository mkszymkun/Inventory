#!/usr/bin/python3

# Inventory - inventory management program

from graphics import Graphics
from file_access import FileAccess


class RegisterUserLogic:

    def __init__(self, controller):

        self.controller = controller

    def register_user(self, username, password):

        users_and_passwords_data \
            = FileAccess.load_users_and_passwords_data(self)
        users_and_passwords_data[username] = password
        FileAccess.save_users_and_passwords_data(
            self, users_and_passwords_data)
        users_private_list = {}
        FileAccess.save_obj(self, users_private_list,
                            username)
        self.controller.show_frame("LoginView")

    def check_registration_data(self, username_input_field,
                                password_input_field,
                                password_repeat_input_field):

        provided_username = username_input_field.get()
        provided_password = password_input_field.get()
        provided_password_repeat = password_repeat_input_field.get()

        if RegisterUserLogic.check_username(self, provided_username) \
                and RegisterUserLogic.check_password(self, provided_password,
                                                provided_password_repeat):

            RegisterUserLogic.register_user(self, provided_username,
                                            provided_password)

    def check_username_length(self, username):

        if len(username) < 6:
            Graphics.display_registration_error(
                self, "Nazwa za krótka (min 6)")
            return False
        else:
            return True

    def check_username_characters(self, username):

        if not username.isalnum():
            Graphics.display_registration_error(
                self, "Nazwa może zawierać litery i cyfry")
            return False
        else:
            return True

    def check_username_availability(self, username):

        users_and_passwords_data \
            = FileAccess.load_users_and_passwords_data(self)
        if username in users_and_passwords_data.keys():
            Graphics.display_registration_error(self, "Nazwa zajęta")
            return False
        else:
            return True

    def check_username(self, username):

        return RegisterUserLogic.check_username_length(self,
                                                       username) \
               and RegisterUserLogic.check_username_characters(self,
                                                               username) \
               and RegisterUserLogic.check_username_availability(self,
                                                                 username)

    def check_password_length(self, password):

        if len(password) < 6:
            Graphics.display_registration_error(
                self, "Hasło za krótkie (min 6)")
            return False
        else:
            return True

    def check_password_letter(self, password):

        for char in password:
            if char.isalpha():
                return True
        Graphics.display_registration_error(
            self, "Hasło musi zawierać litery i cyfry")
        return False

    def check_password_number(self, password):

        for char in password:
            if char.isdecimal():
                return True
        Graphics.display_registration_error(
            self, "Hasło musi zawierać litery i cyfry")
        return False

    def check_password_invalid_char(self, password):

        for char in password:
            if not char.isalpha() and not char.isdecimal:
                return True
        return False

    def check_password_repeat(self, password, password2):

        if password != password2:
            Graphics.display_registration_error(
                self, "Hasła nie są jednakowe")
            return False
        else:
            return True

    def check_password(self, password, password2):

        if RegisterUserLogic.check_password_length(self, password):
            if RegisterUserLogic.check_password_letter(self, password):
                if RegisterUserLogic.check_password_number(self, password):
                    if not RegisterUserLogic.check_password_invalid_char(
                            self, password):
                        if RegisterUserLogic.check_password_repeat(
                                self, password, password2):
                            return True
                        else:
                            Graphics.display_registration_error(
                                        self, "Hasła nie są jednakowe")
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
