#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
from graphics import Graphics
from items_search_results_logic import ItemsSearchResultsLogic
from search_for_items_logic import SearchForItemsLogic


class ItemsSearchResultsView(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):

        for widget in self.winfo_children():
            widget.destroy()

        item = SearchForItemsLogic.item_to_find

        Graphics.search_results_label(self, item)

        Graphics.empty_row(self, 2, 1)

        ItemsSearchResultsLogic.display_results(self)
