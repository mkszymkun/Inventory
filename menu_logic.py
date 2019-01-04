#!/usr/bin/python3

# Inventory - inventory management program

from graphics import Graphics
from list_of_items_logic import ListOfItemsLogic
from users_reservations_list_logic import UsersReservationsListLogic
from items_search_results_logic import ItemsSearchResultsLogic


class MenuLogic:

    def __init__(self, controller):

        self.controller = controller

    def display_menu_button(self, text, frame, row):
        Graphics.menu_button(
            self, text, lambda: MenuLogic.menu_button_click(self, frame), row)

    def menu_button_click(self, frame):
        MenuLogic.clear_selections(self)
        self.controller.show_frame(frame)
        self.controller.show_frame("EmptyFrameRight")

    def clear_selections(self):

        ListOfItemsLogic.last_chosen_item = ''
        ListOfItemsLogic.last_chosen_location = ''

        ItemsSearchResultsLogic.last_selected_item = ''
        ItemsSearchResultsLogic.last_selected_location = ''

        UsersReservationsListLogic.last_chosen_item = ''
        UsersReservationsListLogic.last_chosen_location = ''

    def display_logout_button(self, text, row):
        Graphics.logout_button(self, text, lambda: MenuLogic.logout(self), row)

    def logout(self):
        self.controller.show_frame("EmptyFrameRight")
        self.controller.show_frame("EmptyFrameLeft")
        self.controller.show_frame("LoginView")
