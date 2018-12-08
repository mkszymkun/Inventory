#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle
from graphics import Graphics
from file_access import FileAccess
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

        tk.Button(self, text="Wyloguj", font='Arial 10', width=50, height=6, relief='groove',
                  command=lambda: MenuLogic.logout(self)).grid(row=8, column=1)
