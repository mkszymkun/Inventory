#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle
from file_access import FileAccess
from graphics import Graphics
from search_for_items_logic import SearchForItemsLogic


class SearchForItemsView(tk.Frame):

    item_to_find = ''

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):

        for widget in self.winfo_children():
            widget.destroy()

        Graphics.login_header(self, "WYSZUKIWARKA")

        Graphics.empty_row(self, 2, 1)

        the_input_search = tk.Entry(self, width=50)
        the_input_search.grid(row=3, column=0, columnspan=4)

        Graphics.search_button(self, lambda: SearchForItemsLogic.find_item(self, the_input_search))
