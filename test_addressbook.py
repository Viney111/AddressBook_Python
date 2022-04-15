"""
    @Author: Viney Khaneja
    @Date: 2022-04-14 15:41PM
    @Last Modified by: Viney Khaneja
    @Last Modified time: None
    @Title : Unit Test Class
"""


import io
import sys
from ast import Assert
# Importing Unit Test Module
import unittest
from contacts import Contacts
from unittest.mock import patch
from io import StringIO

# Importing Address Book
import address_book

# Importing Regex Class
from Validation_Regex import Regex_Validation


class Test_AddressBook(unittest.TestCase):
    """
    Description: This class is to test all the methods used in addressBook
    """

    def test_first_name_when_entered_correct_should_return_true(self):
        """
            Description: Unit Test to verify first Name positively
            Parametres: Takes correct first name
            Returns: Just Checks the value inputed is giving desired results or not
        """
        self.assertTrue(Regex_Validation.validate_first_name("Viney"))
        self.assertTrue(Regex_Validation.validate_first_name("Vishal"))

    def test_first_name_when_entered_incorrect_should_return_false(self):
        """
            Description: Unit Test to verify first Name negatively
            Parametres: Takes Incorrect first name
            Returns: Just Checks the value inputed is giving desired results or not
        """
        self.assertFalse(Regex_Validation.validate_first_name("viney"))
        self.assertFalse(Regex_Validation.validate_first_name("Vi"))

    def test_last_name_when_entered_correct_should_return_true(self):
        """
            Description: Unit Test to verify last Name positively
            Parametres: Takes correct last name
            Returns: Just Checks the value inputed is giving desired results or not
        """
        self.assertTrue(Regex_Validation.validate_last_name("Khaneja"))
        self.assertTrue(Regex_Validation.validate_last_name("Juneja"))

    def test_last_name_when_entered_incorrect_should_return_false(self):
        """
            Description: Unit Test to verify last Name negatively
            Parametres: Takes Incorrect last name
            Returns: Just Checks the value inputed is giving desired results or not
        """
        self.assertFalse(Regex_Validation.validate_last_name("Kj"))
        self.assertFalse(Regex_Validation.validate_last_name("juneja"))

    def test_address_when_entered_correct_should_return_true(self):
        """
            Description: Unit Test to verify address positively
            Parametres: Takes correct address
            Returns: Just Checks the value inputed is giving desired results or not
        """
        self.assertTrue(Regex_Validation.validate_address("metoo"))
        self.assertTrue(Regex_Validation.validate_address("kalanaur"))

    def test_address_when_entered_incorrect_should_return_false(self):
        """
            Description: Unit Test to verify address negatively
            Parametres: Takes Incorrect address
            Returns: Just Checks the value inputed is giving desired results or not
        """
        self.assertFalse(Regex_Validation.validate_address("vine"))
        self.assertFalse(Regex_Validation.validate_address("Vi"))

    def test_cityname_when_entered_correct_should_return_true(self):
        """
            Description: Unit Test to verify city name positively
            Parametres: Takes correct city name
            Returns: Just Checks the value inputed is giving desired results or not
        """
        self.assertTrue(Regex_Validation.validate_city_name("Rohtak"))
        self.assertTrue(Regex_Validation.validate_city_name("Mumbai"))

    def test_cityname_when_entered_incorrect_should_return_false(self):
        """
            Description: Unit Test to verify city name negatively
            Parametres: Takes Incorrect city name
            Returns: Just Checks the value inputed is giving desired results or not
        """
        self.assertFalse(Regex_Validation.validate_city_name("panji"))
        self.assertFalse(Regex_Validation.validate_city_name("ochi"))

    def test_statename_when_entered_correct_should_return_true(self):
        """
            Description: Unit Test to verify state name positively
            Parametres: Takes correct state name
            Returns: Just Checks the value inputed is giving desired results or not
        """
        self.assertTrue(Regex_Validation.validate_state_name("Haryana"))
        self.assertTrue(Regex_Validation.validate_state_name("Karnataka"))

    def test_statename_when_entered_incorrect_should_return_false(self):
        """
            Description: Unit Test to verify state name negatively
            Parametres: Takes Incorrect state name
            Returns: Just Checks the value inputed is giving desired results or not
        """
        self.assertFalse(Regex_Validation.validate_state_name("goa"))
        self.assertFalse(Regex_Validation.validate_state_name("assam"))

    def test_zip_when_entered_correct_should_return_true(self):
        """
            Description: Unit Test to verify zip positively
            Parametres: Takes correct zip code
            Returns: Just Checks the value inputed is giving desired results or not
        """
        self.assertTrue(Regex_Validation.validate_zip("124113"))
        self.assertTrue(Regex_Validation.validate_zip("124001"))

    def test_zip_when_entered_incorrect_should_return_false(self):
        """
            Description: Unit Test to verify zip negatively
            Parametres: Takes Incorrect zip code
            Returns: Just Checks the value inputed is giving desired results or not
        """
        self.assertFalse(Regex_Validation.validate_zip("1256"))
        self.assertFalse(Regex_Validation.validate_zip("14 566"))

    def test_phoneNo_when_entered_correct_should_return_true(self):
        """
            Description: Unit Test to verify phone number positively
            Parametres: Takes correct phone number
            Returns: Just Checks the value inputed is giving desired results or not
        """
        self.assertTrue(
            Regex_Validation.validate_phone_number("91 7206594149"))
        self.assertTrue(
            Regex_Validation.validate_phone_number("91 9991661664"))

    def test_phoneNo_when_entered_incorrect_should_return_false(self):
        """
            Description: Unit Test to verify phone number negatively
            Parametres: Takes Incorrect phone number
            Returns: Just Checks the value inputed is giving desired results or not
        """
        self.assertFalse(Regex_Validation.validate_phone_number("7206594149"))
        self.assertFalse(
            Regex_Validation.validate_phone_number("91 5466664666"))

    def test_email_when_entered_correct_should_return_true(self):
        """
            Description: Unit Test to verify email positively
            Parametres: Takes correct email
            Returns: Just Checks the value inputed is giving desired results or not
        """
        self.assertTrue(
            Regex_Validation.validate_email("vineykahneja999@gmail.com"))
        self.assertTrue(
            Regex_Validation.validate_email("vishal1juuneha@bridgelabz.com"))

    def test_email_when_entered_incorrect_should_return_false(self):
        """
            Description: Unit Test to verify email negatively
            Parametres: Takes Incorrect email
            Returns: Just Checks the value inputed is giving desired results or not
        """
        self.assertFalse(Regex_Validation.validate_email(
            "vineykahneja999gmail.com"))
        self.assertFalse(
            Regex_Validation.validate_email("vishal1juuneha@bridgelabzcom"))

    # def test_add_correct_contacts_details_from_console_returns_an_object_user_inputed(self):
    #     """
    #         Description: Unit Test to verify if contact added from console is stored as object
    #         Parametres: Takes Input from user
    #         Returns: The object having details entered by user from Console
    #     """
    #     contact_obj = address_book.add_contacts_from_console()
    #     self.assertEqual(contact_obj.first_name, "Viney")

    def test_add_incorrect_contacts_details_from_console_returns_error_msg(self):
        """
            Description: Unit Test to verify if contact added from console is stored as object
            Parametres: Takes Input from user
            Returns: The object having details entered by user from Console
        """
        contact_obj = Contacts("Viney", "Khaneja", "", "", "",
                               "124113", "91 7206594194", "vineykahneja999@gmail.com")
        contacts_list = []
        contacts_list.append(contact_obj)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            address_book.storing_contacts_in_list(contacts_list)
            self.assertEqual(fake_out.getvalue(
            ), "The entered Full name i.e. first name and last name already exists in particular address Book")
        # captured_output = io.StringIO()
        # sys.stdout = captured_output
        # address_book.add_contacts_from_console()
        # sys.stdout = sys.__stdout__
        # print("Captured", captured_output.value())


if __name__ == "__main___":
    unittest.main()
