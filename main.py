#!/usr/bin/python3

# Inventory - inventory management program

import tkinter as tk
from file_access import FileAccess

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
        bgcolor = '#303030'

        container = tk.Frame(self, bg=bgcolor)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        container.grid(row=0, column=0, sticky="nsew")

        container_top = tk.Frame(container, bg=bgcolor)
        container_top.grid(row=0, column=0, columnspan=3)

        container_left = tk.Frame(container, bg=bgcolor)
        container_left.grid(row=1, column=0)

        container_bot = tk.Frame(container, bg=bgcolor)
        container_bot.grid(row=1, column=1)

        container_right = tk.Frame(container, bg=bgcolor)
        container_right.grid(row=1, column=2)

        try:
            FileAccess.load_item_location_data(self)
        except FileNotFoundError:
            item_location_data = {}
            FileAccess.save_item_location_data(self, item_location_data)

        try:
            FileAccess.load_users_and_passwords_data(self)
        except FileNotFoundError:
            users = {}
            FileAccess.save_users_and_passwords_data(self, users)

        self.frames = {}

        for F in (ListOfItemsView, SearchForItemsView, ItemsSearchResultsView,
                  ListOfLocationsView, LoginView, UsersReservationsListView,
                  RegisterUserView, ConfirmLocationRemovalView):

            cont = F.__name__

            frame = F(container_bot, self)

            self.frames[cont] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            frame.config(bg=bgcolor)

        self.frames["EmptyFrameLeft"] = EmptyFrameView(parent=container_left,
                                                       controller=self)
        self.frames["EmptyFrameLeft"].config(bg=bgcolor)
        self.frames["EmptyFrameLeft"].grid(row=0, column=0, sticky="nsew")

        self.frames["EmptyFrameRight"] = EmptyFrameView(parent=container_right,
                                                        controller=self)
        self.frames["EmptyFrameRight"].config(bg=bgcolor)
        self.frames["EmptyFrameRight"].grid(row=0, column=0, sticky="nsew")

        self.frames["AdditionalButtonsView"] = AdditionalButtonsView(
            parent=container_right, controller=self)
        self.frames["AdditionalButtonsView"].config(bg=bgcolor)
        self.frames["AdditionalButtonsView"].grid(row=0, column=0,
                                                  sticky="nsew")

        self.frames["EmptyFrameTop"] = EmptyFrameView(parent=container_top,
                                                      controller=self)
        self.frames["EmptyFrameTop"].config(bg=bgcolor)
        self.frames["EmptyFrameTop"].grid(row=0, column=0, sticky="nsew")

        self.frames["EmptyFrameBot"] = EmptyFrameView(parent=container_bot,
                                                      controller=self)
        self.frames["EmptyFrameBot"].config(bg=bgcolor)
        self.frames["EmptyFrameBot"].grid(row=0, column=0, sticky="nsew")

        self.frames["MenuView"] = MenuView(parent=container_left,
                                           controller=self)
        self.frames["MenuView"].config(bg=bgcolor)
        self.frames["MenuView"].grid(row=0, column=0, sticky="nsew")

        self.frames["Title"] = TitleView(parent=container_top, controller=self)
        self.frames["Title"].config(bg=bgcolor)
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
app.config(bg='#303030')

app.mainloop()
