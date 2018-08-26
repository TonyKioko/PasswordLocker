import unittest # Importing the unittest module
import pyperclip
from password_manager import User  # Importing the User class
from password_manager import Credential  # Importing the Credential class

class TestUser(unittest.TestCase):

    
    def setUp(self):
        '''
        Setup method to run before each test cases.
        '''
        self.new_user = User('Tony','tony@abc.com','abc123') ## create user object
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,'Tony')
        self.assertEqual(self.new_user.email,'tony@abc.com')
        self.assertEqual(self.new_user.password,'abc123')

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the list of users
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.list_of_users),1)
    def test_user_exists(self):
        '''
        test_user_exists test case to test if the user exists in the
        list of users.
        '''
        self.new_user = User("Tony","tony@abc.com","abc123")
        self.new_user.save_user()
        user_exists =  User.user_exists("Tony")
        self.assertTrue(user_exists)



class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Setup method to run before each test cases.
        '''
        self.new_credential = Credential("Slack","Tonykm","xyz456")
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.account_name,"Slack")
        self.assertEqual(self.new_credential.user_name,"Tonykm")
        self.assertEqual(self.new_credential.account_password,"xyz456")
    def test_save_credentials(self):
        '''
        test_save_credential test case to test if the credential object is saved into
        the list of credentials
        '''
        self.new_credential.save_credentials()
        self.assertEqual(len(Credential.list_of_credentials), 1)
    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credential
        objects to our list_of_credentials
        '''
        self.new_credential.save_credentials()
        test_credential = Credential("Slack","Tonykm","xyz456")
        test_credential.save_credentials()
        self.assertEqual(len(Credential.list_of_credentials), 2)
    def tearDown(self):
        '''
        tearDown method that cleans up the list_of_credentials after each test case has run.
        '''
        Credential.list_of_credentials = []
    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove a credential from our list_of_credentials
        '''
        self.new_credential.save_credentials()
        test_credential = Credential("Slack","Tonykm","xyz456")
        test_credential.save_credentials()
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credential.list_of_credentials),1)
    def test_find_credential_by_website(self):
        self.new_credential.save_credentials()
        test_credential = Credential("Slack","Tonykm","xyz456")
        test_credential.save_credentials()
        found_credential = Credential.find_by_website("Slack")
        self.assertEqual(found_credential.account_name, "Slack")
    def test_credential_exists(self):
        self.new_credential.save_credentials()
        test_credential = Credential("Slack","Tonykm","xyz456")
        test_credential.save_credentials()
        credential_exists = Credential.credential_exists("Slack")
        self.assertTrue(credential_exists)

    def test_copy_password(self):
        self.new_credential.save_credentials()
        test_credential = Credential("Slack","Tonykm","xyz456")
        test_credential.save_credentials()
        Credential.copy_password("Slack")
        self.assertEqual(self.new_credential.account_password,pyperclip.paste())




if __name__ == '__main__':
    unittest.main()
