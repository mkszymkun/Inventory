#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
from tkinter import font as tkfont
from graphics import Graphics
from confirm_location_removal_logic import ConfirmLocationRemovalLogic


class ConfirmLocationRemovalView(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):

        location_to_delete = self.controller.get_page(
            "ListOfLocationsView").location_to_delete

        font = tkfont.Font(family='Ubuntu', size=25, weight="bold")
        image = tk.PhotoImage(file="pictures/labels/login_header.png")
        label = tk.Label(self, text="USUNĄĆ {}?".format(
            location_to_delete.upper()), font=font, image=image,
                         borderwidth='0', bg='#303030',  fg='white',
                         activebackground='#303030',  compound='center',
                         highlightbackground='#303030',
                 relief='groove')
        label.image = image
        label.grid(row=1, column=1)

        Graphics.empty_row(self, 2, 1)

        Graphics.warning(
            self, "Cała zawartość magazynu zostanie usunięta.", 3, 1)

        ConfirmLocationRemovalLogic.button_delete_location(
            self, "Usuń", location_to_delete, 8)

        ConfirmLocationRemovalLogic.button_go_back(self, "Wróć", 9)
