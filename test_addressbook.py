"""
    @Author: Viney Khaneja
    @Date: 2022-04-14 15:41PM
    @Last Modified by: Viney Khaneja
    @Last Modified time: None
    @Title : Unit Test Class
"""


# Importing Required Unit Test Modules
import unittest
from contacts import Contacts
import multiple_addressbook
import address_book
from Validation_Regex import Regex_Validation


class master:
    contact1 = Contacts("Viney", "Khaneja", "kalanaur", "Rohtak",
                        "Punjab", "124113", "91 7206594149", "vineykhaneja999gmail.com")
    contact2 = Contacts("Aman", "Gupta", "jagdishcolony", "Rohtak",
                        "Haryana", "124001", "91 9991661664", "amangpta123gmail.com")
    contact3 = Contacts("Sidharth", "Madaan", "busstand", "Sonepat",
                        "Punjab", "122001", "91 9466365917", "sidhumoosa129gmail.com")
    contact4 = Contacts("Papplu", "Sharma", "parichowk", "Jind",
                        "Haryana", "156301", "91 9215214254", "sharmagpta123gmail.com")
    addressbookdict = {"Evehi": [contact1, contact2], "Jigri":
                       [contact3, contact4]}


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

    def test_contacts_sorted_by_name(self):
        """
            Description: Unit Test to verify, contacts sorted by first name or not
            Parametres: Takes master dictionary
            Returns: Just Checks the value inputed is giving desired results or not
        """
        resulted_sorted_list = multiple_addressbook.sorting_entries_by_name(
            master.addressbookdict)
        expected_sorted_list = [master.contact2, master.contact4,
                                master.contact3, master.contact1]
        self.assertEqual(resulted_sorted_list, expected_sorted_list)

    def test_dictionary_of_city_and_person(self):
        """
            Description: Unit Test to verify, dictionary being made with city as key & contact details as values
            Parametres: Takes master dictionary
            Returns: Just Checks the value inputed is giving desired results or not
        """
        resulted_dict_city_and_person = multiple_addressbook.dictionary_of_city_and_person(
            master.addressbookdict)
        expected_dict_city_and_person = {"Rohtak": [master.contact1, master.contact2], "Jind": [
            master.contact4], "Sonepat": [master.contact3]}
        self.assertEqual(resulted_dict_city_and_person,
                         expected_dict_city_and_person)

    def test_dictionary_of_state_and_person(self):
        """
            Description: Unit Test to verify, dictionary being made with state name as key & contact details as values
            Parametres: Takes master dictionary
            Returns: Just Checks the value inputed is giving desired results or not
        """
        resulted_dict_state_and_person = multiple_addressbook.dictionary_of_state_and_person(
            master.addressbookdict)
        expected_dict_state_and_person = {"Punjab": [master.contact1, master.contact3], "Haryana": [
            master.contact2, master.contact4]}
        self.assertEqual(resulted_dict_state_and_person,
                         expected_dict_state_and_person)

    def test_count_by_state_and_city(self):
        """
            Description: Unit Test to verify, counting of persons by city & states 
            Parametres: Takes master dictionary
            Returns: Just Checks the value inputed is giving desired results or not
        """
        dict_state_and_person = multiple_addressbook.dictionary_of_state_and_person(
            master.addressbookdict)
        dict_city_and_person = multiple_addressbook.dictionary_of_city_and_person(
            master.addressbookdict)
        for key in dict_state_and_person:
            resulted_counts_by_state = len((dict_state_and_person[key]))
        self.assertEqual(resulted_counts_by_state, 2)
        count_by_city_list = []
        for key in dict_city_and_person:
            resulted_count_by_city = len(dict_city_and_person[key])
            count_by_city_list.append(resulted_count_by_city)
        self.assertEqual(count_by_city_list, [2, 1, 1])


if __name__ == "__main___":
    unittest.main()
