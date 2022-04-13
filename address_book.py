"""
    @Author: Viney Khaneja
    @Date: 2022-04-13 20:05PM
    @Last Modified by: Viney Khaneja
    @Last Modified time: None
    @Title : Address_Book_Problem_Statement
"""


class Contacts():

    def __init__(self, first_name, last_name, address, city, state, zip, phone_number, email):
        """
            Description: Constructor of Contacts Class
            Parametres: Takes class fields
            Retuns: None, Just initialize the values of object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        """
            Description: To return textual content of the Contacts class Object
            Parameters: Takes Instance (Object) of class as arguments
            Returns: Returns String Representation of object, understandable by User
        """
        return f"Full Name is {self.first_name} {self.last_name}\nFull address is {self.address},{self.city},{self.state},{self.zip}\nPhone Number & email is {self.phone_number} and {self.email} respectively"


def Add_conatcts_from_console():
    """
        Description: Adding Contact Details form Console & returning that details as an object of Contacts Class
        Parameters: None
        Returns: Returns Conatacts class object having all info
    """
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


def Storing_contacts_in_list():
    """
        Description: Adding Contact Details form Console in list
        Parameters: None
        Returns: Returns a list containing objects of Contact Class that is taken form Console i.e. User
    """
    while(True):
        contact_obj = Add_conatcts_from_console()
        contacts_list.append(contact_obj)
        contacts_add_choice = input(
            "Enter \"Y\" for adding more & \"N\" to stop adding: ")
        if (contacts_add_choice.upper() == "N"):
            break
    return contacts_list


if __name__ == "__main__":
    contacts_list = []
    Storing_contacts_in_list()
    for item in contacts_list:
        print(str(item))
