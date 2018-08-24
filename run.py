#!/usr/bin/env python3.6
from users_credentials import User
from users_credentials import Credential

def create_user(self,fname,lname,password):
    new_user = User(fname,lname,password)
    return new_user

def save_user(user):
    user.save_user()

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
def check_credential_exists(account_name)
    return Credential.credential_exists(account_name)

def display_credential():
    return Credential.display_all_credentials()

def delete_credential(credential):
    credential.delete_credentials()


def main():
    print("Hello Welcome to your Password Locker.")
