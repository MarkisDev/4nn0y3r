"""
Main functions for 4nn0y3r
This script contains all the functions required for 4nn0y3r.
@author : MarkisDev
@copyright : https://markis.dev
"""  
import os

# Function to display disclaimer [because I don't want to be sued]
def disclaimer():
    print("""
██╗  ██╗███╗   ██╗███╗   ██╗ ██████╗ ██╗   ██╗██████╗ ██████╗ 
██║  ██║████╗  ██║████╗  ██║██╔═████╗╚██╗ ██╔╝╚════██╗██╔══██╗
███████║██╔██╗ ██║██╔██╗ ██║██║██╔██║ ╚████╔╝  █████╔╝██████╔╝
╚════██║██║╚██╗██║██║╚██╗██║████╔╝██║  ╚██╔╝   ╚═══██╗██╔══██╗
     ██║██║ ╚████║██║ ╚████║╚██████╔╝   ██║   ██████╔╝██║  ██║
     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚═════╝ ╚═╝  ╚═╝
                                            
                                                      __          __   __   ___      
                                    __     |\/|  /\  |__) |__/ | /__` |  \ |__  \  / 
                                           |  | /~~\ |  \ |  \ | .__/ |__/ |___  \/  
            """)
    print("USE THIS AT YOUR OWN RISK.")
    print("NEITHER AM I NOR ANYONE RELATED TO THIS PROJECT RESPONSIBLE FOR WHAT YOU DO.")
    print("ONLY YOU ARE RESPONSIBLE FOR ANYTHING THIS SCRIPT DOES.")


# Function to display and take input for browser
def browser_choice():
    print("\n[1] Chrome")
    print("[2] Edge")
    choice = input("\nEnter your browser type: ")
    if(choice.isdigit()):
        if (int(choice) == 0 or (int(choice) > 2)):
            print("\nInvalid choice! Try again.")
            browser_choice()
        return int(choice)
    else:
        print("\nInvalid choice! Try again.")
        browser_choice()

# Function to display, take input for browser version and return webdriver path
def directory_choice(browser):
    if (browser == 1):
        print("\n[1] 80")
        print("[2] 81")
        print("[3] 83")
        print("[4] 84")
        choice = input("\nEnter the version of Chrome you are on: ")
        if(choice.isdigit()):
            choice = int(choice)
            if (choice == 0 or choice > 4):
                print("\nInvalid choice! Try again.")
                directory_choice(browser)
            directory = os.getcwd()
            if(choice == 1):
                directory = directory + "\drivers\chrome\win\80\chromedriver.exe"
            elif(choice == 2):
                directory = directory + "\drivers\chrome\win\81\chromedriver.exe"
            elif(choice == 3):
                directory = directory + "\drivers\chrome\win\83\chromedriver.exe"
            elif(choice == 4):
                directory = directory + "\drivers\chrome\win\84\chromedriver.exe"
            return directory
        else:
            print("\nInvalid choice! Try again.")
            directory_choice(browser)
    elif(browser == 2):
        print("\n[1] 83")
        print("[2] 84")
        print("[3] 85")
        choice = input("\nEnter the version of Edge you are on: ")
        if(choice.isdigit()):
            choice = int(choice)
            if (choice == 0 or choice > 3):
                print("\nInvalid choice! Try again.")
                directory_choice(browser)
            directory = os.getcwd()
            if(choice == 1):
                directory = directory + "\drivers\edge\win\83\msedgedriver.exe"
            elif(choice == 2):
                directory = directory + "\drivers\edge\win\84\msedgedriver.exe"
            elif(choice == 3):
                directory = directory + "\drivers\edge\win\85\msedgedriver.exe"
            return directory
        else:
            print("\nInvalid choice! Try again.")
            directory_choice(browser)

# Function to get names to spam
def name_chooser():
    print("\nEnter the usernames of the people you want to spam: ")
    print("\nType END when you are done.\n")
    names=[]
    while True:
        name = str(input())
        if(name.lower() == "end"):
            break
        names.append(name)
    return names

# Function to get number of times to spam
def count_chooser():
    choice = input("\nEnter the number of times you want to spam: ")
    if (choice.isdigit()):
        return int(choice)
    else:
        print("\nInvalid value! Try again.")

# Function to get the message from the user
def message_chooser():
    print("\nEnter your message, press enter for multiple lines.")
    print("\nType END when you are done.\n")
    lines = []
    while True:
        line = str(input())
        if (line.lower() == "end"):
            break
        lines.append(line)
    return lines

# Recursive function to make sure user has authenticated themselves
def has_authenticated_whatsapp(driver):
    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException
    import time
    try:
        driver.find_element_by_xpath("//*[@id=\"side\"]/div[1]/div[1]/label[1]/div[1]/div[2]")
    except NoSuchElementException:
        time.sleep(5)
        has_authenticated(driver)
    return True

# Function to get Instagram login
def username_chooser_insta():
    username = input("\n Please enter your Instagram username: ")
    return username

# Function to get Instagram password
def password_chooser_insta():
    from getpass import getpass
    password = getpass("\n Please enter your Instagram password: ")
    return password