#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle
from file_access import FileAccess
from graphics import Graphics


class SearchForItemsLogic(tk.Frame):

    item_to_find = ''

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

    def find_item(self, user_input):

        item = user_input.get()

        SearchForItemsLogic.item_to_find = item
        self.controller.show_frame("ItemsSearchResultsView")
