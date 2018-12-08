#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle
from file_access import FileAccess
from graphics import Graphics
from users_reservations_list_logic import UsersReservationsListLogic
from additional_buttons_logic import AdditionalButtonsLogic


class UsersReservationsListView(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):

        for widget in self.winfo_children():
            widget.destroy()

        Graphics.login_header(self, "MOJE REZERWACJE")
        Graphics.empty_row(self, 2, 1)

        reservation_data = FileAccess.load_user_data(self)

        UsersReservationsListLogic.locations_row = 3

        for location in reservation_data.keys():
            UsersReservationsListLogic.display_location_name_button(self, location)

        if AdditionalButtonsLogic.called:
            AdditionalButtonsLogic.called = False
            UsersReservationsListLogic.location_chosen = True
            UsersReservationsListLogic.chosen_location = AdditionalButtonsLogic.chosen_location
            self.controller.show_frame("UsersReservationsListView")

        if UsersReservationsListLogic.location_chosen:
            UsersReservationsListLogic.display_items_buttons(self)
