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


if __name__ == "__main__":
    viney = Contacts("Viney", "Khaneja", "657/8,VPO Kalanaur", "Rohtak",
                     "Haryana", 124113, 7206594149, "vineykhaneja999@gmail.com")
    try:
        print(str(viney))
    except Exception as ex:
        print(ex)
