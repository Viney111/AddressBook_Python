"""
    @Author: Viney Khaneja
    @Date: 2022-04-14 13:05PM
    @Last Modified by: Viney Khaneja
    @Last Modified time: None
    @Title : Custom Exception Class
"""


class Custom_Exception_AddressBook(Exception):
    """
    Description: This class is to generating Custom Exception as per User Understanding
    """

    def __init__(self, msg):
        """
            Description: Constructor of Custom_Exception_AddressBook Class
            Parametres: Takes class fields & exception message
            Retuns: None, Just initialize the values of object
        """
        # To access the Base Exception Class
        super().__init__(msg)
