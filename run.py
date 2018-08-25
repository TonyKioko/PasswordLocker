#!/usr/bin/env python3.6
from users_credentials import User
from users_credentials import Credential
import datetime

def create_user(fname,lname,password):
    new_user = User(fname,lname,password)
    return new_user

def save_user(user):
    User.save_user(user)
def authenticate_user(fname):
    confirm_user = User.user_exists(fname)
    return confirm_user

def make_password():
    auto_password = Credential.automate_password()
    return auto_password

def create_credential(account_name,user_name,acc_password):
    new_credential = Credential(account_name,user_name,acc_password)
    return new_credential

def save_credential(credential):
    Credential.save_credentials(credential)
def find_credential(account_name):
    return Credential.find_by_website(account_name)
def check_credential_exists(account_name):
    return Credential.credential_exists(account_name)

def display_credential():
    return Credential.display_all_credentials()
def copy_password(account_name):
    return Credential.copy_password(account_name)

def delete_credential(credential):
    credential.delete_credentials()



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
            last_name = input("Enter your last name: ").strip()
            password = input("Enter your password: ").strip()
            confirm_password = input("Confrim password: ").strip()
            if password == confirm_password:
                save_user(create_user(first_name, last_name, password))
                print(f"New Account, {first_name} {last_name} using password: {password} created on {datetime.datetime.now()} ")
                print(f'{first_name}, you can proceed to login and save your credentials')
            else:
                print("***Your passwords do not match. Please try again.***")


        elif short_code == "lg":
            print("*"*40)
            print("Enter details to access your account")
            user_name = input("Enter first name: ").strip()
            password = str(input("Enter password: "))
            user_exists = authenticate_user(user_name)

            if user_exists:
                print(" ")
                print(f"Logged in as {user_name}.")
                print(" ")
                while True:
                    print('Use the shortcodes: \n cc-Create new Credential ||  sc-Show Your Saved Credentials \n cp-Copy to Password   ||  q-Quit')
                    print("*_"*40)
                    short_code = input("Select choice to proceed: ").lower()
                    if short_code == "q":
                        print(" ")
                        print(f"Exiting application... See you soon {user_name}")
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
                        print(f"*****Credential Saved For: Website: {website_name}, login name: {login_name}, with Password: {secret_password}*****")
                        print("")
                    elif short_code == "sc":
                        print(" ")
                        if display_credential():
                            print(" ")
                            print("Your saved Credentials are displayed below.")
                            for cred in display_credential():
                                print(f"Website:{cred.account_name}, login name: {cred.user_name}, with Password :{cred.account_password}")
                                print(" ")
                        else:
                            print(f"Your credential list is empty. Please add your Credentials")
                    elif short_code == "cp":
                        print(" ")
                        selected_website = print("Select website for password to be copied: ")
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
