"""
    @Author: Viney Khaneja
    @Date: 2022-04-14 15:05PM
    @Last Modified by: Viney Khaneja
    @Last Modified time: None
    @Title : Multiple Address Book
"""

from os import execl
# Importing Exception class
from Custom_Exception import Custom_Exception_AddressBook

# Importing Address Book
import address_book

# Importing Contacts Class
from contacts import Contacts


def adding_contactslist_in_dict(addressbook_dict):
    """
        Description: Adding Address Book name as key & Contact Details as value in Dictionary
        Parameters: addressbook_dict : The dictionary in which all these contacts details to be stored
        Returns: Returns A filled dictionary, taking inputs from console
    """
    try:
        while True:
            name_of_address_book = input("Enter the name of addressBook: ")
            for book_name in addressbook_dict.keys():
                if book_name == name_of_address_book:
                    raise Custom_Exception_AddressBook(
                        "This addressBook name already exists")
            list_of_particular_addressbook = address_book.contacts_list_maker()
            addressbook_dict[name_of_address_book] = list_of_particular_addressbook
            choice = input(
                "Enter the choice u want to add more address Books or not \"Y\" OR \"N\": ").upper()
            if choice == "N":
                break
    except Exception as ex:
        print(ex)
        adding_contactslist_in_dict(addressbook_dict)


def search_person_in_a_city_state(searching_dict):
    try:
        entered_city_or_state = input(
            "Please enter a city or state for searching a person: ")
        for key, value in searching_dict.items():
            lis1 = list(filter(lambda x: (
                x.city == entered_city_or_state or x.state == entered_city_or_state), value))
            if len(lis1) > 0:
                for item in lis1:
                    print(str(item))
            else:
                print(f"No person from {key} belongs to this city or state")
    except Exception as ex:
        print(ex)


def dictionary_of_city_and_person(searching_dict):
    try:
        city_person_dict = {}
        for contacts_list in searching_dict.values():
            list(map(lambda x: city_person_dict.setdefault(
                x.city, []).append(x), contacts_list))
        return city_person_dict
    except Exception as ex:
        print(ex)


def dictionary_of_state_and_person(searching_dict):
    try:
        state_person_dict = {}
        for contacts_list in searching_dict.values():
            list(map(lambda x: state_person_dict.setdefault(
                x.state, []).append(x), contacts_list))
        return state_person_dict
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    address_book_dict = {}
    adding_contactslist_in_dict(address_book_dict)
    for key, value in address_book_dict.items():
        print("Address Book Name is: ", key)
        for item in value:
            print(str(item))
    # search_person_in_a_city_state(address_book_dict)
    cityperson_dict = dictionary_of_city_and_person(address_book_dict)
    for key, value in cityperson_dict.items():
        print("Persons residing in ", key, " city are:")
        for each_contact in value:
            print(str(each_contact))
    stateperson_dict = dictionary_of_state_and_person(address_book_dict)
    for key, value in stateperson_dict.items():
        print("Persons residing in ", key, " state are:")
        for each_contact in value:
            print(str(each_contact))
