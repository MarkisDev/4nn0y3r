"""
4nn0y3r - A script to literally annoy people. 
This script contains all the code required to spam users on WhatsApp 
@author : MarkisDev
@copyright : https://markis.dev
"""  
# Importing Selenium for automation
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Importing time to let the user see what's happening
import time

# Importing all the functions required
from func import *

# Initializing variables
driver = ''
message = []

# Displaying the disclaimer
disclaimer()

# Getting browser input
browser = browser_choice()

# Getting browser version
directory = directory_choice(browser)

# Getting name
names = name_chooser()

# Getting count for spam
count = count_chooser()

# Getting the message
message = message_chooser()

# Load webdriver 
if browser == 1:
    driver = webdriver.Chrome(directory)
elif(browser == 2):
    driver = webdriver.Edge(directory)

# Open Web WhatsApp
driver.set_page_load_timeout(15)
driver.get("https://web.whatsapp.com")
time.sleep(3)

# Unchecking 'Keep me signed in'
driver.find_element_by_name("rememberMe").click()
time.sleep(2)

# Checking if user has authenticated successfully 
if has_authenticated_whatsapp(driver):
    # Running a loop to send messages to every person
    for name in names:
        # Searching for account
        driver.find_element_by_xpath("//*[@id=\"side\"]/div[1]/div[1]/label[1]/div[1]/div[2]").send_keys(name)
        time.sleep(2)
        # Selecting account
        driver.find_element_by_xpath("//*[@id=\"side\"]/div[1]/div[1]/label[1]/div[1]/div[2]").send_keys(Keys.ENTER)
        time.sleep(2)
        # Running a loop to send message
        for i in range(count):
            # Running a loop to type the message's different lines
            for j in range(len(message)):
                driver.find_element_by_xpath("//*[@id=\"main\"]/footer[1]/div[1]/div[2]/div[1]/div[2]").send_keys(Keys.SHIFT, Keys.ENTER)
                driver.find_element_by_xpath("//*[@id=\"main\"]/footer[1]/div[1]/div[2]/div[1]/div[2]").send_keys(message[j])
            driver.find_element_by_xpath("//*[@id=\"main\"]/footer[1]/div[1]/div[2]/div[1]/div[2]").send_keys(Keys.ENTER)
            time.sleep(2)
        # Pretty formatting for Grammar Nazis!
        if (count > 1):
            print(f"\n{name} was sent {count} messages!\n")
        else:
            print(f"\n{name} was sent {count} message!\n")
        time.sleep(2)
    # Pretty formatting for Grammar Nazis!
    if(len(names) > 1):
        print(f"\n You've successfully 4nn0y3d {len(names)} people\n")
    else:
        print(f"\n You've successfully 4nn0y3d {len(names)} person\n")
    driver.quit()




