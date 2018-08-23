import unittest
from users_credentials import User

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
        

if __name__ == '__main__':
    unittest.main()