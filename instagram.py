"""
4nn0y3r - A script to literally annoy people. 
This script contains all the code required to spam users on Instagram 
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

# Getting username for Instagram login
username = username_chooser_insta()

# Getting password for Instagram password
password = password_chooser_insta()

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

# Open Instagram
driver.set_page_load_timeout(15)
driver.get("https://instagram.com")
time.sleep(3)

# Entering Instagram username
driver.find_element_by_name("username").send_keys(username)
time.sleep(1)

# Entering Instagram password
driver.find_element_by_name("password").send_keys(password)
time.sleep(1)

# Logging in
driver.find_element_by_xpath("//*[@id=\"react-root\"]/section[1]/main[1]/article[1]/div[2]/div[1]/div[1]/form[1]/div[4]/button[1]").click()
time.sleep(3)

# Running a loop to cvisit each username and send message
for name in names:
    driver.get(f"https://instagram.com/{name}")
    time.sleep(3)
    # Opening message box
    driver.find_element_by_xpath("//*[@id=\"react-root\"]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[1]/div[1]/button[1]").click()
    time.sleep(3)
    # Running a loop to type message X times
    for i in range(count):
        # Running a loop to type message
        for msg in message:
            driver.find_element_by_xpath("//*[@id=\"react-root\"]/section[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/textarea[1]").send_keys(message)
            driver.find_element_by_xpath("//*[@id=\"react-root\"]/section[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/textarea[1]").send_keys(Keys.SHIFT, Keys.ENTER)
            # Sending the message
        driver.find_element_by_xpath("//*[@id=\"react-root\"]/section[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/textarea[1]").send_keys(Keys.ENTER)
        # Pretty formatting for Grammar Nazis!
    if (count > 1):
        print(f"\n{name} was sent {count} messages!\n")
    else:
        print(f"\n{name} was sent {count} message!\n")

# Pretty formatting for Grammar Nazis!
if(len(names) > 1):
    print(f"\n You've successfully 4nn0y3d {len(names)} people\n")
else:
    print(f"\n You've successfully 4nn0y3d {len(names)} person\n")
    driver.quit()

