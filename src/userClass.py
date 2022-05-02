##
# EPITECH PROJECT, 2021
# B-MAT-500-COT-5-1-302separation-charmeel.vodouhe
# File description:
# userClass
##

import errors


class User:
    def __init__(self, name):
        self.name = name
        self.contactList = list()

    def __str__(self):
        return (f"User({self.name})")

    def __repr__(self):
        return (f"User(Name={self.name}, ContactList={self.contactList})")

    def addContact(self, contact):
        if (not isinstance(contact, User)) or contact.name == self.name:
            errors.report("Error: User linked to himself")
        elif not (contact in self.contactList):
            self.contactList.append(contact)

    def __eq__(self, other):
        if (isinstance(other, User)):
            return (self.name == other.name)
        return (False)

    def __lt__(self, other):
        if (isinstance(other, User)):
            return (self.name < other.name)
        return (False)
