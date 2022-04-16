"""
    @Author: Viney Khaneja
    @Date: 2022-04-14 15:05PM
    @Last Modified by: Viney Khaneja
    @Last Modified time: None
    @Title : Multiple Address Book
"""

# Importing reduce
from functools import reduce
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
    """
        Description: Fetch all the person details, who belongs to entered city or state 
        Parameters: addressbook_dict : The dictionary in which all these contacts details to be stored
        Returns: None, just prints the person details present in particular city or state
    """
    try:
        entered_city_or_state = input(
            "Please enter a city or state for searching a person: ")
        if searching_dict:
            for key, value in searching_dict.items():
                list_by_city_or_state = list(filter(lambda x: (
                    x.city == entered_city_or_state or x.state == entered_city_or_state), value))
                if len(list_by_city_or_state) > 0:
                    for item in list_by_city_or_state:
                        print(str(item))
                else:
                    print(
                        f"No person from {key} belongs to this city or state")
        else:
            raise Custom_Exception_AddressBook(
                "Dictionary is empty as of now, Please enter details first")
    except Exception as ex:
        print(ex)


def dictionary_of_city_and_person(searching_dict):
    """
        Description: Store all the persons in Dictionary with city name as keys and person details as values
        Parameters: searching_dict : The dictionary in which all these contacts details to be stored
        Returns: city_person_dict
    """
    try:
        if searching_dict:
            city_person_dict = {}
            for contacts_list in searching_dict.values():
                list(map(lambda x: city_person_dict.setdefault(
                    x.city, []).append(x), contacts_list))
            return city_person_dict
        else:
            raise Custom_Exception_AddressBook(
                "Dictionary is empty as of now, Please enter details first")
    except Exception as ex:
        print(ex)


def dictionary_of_state_and_person(searching_dict):
    """
        Description: Store all the persons in Dictionary with state name as keys and person details as values
        Parameters: searching_dict : The dictionary in which all these contacts details to be stored
        Returns: state_person_dict
    """
    try:
        if searching_dict:
            state_person_dict = {}
            for contacts_list in searching_dict.values():
                list(map(lambda x: state_person_dict.setdefault(
                    x.state, []).append(x), contacts_list))
            return state_person_dict
        else:
            raise Custom_Exception_AddressBook(
                "Dictionary is empty as of now, Please enter details first")
    except Exception as ex:
        print(ex)


def sorting_entries_by_name(add_book_dict):
    """
        Description: Sorting all the persons by name across multiple AddressBook and stores it in a sorted list
        Parameters: add_book_dict : The dictionary in which all these contacts details to be stored
        Returns: sorted_list
    """
    try:
        contacts_list = list(add_book_dict.values())
        sorted_list = reduce(lambda x, y: x+y, contacts_list)
        sorted_list.sort(key=lambda x: x.first_name)
        return sorted_list
    except Exception as ex:
        print(ex)


def sorting_entries_by_city(add_book_dict):
    """
        Description: Sorting all the persons by city name across multiple AddressBook and stores it in a sorted list
        Parameters: add_book_dict : The dictionary in which all these contacts details to be stored
        Returns: sorted_list
    """
    try:
        contacts_list = list(add_book_dict.values())
        sorted_list = reduce(lambda x, y: x+y, contacts_list)
        sorted_list.sort(key=lambda x: x.city)
        return sorted_list
    except Exception as ex:
        print(ex)


def sorting_entries_by_state(add_book_dict):
    """
        Description: Sorting all the persons by state name across multiple AddressBook and stores it in a sorted list
        Parameters: add_book_dict : The dictionary in which all these contacts details to be stored
        Returns: sorted_list
    """
    try:
        contacts_list = list(add_book_dict.values())
        sorted_list = reduce(lambda x, y: x+y, contacts_list)
        sorted_list.sort(key=lambda x: x.state)
        return sorted_list
    except Exception as ex:
        print(ex)


def sorting_entries_by_zip(add_book_dict):
    """
        Description: Sorting all the persons by zip name across multiple AddressBook and stores it in a sorted list
        Parameters: add_book_dict : The dictionary in which all these contacts details to be stored
        Returns: sorted_list
    """
    try:
        contacts_list = list(add_book_dict.values())
        sorted_list = reduce(lambda x, y: x+y, contacts_list)
        sorted_list.sort(key=lambda x: x.zip)
        return sorted_list
    except Exception as ex:
        print(ex)


def printing_details_on_console(list_to_be_printed):
    """
        Description: Printing the person details on console, which is stored as object in lists
        Parameters: list_to_be_printed : List that  needs to be printed
        Returns: None,just displays the person details on console
    """
    for item in list_to_be_printed:
        print(str(item))


if __name__ == "__main__":
    address_book_dict = {}
    while True:
        user_choice = int(input(
            "\"1\" for Adding Contact Details...\n\"2\" for searching the person in city or state...\n\"3\" for viewing person from a city...\n\"4\" for viewing person from a state...\n\"5\" for sorting person by first name...\n\"6\" for sorting person by city name...\n\"7\" for sorting person by state name...\n\"8\" for sorting person by zip...\n\"ANY OTHER KEY\" for exiting..."))
        if user_choice == 1:
            adding_contactslist_in_dict(address_book_dict)
            for key, value in address_book_dict.items():
                print("Address Book Name is: ", key)
                printing_details_on_console(value)
            continue
        if user_choice == 2:
            search_person_in_a_city_state(address_book_dict)
            continue
        if user_choice == 3:
            cityperson_dict = dictionary_of_city_and_person(address_book_dict)
            for key, value in cityperson_dict.items():
                print(
                    f"Total Number of Persons residing in {key} city are: {len(value)} and details of those are: ")
                printing_details_on_console(value)
            continue
        if user_choice == 4:
            stateperson_dict = dictionary_of_state_and_person(
                address_book_dict)
            for key, value in stateperson_dict.items():
                print(
                    f"Total Number of Persons residing in {key} state are: {len(value)} and details of those are: ")
                printing_details_on_console(value)
            continue
        if user_choice == 5:
            sorted_by_name_list = sorting_entries_by_name(address_book_dict)
            printing_details_on_console(sorted_by_name_list)
            continue
        if user_choice == 6:
            sorted_by_city_list = sorting_entries_by_city(address_book_dict)
            printing_details_on_console(sorted_by_city_list)
            continue
        if user_choice == 7:
            sorted_by_state_list = sorting_entries_by_state(address_book_dict)
            printing_details_on_console(sorted_by_state_list)
            continue
        if user_choice == 8:
            sorted_by_zip_list = sorting_entries_by_zip(address_book_dict)
            printing_details_on_console(sorted_by_zip_list)
            continue
        if user_choice is not 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
            break
