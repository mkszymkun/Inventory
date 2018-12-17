#!/usr/bin/python3

# Inventory - inventory management program

import pickle


class FileAccess:

    def __init__(self, controller):
        self.controller = controller

    # Saving/loading data

    def save_obj(self, obj, name):
        with open(name + '.pkl', 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

    def load_obj(self, name):
        with open(name + '.pkl', 'rb') as f:
            return pickle.load(f)

    def save_item_location_data(self, obj):
        with open('item_location_data.pkl', 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

    def load_item_location_data(self):
        with open('item_location_data.pkl', 'rb') as f:
            return pickle.load(f)

    def save_users_and_passwords_data(self, obj):
        with open('users.pkl', 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

    def load_users_and_passwords_data(self):
        with open('users.pkl', 'rb') as f:
            return pickle.load(f)

    def save_user_data(self, obj):
        username = self.controller.get_page("LoginView").username
        with open(username + '.pkl', 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

    def load_user_data(self):
        username = self.controller.get_page("LoginView").username
        with open(username + '.pkl', 'rb') as f:
            return pickle.load(f)

    #

    def remove_location(self, input_location, output_list):
        output_list.pop(input_location.lower())
        FileAccess.save_item_location_data(self, output_list)



