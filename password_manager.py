
import random
import string
import pyperclip

class User:
    """
    Class that generates new instances of users
    """
    # pass
    list_of_users = [] # Empty list of users

    def __init__(self,first_name,email,password):

        """ the init method helps in defining properties of our objects"""
        self.first_name = first_name
        self.email = email
        self.password = password

    def save_user(self):
        '''
        save_user method saves contact objects into list_of_users
        '''

        User.list_of_users.append(self)

    @classmethod
    def user_exists(cls,first_name):
        '''
        Method that checks if a user exists from the list_of_users
        '''
        for user in cls.list_of_users:
            if (user.first_name == first_name):
                return True
        return False
    @classmethod
    def user_exists_by_email(cls,email):
        for user in cls.list_of_users:
            if (user.email == email):
                return True
        return False

class Credential:
    """This is a class for creating new instances, methods and properties of credentials"""

    list_of_credentials = [] #Empty list of credentials
   
    def __init__(self,account_name,user_name,account_password):

        '''
        init method helps us define properties for our objects
        '''
        self.account_name = account_name
        self.user_name = user_name
        self.account_password = account_password
    def save_credentials(self):
        '''
        Method to save each new credential to the list of credetials
        '''
        Credential.list_of_credentials.append(self)

    def automate_password(chars=string.ascii_letters + string.digits):
        """
        Method returns a string of random characters. Length of password to be determined by user.
        
        Source: http://stackoverflow.com/a/2257449
        """

        length = int(input("Enter length of password: "))
        auto_password = ''.join(random.choice(chars) for i in range(length))
        return auto_password
    def delete_credentials(self):
        """Method deletes credentials from list of credentials"""

        Credential.list_of_credentials.remove(self)
    @classmethod
    def find_by_website(cls,account_name):
        """Method that returns saved credentials for a specific website"""
        for credential in cls.list_of_credentials:
            if credential.account_name == account_name:
                return credential
    @classmethod
    def credential_exists(cls,account_name):
        """Method that checks if credentials exist from the list of credentials 
        Returns :
            Boolean: True or false depending if the credentials exists
        """
        for credential in cls.list_of_credentials:
            if credential.account_name == account_name:
                return True
        return False
    @classmethod
    def display_all_credentials(cls):

        """Method displays all saved credentials for a given user"""
        return cls.list_of_credentials
    @classmethod
    def copy_password(cls,account_name):
        """Method that enables user to copy password for specific website"""
        credential_found = Credential.find_by_website(account_name)
        return pyperclip.copy(credential_found.account_password)
        print(pyperclip.copy(credential_found.account_password))
