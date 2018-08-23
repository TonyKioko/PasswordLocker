
class User:
    # pass
    user_list = []
    def __init__(self,first_name,last_name,password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        
    def save_user(self):
        User.user_list.append(self)

class Credential:

    credentials_list = []
    def __init__(self,account_name,account_password):
        self.account_name = account_name
        self.account_password = account_password
    def save_credentials(self):
        self.credentials_list.append(self)
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
