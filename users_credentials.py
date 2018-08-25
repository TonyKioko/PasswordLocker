
import random
import string
import pyperclip

global user_list;

class User:
    # pass
    user_list = []
    def __init__(self,first_name,last_name,password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        
    def save_user(self):
        User.user_list.append(self)

    @classmethod
    def user_exists(cls,first_name):
        for user in cls.user_list:
            if user.first_name == first_name:
                return True
        return False

class Credential:

    credentials_list = []
    # @classmethod
    # def user_exists(cls,first_name):
    #     for user in cls.user_list:
    #         if user.first_name == first_name:
    #             return True
    #     return False
    # @classmethod
	# def authenticate_user(cls,first_name,password):
	# 	current_user = ''
	# 	for user in cls.user_list:
	# 		if (user.first_name == first_name and user.password == password):
	# 			current_user = user.first_name
	# 	return current_user
    def __init__(self,account_name,account_password):
        self.account_name = account_name
        self.account_password = account_password
    def save_credentials(self):
        Credential.credentials_list.append(self)

    def automate_password(length=6, chars=string.ascii_letters + string.digits):
        
        auto_password = ''.join(random.choice(chars) for i in range(length))
        return auto_password
    def delete_credentials(self):
        Credential.credentials_list.remove(self)
    @classmethod
    def find_by_website(cls,account_name):
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential
    @classmethod
    def credential_exists(cls,account_name):
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return True
        return False
    @classmethod
    def display_all_credentials(cls):
        return cls.credentials_list
    # @classmethod
    # def copy_password(cls,account_name):
    #     credential_found = Credential.find_by_website(account_name)
    #     return pyperclip.copy(credential_found.account_password)