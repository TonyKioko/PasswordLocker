#!/usr/bin/env python3.6
from password_manager import User
from password_manager import Credential
import datetime

def create_user(fname,email,password):
    '''
    This method allows the creation of new user accounts
    '''
    new_user = User(fname,email,password)
    return new_user

def save_user(user):
    '''
    Function that saves the created user to the list_of_users
    '''
    User.save_user(user)
def authenticate_user(fname):
    '''
    Function that authenticates if a user has a user account
    '''
    confirm_user = User.user_exists(fname)
    return confirm_user
def authenticate_by_email(email):
    confirm_user1 = User.user_exists_by_email(email)
    return confirm_user1

def make_password():
    '''
    Function that generates a random password for the user
    '''
    auto_password = Credential.automate_password()
    return auto_password

def create_credential(account_name,user_name,acc_password):
    '''
    This function allows the creation of new credential
    '''
    new_credential = Credential(account_name,user_name,acc_password)
    return new_credential

def save_credential(credential):
    '''
    Functions invokes the save_credentials method from class 
    Credential to add a new_credential to the list of credentials
    '''
    Credential.save_credentials(credential)
def find_credential(account_name):
    '''
    Function that returns credential for specific website
    '''

    return Credential.find_by_website(account_name)
def check_credential_exists(account_name):
    '''
    Function that checks if credential in the list_of_credentials
    '''
    return Credential.credential_exists(account_name)

def display_credential():
    return Credential.display_all_credentials()
    '''
    This function displays all credentials saved by the user
    '''

def delete_credential(credential):
    '''
    Function that deletes a credential from the list of credentials
    '''
    credential.delete_credentials()
def copy_password(account_name):
    '''
    This function allows user to copy password to clipboard
    '''
    return Credential.copy_password(account_name)


def main():
    print("Hello and Welcome to your Password Locker.")

    while True:
        print("\n")
        print("PLEASE USE THE SHORTCODES: cu - to CREATE USER ACCOUNT , lg - to LOGIN to your existing account, ex - to EXIT password Locker ")
        short_code = input().lower()
        print('\n')

        if short_code == 'cu':
            print("Create an Account to use the Password Locker App")
            first_name = input("Enter your first name: ").strip()
            email = input("Enter your email: ").strip()
            password = input("Enter your password: ").strip()
            confirm_password = input("Confrim password: ").strip()
            if password == confirm_password:
                save_user(create_user(first_name, email, password))
                print("")
                print(f"New Account, {first_name} with {email} using password: {password} created on {datetime.datetime.now()} ")
                print(f"{first_name}, you can now proceed to login and save your credentials")
            else:
                print("***Your passwords do not match. Please try again.***")


        elif short_code == "lg":
            print("*"*40)
            print("Enter details to access your account")
            user_name = input("Enter first name: ").strip()
            password = str(input("Enter password: "))
            user_exists = authenticate_user(user_name)
    
            if user_exists == True:
                print(" ")
                print(f"Logged in as {user_name}.")
                print(" ")
                while True:
                    print('Use the shortcodes: \n cc-Create new Credential ||  sc-Show Your Saved Credentials \n cp-Copy to Password   ||  lu-Logout')
                    print("*_"*40)
                    short_code = input("Select choice to proceed: ").lower()
                    if short_code == "lu":
                        print(" ")
                        print(f"You are now logged out... See you soon {user_name}")
                        break
                    elif short_code ==  "cc":
                        print(" ")
                        print("Create Credential: ")
                        website_name = input("Enter  website's name: ").strip()
                        login_name = input("Enter login name on website: ").strip()
                        while True:
                            print("")
                            print("Password Options: \n 1-enter own password | 2-Let us generate a password for you | q-quit")
                            pass_code = str(input("Enter an option: ")).lower().strip()
                            if pass_code == "1":
                                print(" ")
                                secret_password = input("Enter password: ")
                                break
                            elif pass_code == "2":
                                secret_password = make_password()
                                break
                            elif pass_code == "q":
                                break
                            else:
                                print("Please enter a valid choice")
                        save_credential(create_credential(website_name,login_name,secret_password))
                        print("")
                        print(f"*****   Credential Saved For: Website: {website_name}, login name: {login_name}, with Password: {secret_password}   *****")
                        print("")
                    elif short_code == "sc":
                        print(" ")
                        if display_credential():
                            print(" ")
                            print("Your saved Credentials are displayed below.")
                            for cred in display_credential():
                                print("")
                                print(f"Website:{cred.account_name}, login name: {cred.user_name}, with Password :{cred.account_password}")
                                print(" ")
                        else:
                            print(f"Your credential list is empty. Please add your Credentials")
                    elif short_code == "cp":
                        print(" ")
                        selected_website = input("Select website for password to be copied: ").strip()
                        copy_password(selected_website)

                    else:
                        print("Please selected a valid code to proceed")
                else:
                    print("Incorrect details. Please use the short codes to proceed.")
            else:
                print(" ")
                print("***Invalid Login details. Make sure you have a User Account***")
        elif short_code == "ex":
            print ("EXITING APPLICATION......")
            print ("\n")
            break


        else:
            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()
