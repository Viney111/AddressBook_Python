"""
    @Author: Viney Khaneja
    @Date: 2022-04-13 20:05PM
    @Last Modified by: Viney Khaneja
    @Last Modified time: None
    @Title : Address_Book_Problem_Statement
"""

# Importing Contacts Class
from contacts import Contacts


def Add_conatcts_from_console():
    """
        Description: Adding Contact Details form Console & returning that details as an object of Contacts Class
        Parameters: None
        Returns: Returns Conatacts class object having all info
    """
    try:
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        address = input("Enter the address: ")
        city = input("Enter city name: ")
        state = input("Enter state name: ")
        zip = input("Enter zip code: ")
        phone_number = input("Enter phone_number: ")
        email = input("Enter email address: ")
        contact_obj = Contacts(first_name, last_name, address,
                               city, state, zip, phone_number, email)
        return contact_obj
    except Exception as ex:
        print(ex)


def Storing_contacts_in_list():
    """
        Description: Adding Contact Details form Console in list
        Parameters: None
        Returns: Returns a list containing objects of Contact Class that is taken form Console i.e. User
    """
    try:
        while(True):
            contact_obj = Add_conatcts_from_console()
            contacts_list.append(contact_obj)
            contacts_add_choice = input(
                "Enter \"Y\" for adding more & \"N\" to stop adding: ")
            if (contacts_add_choice.upper() == "N"):
                break
        return contacts_list
    except Exception as ex:
        print(ex)


def Editing_or_deleting_contacts(con_list):
    """
        Description: Editing Contact Details form Console i.e. by user choice
        Parameters: None
        Returns: Returns a list containing objects of Contact Class that is taken form Console i.e. User
    """
    edited_or_deleted_person_name = input(
        "Enter the name of person, whom details you want to edit or delete: ").upper()
    try:
        for item in con_list:
            if item.first_name.upper() == edited_or_deleted_person_name:
                choice = input(
                    "Enter choice, u want to edit or delete:\n 1 : FN,2 : LN,3 : Address,4 : City,5 : State,6 : ZIP,7 : Phone,8 : Email,9 : For deleting Contact alltogether")
                if (choice == "1"):
                    fn = input("Enter updated first name: ")
                    item.first_name = fn
                elif (choice == "2"):
                    ln = input("Enter updated last name: ")
                    item.last_name = ln
                elif (choice == "3"):
                    addrs = input("Enter updated address: ")
                    item.address = addrs
                elif (choice == "4"):
                    city = input("Enter updated city: ")
                    item.city = city
                elif (choice == "5"):
                    state = input("Enter updated state: ")
                    item.state = state
                elif (choice == "6"):
                    zip = input("Enter updated zip: ")
                    item.zip = zip
                elif (choice == "7"):
                    phn_no = input("Enter updated phn number: ")
                    item.phone_number = phn_no
                elif (choice == "8"):
                    email = input("Enter updated email: ")
                    item.email = email
                elif (choice == "9"):
                    con_list.remove(item)
                else:
                    print("Invalid Choice")
            else:
                print("The name entered by you does not exist in Contacts list")
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    contacts_list = []
    Storing_contacts_in_list()
    user_choice = input(
        "Do u want to edit or delete Contacts \"Y\" OR \"N\":").upper()
    if (user_choice.upper() == "Y"):
        Editing_or_deleting_contacts(contacts_list)
    for item in contacts_list:
        print(str(item))
