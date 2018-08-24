#!/usr/bin/env python3.6
from users_credentials import User
from users_credentials import Credential

def create_user(fname,lname,password):
    new_user = User(fname,lname,password)
    return new_user

def save_user(user):
    User.save_user(user)
def authenticate_user(fname):
    confirm_user = User.user_exists(fname)
    return confirm_user

def make_password(self):
    password = Credential.automate_password()
    return password

def create_credential(account_name,password):
    new_credential = Credential(account_name,password)
    return new_credential

def save_credential(credential):
    credential.save_credentials()
def find_credential(account_name):
    return Credential.find_by_website(account_name)
def check_credential_exists(account_name):
    return Credential.credential_exists(account_name)

def display_credential():
    return Credential.display_all_credentials()

def delete_credential(credential):
    credential.delete_credentials()


def main():
    print("Hello Welcome to your Password Locker.")

    while True:
        print("\n")
        print("Use these short codes to select an option: ca - to create account , li - to log in, ex - to exit password Locker ")
        short_code = input().lower()
        print('\n')

        if short_code == 'ca':
            print("Create an Account")
            first_name = input('Enter your first name - ').strip()
            last_name = input('Enter your last name - ').strip()
            password = input('Enter your password - ').strip()
            save_user(create_user(first_name, last_name, password))
            print(f'New Account Created for: {first_name} {last_name} using password: {password}')

        elif short_code == "li":
            print("*"*40)
            print("Enter details to access your account")
            user_name = input("Enter first name: ").strip()
            password = str(input("Enter password: "))
            user_exists = authenticate_user(user_name)

    else:
          print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()