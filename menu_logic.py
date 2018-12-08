#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle
from graphics import Graphics
from file_access import FileAccess
from list_of_items_logic import ListOfItemsLogic
from users_reservations_list_logic import UsersReservationsListLogic
from items_search_results_logic import ItemsSearchResultsLogic


class MenuLogic(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

    def logout(self):
        self.controller.show_frame("EmptyFrameRight")
        self.controller.show_frame("EmptyFrameLeft")
        self.controller.show_frame("LoginView")

    def clear_selections(self):

        ListOfItemsLogic.last_chosen_item = ''
        ListOfItemsLogic.last_chosen_location = ''

        ItemsSearchResultsLogic.last_selected_item = ''
        ItemsSearchResultsLogic.last_selected_location = ''

        UsersReservationsListLogic.last_chosen_item = ''
        UsersReservationsListLogic.last_chosen_location = ''


    def menu_button_click(self, frame):

        MenuLogic.clear_selections(self)
        self.controller.show_frame(frame)
        self.controller.show_frame("EmptyFrameRight")

    def display_menu_button(self, text, frame, row):
        Graphics.menu_button(self, text, lambda: MenuLogic.menu_button_click(self, frame), row)

