#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle
from file_access import FileAccess
from graphics import Graphics
from register_user_logic import RegisterUserLogic


class RegisterUserView(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        Graphics.login_header(self, "REJESTRACJA")

        Graphics.empty_row(self, 2, 1)
        Graphics.login_label(self, "Login:", 3, 1)

        input_user = tk.Entry(self)
        input_user.grid(row=3, column=2)

        Graphics.empty_row(self, 4, 1)
        Graphics.login_label(self, "Hasło:", 5, 1)

        input_pword = tk.Entry(self, show='*')
        input_pword.grid(row=5, column=2)

        Graphics.empty_row(self, 6, 1)
        Graphics.login_label(self, "Powtórz hasło:", 7, 1)

        input_pword2 = tk.Entry(self, show='*')
        input_pword2.grid(row=7, column=2)

        self.last_error_label = tk.Label(self)
        self.last_error_label.grid(row=8, column=1)

        Graphics.empty_row(self, 9, 1)
        Graphics.login_button(self, "Zarejestruj", lambda: RegisterUserLogic.register_user(self, input_user, input_pword, input_pword2), 10)
        Graphics.login_button(self, "Wróć", lambda: controller.show_frame("LoginView"), 11)

    def on_show_frame(self, event):

        self.last_error_label.destroy()
