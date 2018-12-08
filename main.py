#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
import pickle
from file_access import FileAccess
from graphics import Graphics

from menu_view import MenuView
from empty_frame_view import EmptyFrameView
from title_view import TitleView
from login_view import LoginView
from register_user_view import RegisterUserView
from list_of_items_view import ListOfItemsView
from list_of_locations_view import ListOfLocationsView
from users_reservations_list_view import UsersReservationsListView
from search_for_items_view import SearchForItemsView
from items_search_results_view import ItemsSearchResultsView
from confirm_location_removal_view import ConfirmLocationRemovalView
from additional_buttons_view import AdditionalButtonsView


class Main(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self, width=100, height=100)

        container.pack(padx=2, pady=2, expand=True)

        container.grid_rowconfigure(0, weight=0)
        container.grid_columnconfigure(0, weight=0)

        container_top = tk.Frame(container, background="green")
        container_bot = tk.Frame(container, background="yellow")
        container_left = tk.Frame(container, background="red")
        container_right = tk.Frame(container, background="blue")

        container_top.grid(row=0, column=0, columnspan=3)
        container_left.grid(row=1, column=0)
        container_bot.grid(row=1, column=1)
        container_right.grid(row=1, column=2)

        try:
            FileAccess.load_item_location_data(self)
        except:
            item_location_data = {}
            FileAccess.save_item_location_data(self, item_location_data)

        try:
            FileAccess.load_users_and_passwords_data(self)
        except:
            users = {}
            FileAccess.save_users_and_passwords_data(self, users)

        self.frames = {}

        for F in (ListOfItemsView, SearchForItemsView, ItemsSearchResultsView, ListOfLocationsView, LoginView, UsersReservationsListView, RegisterUserView, ConfirmLocationRemovalView):

            cont = F.__name__

            frame = F(container_bot, self)

            self.frames[cont] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.frames["EmptyFrameLeft"] = EmptyFrameView(parent=container_left, controller=self)
        self.frames["EmptyFrameLeft"].grid(row=0, column=0, sticky="nsew")

        self.frames["EmptyFrameRight"] = EmptyFrameView(parent=container_right, controller=self)
        self.frames["EmptyFrameRight"].grid(row=0, column=0, sticky="nsew")

        self.frames["AdditionalButtonsView"] = AdditionalButtonsView(parent=container_right, controller=self)
        self.frames["AdditionalButtonsView"].grid(row=0, column=0, sticky="nsew")

        self.frames["EmptyFrameTop"] = EmptyFrameView(parent=container_top, controller=self)
        self.frames["EmptyFrameTop"].grid(row=0, column=0, sticky="nsew")

        self.frames["EmptyFrameBot"] = EmptyFrameView(parent=container_bot, controller=self)
        self.frames["EmptyFrameBot"].grid(row=0, column=0, sticky="nsew")

        self.frames["MenuView"] = MenuView(parent=container_left, controller=self)
        self.frames["Title"] = TitleView(parent=container_top, controller=self)

        self.frames["MenuView"].grid(row=0, column=0, sticky="nsew")
        self.frames["Title"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("EmptyFrameLeft")
        self.show_frame("EmptyFrameRight")
        self.show_frame("Title")
        self.show_frame("LoginView")

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.event_generate("<<ShowFrame>>")
        frame.tkraise()

    def get_page(self, frame_class):
        return self.frames[frame_class]


app = Main()

app.mainloop()
