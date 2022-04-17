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
from this import d
# Importing Exception class
from Custom_Exception import Custom_Exception_AddressBook
# Importing CSV & Json
import csv
import json
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
    try:
        for item in list_to_be_printed:
            print(str(item))
    except Exception as ex:
        print(ex)


def writing_address_book_details_text_file(writing_dict):
    """
        Description: Writing the person details to text file
        Parameters: Address Book Dictionary
        Returns: None,just writes to file
    """
    try:
        for key, value in writing_dict.items():
            with open("addressBookDetails.txt", "a") as write_text:
                write_text.write(f"Address Book name is:{key}\n")
                for item in value:
                    write_text.write(str(item))
                    write_text.write("\n")
    except IOError as ex:
        print(ex)
    except Exception as ex:
        print(ex)


def reading_address_book_details_text_file():
    """
        Description: Reading the person details to console from Text File
        Parameters: None
        Returns: None,just reades to console from file
    """
    try:
        with open("addressBookDetails.txt", "r") as read_text:
            print(read_text.read())
    except IOError as ex:
        print(ex)
    except Exception as ex:
        print(ex)


def writing_address_book_details_csv_file(writing_dict):
    """
        Description: Writing the person details to CSV file
        Parameters: Address Book Dictionary
        Returns: None,just writes to file
    """
    try:
        csv_columns = ["AddressBook Name", "First Name", "Last Name", "Address",
                       "City", "State", "Zip", "Phone Number", "Email"]
        with open("addressbookdetails.csv", "a") as write_csv:
            csvwriter = csv.writer(write_csv)
            csvwriter.writerow(csv_columns)
            for key, value in writing_dict.items():
                for item in value:
                    contact_row = [key, item.first_name, item.last_name, item.address,
                                   item.city, item.state, item.zip, item.phone_number, item.email]
                    csvwriter.writerow(contact_row)
    except IOError as ex:
        print(ex)
    except Exception as ex:
        print(ex)


def reading_address_book_details_csv_file():
    """
        Description: Reading the person details to console from CSV File
        Parameters: None
        Returns: None,just reades to console from file
    """
    try:
        with open("addressbookdetails.csv", "r") as read_csv:
            csvFile = csv.reader(read_csv)
            for lines in csvFile:
                print(lines)
    except IOError as ex:
        print(ex)
    except Exception as ex:
        print(ex)


def writing_address_book_details_json_file(writing_dict):
    """
        Description: Writing the person details to JSON File
        Parameters: None
        Returns: None,just writes to file
    """
    try:
        # Initializing dictionary which would have Json Serialized objects of conatcts clas.
        json_dict = {}
        for key, value in writing_dict.items():
            for item in value:
                # Making my Conatcts class Json Serializable for dumping in Json File
                json_obj = item.toJson()
                # Appending Elements to json_dict, which is to be converted into Json File
                json_dict.setdefault(key, []).append(json_obj)
        with open("addressbookdetails.json", "w") as write_json:
            json.dump(json_dict, write_json, indent=4)
    except IOError as ex:
        print(ex)
    except Exception as ex:
        print(ex)


def reading_address_book_details_json_file():
    """
        Description: Reading the person details to console from JSON File
        Parameters: None
        Returns: None,just reades to console from file
    """
    try:
        with open("addressbookdetails.json", "r") as read_json:
            data = json.load(read_json)
            print(data)
    except IOError as ex:
        print(ex)


if __name__ == "__main__":
    contact1 = Contacts("Viney", "Khaneja", "kalanaur", "Panipat",
                        "Punjab", "124113", "91 7206594149", "vineykhaneja999gmail.com")
    contact2 = Contacts("Aman", "Gupta", "jagdishcolony", "Rohtak",
                        "Haryana", "124001", "91 9991661664", "amangpta123gmail.com")
    contact3 = Contacts("Sidharth", "Madaan", "busstand", "Sonepat",
                        "Punjab", "122001", "91 9466365917", "sidhumoosa129gmail.com")
    contact4 = Contacts("Papplu", "Sharma", "parichowk", "Jind",
                        "Haryana", "156301", "91 9215214254", "sharmagpta123gmail.com")
    # This dictionary is being used to read & write data into files(Text,CSV,JSON)
    addressbookdict = {"Evehi": [contact1, contact2], "Jigri":
                       [contact3, contact4]}
    address_book_dict = {}
    while True:
        user_choice = int(input(
            "\"1\" for Adding Contact Details...\n\"2\" for searching the person in city or state...\n"
            "\"3\" for viewing person from a city...\n\"4\" for viewing person from a state...\n"
            "\"5\" for sorting person by first name...\n\"6\" for sorting person by city name...\n"
            "\"7\" for sorting person by state name...\n\"8\" for sorting person by zip...\n"
            "\"9\" for writing details in addressbookdetails.txt...\n\"10\" for reading details to console from addressbookDetails.txt...\n"
            "\"11\" for writing details to CSV file in addressbookdetails.csv...\n\"12\" for reading details to console from addressbookdetails.csv...\n"
            "\"13\" for writing details to JSON in addressbookdetails.json...\n\"14\" for reading details to console from addressbookdetails.json...\n"
            "\"ANY OTHER KEY\" for exiting..."))
        if user_choice == 1:
            adding_contactslist_in_dict(address_book_dict)
            for key, value in address_book_dict.items():
                print("Address Book Name is: ", key)
                printing_details_on_console(value)
            continue
        elif user_choice == 2:
            search_person_in_a_city_state(address_book_dict)
            continue
        elif user_choice == 3:
            cityperson_dict = dictionary_of_city_and_person(address_book_dict)
            for key, value in cityperson_dict.items():
                print(
                    f"Total Number of Persons residing in {key} city are: {len(value)} and details of those are: ")
                printing_details_on_console(value)
            continue
        elif user_choice == 4:
            stateperson_dict = dictionary_of_state_and_person(
                address_book_dict)
            for key, value in stateperson_dict.items():
                print(
                    f"Total Number of Persons residing in {key} state are: {len(value)} and details of those are: ")
                printing_details_on_console(value)
            continue
        elif user_choice == 5:
            sorted_by_name_list = sorting_entries_by_name(address_book_dict)
            printing_details_on_console(sorted_by_name_list)
            continue
        elif user_choice == 6:
            sorted_by_city_list = sorting_entries_by_city(address_book_dict)
            printing_details_on_console(sorted_by_city_list)
            continue
        elif user_choice == 7:
            sorted_by_state_list = sorting_entries_by_state(address_book_dict)
            printing_details_on_console(sorted_by_state_list)
            continue
        elif user_choice == 8:
            sorted_by_zip_list = sorting_entries_by_zip(address_book_dict)
            printing_details_on_console(sorted_by_zip_list)
            continue
        elif user_choice == 9:
            writing_address_book_details_text_file(addressbookdict)
            continue
        elif user_choice == 10:
            reading_address_book_details_text_file()
            continue
        elif user_choice == 11:
            writing_address_book_details_csv_file(addressbookdict)
            continue
        elif user_choice == 12:
            reading_address_book_details_csv_file()
            continue
        elif user_choice == 13:
            writing_address_book_details_json_file(addressbookdict)
            continue
        elif user_choice == 14:
            reading_address_book_details_json_file()
            continue
        else:
            break
