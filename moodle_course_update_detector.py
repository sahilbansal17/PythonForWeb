# moodle course update checker : automatically checks for updates in courses registered on moodle

from selenium import webdriver
import getpass

# credentials for login
username = " " #update it with your username
password = getpass.getpass("Password:")

# start a browser session
browser = webdriver.Chrome("/users/sahilbansal/Downloads/chromedriver") # change the parameter with the path of chromedriver

# open link in browser
browser.get('http://moodlej.iitjammu.ac.in/login/index.php')

# login
nameElem = browser.find_element_by_id('username')
nameElem.send_keys(username)

passElem = browser.find_element_by_id('password')
passElem.send_keys(password)

browser.find_element_by_id('loginbtn').click()
