"""
    @Author: Viney Khaneja
    @Date: 2022-04-14 11:05AM
    @Last Modified by: Viney Khaneja
    @Last Modified time: None
    @Title : Validation Pattern class
"""

# Importing Regex Module
import re

# Importing Custom Exception AddressBook Class
from Custom_Exception import Custom_Exception_AddressBook


class Regex_Validation:
    """
        Description: This Class having Functions to validate the user details
    """
    def validate_first_name(first_name):
        """
        Description: This function is to validate first name.
        Condition: Name should start with Capital letter and should have min 3 letters.
        Args: first_name: First name to validate
        Returns: boolean result
        """
        try:
            if(bool(re.match(r"^[A-Z]{1}[a-z]{2,}$", first_name)) == True):
                return True
            else:
                raise Custom_Exception_AddressBook(
                    "First name should start with capital letter & should have at least 3 characters")
        except Exception as ex:
            print(ex)
            return False

    def validate_last_name(last_name):
        """
        Description: This function is to validate last name.
        Condition: Name should start with Capital letter and should have min 3 letters.
        Args: last_name: Last name to validate
        Returns: boolean result
        """
        try:
            if(bool(re.match(r"^[A-Z]{1}[a-z]{2,}$", last_name)) == True):
                return True
            else:
                raise Custom_Exception_AddressBook(
                    "Last name should start with capital letter & should have at least 3 characters")
        except Exception as ex:
            print(ex)
            return False

    def validate_zip(zip):
        """
        Description: This function is to validate zip code.
        Condition: Zip should contain exact 6 numerical values & should not start with zero
        Args: zip: To be validated
        Returns: boolean result
        """
        try:
            if (bool(re.match(r"^[1-9]{1}[0-9]{5}$", zip)) == True):
                return True
            else:
                raise Custom_Exception_AddressBook(
                    "Zip should have exactly 6 numbers & should not start with zero")
        except Exception as ex:
            print(ex)
            return False

    def validate_phone_number(phone_number):
        """
        Description: This function is to validate phone number.
        Condition: Phone number should start with 91 and should have space afer that, followed by 10 numerical values
        Args: phone_number: To be validated
        Returns: boolean result
        """
        try:
            if (bool(re.match(r"^[0-9]{2}[ ][6-9]{1}[0-9]{9}$", phone_number)) == True):
                return True
            else:
                raise Custom_Exception_AddressBook(
                    "Phone Number should start with 91 (i.e. Country Code) and foloowed by exact 10 numbers")
        except Exception as ex:
            print(ex)
            return False

    def validate_email(email):
        """
        Description: This function is to validate email.
        Condition: Email should contain @ and . and other conditions
        Args: email: To be validated
        Returns: boolean result
        """
        try:
            if(bool(re.match(r"^[0-9a-z]+[+_.-]?[0-9a-z]+[@][0-9a-z]+[.][a-z]{2,}[.]?[a-z]+$", email)) == True):
                return True
            else:
                raise Custom_Exception_AddressBook(
                    "Email should not start with capital letters & should have @ and .")
        except Exception as ex:
            print(ex)
            return False


if __name__ == "__main__":
    Regex_Validation.validate_first_name("Viney")
    Regex_Validation.validate_first_name("viney")
    Regex_Validation.validate_last_name("Khaneja")
    Regex_Validation.validate_last_name("khaneja")
    Regex_Validation.validate_zip("124113")
    Regex_Validation.validate_zip("024113")
    Regex_Validation.validate_phone_number("91 7206594149")
    Regex_Validation.validate_phone_number("7206594149")
    Regex_Validation.validate_email("vineykhaneja999@gmail.com")
    Regex_Validation.validate_email("vineykhaneja999gmail.com")
