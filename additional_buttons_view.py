#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
from additional_buttons_logic import AdditionalButtonsLogic
from graphics import Graphics


class AdditionalButtonsView(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):
        for widget in self.winfo_children():
            widget.destroy()

        if AdditionalButtonsLogic.caller == 'ListOfItemsLogic':
            AdditionalButtonsLogic.print_buttons(
                self, AdditionalButtonsLogic.chosen_location,
                AdditionalButtonsLogic.chosen_item)

        elif AdditionalButtonsLogic.caller == 'UsersReservationsListLogic':
            AdditionalButtonsLogic.print_buttons_private(
                self, AdditionalButtonsLogic.chosen_location,
                AdditionalButtonsLogic.chosen_item)

        elif AdditionalButtonsLogic.caller == 'ItemsSearchResultsLogic':
            AdditionalButtonsLogic.print_buttons_search\
                (self, AdditionalButtonsLogic.chosen_location,
                 AdditionalButtonsLogic.chosen_item)

        for i in range(11, 33):
            Graphics.empty_row(self, i, 1)
