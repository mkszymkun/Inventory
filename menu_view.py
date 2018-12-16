#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
from graphics import Graphics
from menu_logic import MenuLogic


class MenuView(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        Graphics.menu_header(self)

        Graphics.empty_row(self, 2, 1)

        MenuLogic.display_menu_button(self, "Materiały", "ListOfItemsView", 3)

        MenuLogic.display_menu_button(self, "Wyszukiwarka","SearchForItemsView", 4)

        MenuLogic.display_menu_button(self, "Magazyny", "ListOfLocationsView", 5)

        MenuLogic.display_menu_button(self, "Moje rezerwacje","UsersReservationsListView", 6)

        Graphics.empty_row(self, 7, 1)

        MenuLogic.display_logout_button(self, "Wyloguj", 8)

