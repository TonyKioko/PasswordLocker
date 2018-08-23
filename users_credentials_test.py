import unittest
from users_credentials import User
from users_credentials import Credential

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User('Tony','Kioko','abc123')
    def test_init(self):
        self.assertEqual(self.new_user.first_name,'Tony')
        self.assertEqual(self.new_user.last_name,'Kioko')
        self.assertEqual(self.new_user.password,'abc123')

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)



class TestCredential(unittest.TestCase):  

    def setUp(self):
        self.new_credential = Credential("Slack","xyz456")   
    def test_credentials(self):
        self.assertEqual(self.new_credential.account_name,"Slack")  
        self.assertEqual(self.new_credential.account_password,"xyz456")
    def test_save_credentials(self):
        self.new_credential.save_credentials() 
        self.assertEqual(len(Credential.credentials_list), 1) 
    def test_save_multiple_credentials(self):
        self.new_credential.save_credentials()
        test_credential = Credential("eCitizen","jkl789")
        test_credential.save_credentials()
        self.assertEqual(len(Credential.credentials_list), 2)
    def tearDown(self):
        Credential.credentials_list = []
    def test_delete_credentials(self):
        self.new_credential.save_credentials()
        test_credential = Credential("eCitizen","jkl789")
        test_credential.save_credentials()
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credential.credentials_list),1)
    def test_find_credential_by_website(self):
        self.new_credential.save_credentials()
        test_credential = Credential("eCitizen","jkl789")
        test_credential.save_credentials()
        found_credential = Credential.find_by_website("eCitizen")
        self.assertEqual(found_credential.account_name, "eCitizen")

    def test_credential_exists(self):
        self.new_credential.save_credentials()
        test_credential = Credential("eCitizen","jkl789")
        test_credential.save_credentials()
        credential_exists = Credential.credential_exists("eCitizen")
        self.assertTrue(credential_exists)

    def test_display_all_credentials(self):
        self.assertEqual(Credential.display_all_credentials(), Credential.credentials_list)

if __name__ == '__main__':
    unittest.main()