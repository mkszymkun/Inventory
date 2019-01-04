#!/usr/bin/python3

# Inventory - inventory management program


class SearchForItemsLogic:

    item_to_find = ''

    def __init__(self, controller):

        self.controller = controller

    def find_item(self, user_input):

        item = user_input.get()

        SearchForItemsLogic.item_to_find = item
        self.controller.show_frame("ItemsSearchResultsView")
