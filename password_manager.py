
import random
import string
import pyperclip

class User:
    # pass
    list_of_users = []
    def __init__(self,first_name,email,password):
        self.first_name = first_name
        self.email = email
        self.password = password

    def save_user(self):
        User.list_of_users.append(self)

    @classmethod
    def user_exists(cls,first_name):
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

    list_of_credentials = []
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
    def __init__(self,account_name,user_name,account_password):
        self.account_name = account_name
        self.user_name = user_name
        self.account_password = account_password
    def save_credentials(self):
        Credential.list_of_credentials.append(self)

    def automate_password(chars=string.ascii_letters + string.digits):

        length = int(input("Enter length of password: "))
        auto_password = ''.join(random.choice(chars) for i in range(length))
        return auto_password
    def delete_credentials(self):
        Credential.list_of_credentials.remove(self)
    @classmethod
    def find_by_website(cls,account_name):
        for credential in cls.list_of_credentials:
            if credential.account_name == account_name:
                return credential
    @classmethod
    def credential_exists(cls,account_name):
        for credential in cls.list_of_credentials:
            if credential.account_name == account_name:
                return True
        return False
    @classmethod
    def display_all_credentials(cls):
        return cls.list_of_credentials
    @classmethod
    def copy_password(cls,account_name):
        credential_found = Credential.find_by_website(account_name)
        return pyperclip.copy(credential_found.account_password)
        print(pyperclip.copy(credential_found.account_password))
