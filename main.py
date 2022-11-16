import selenium
from selenium import webdriver
from time import sleep


class fortilog:

   def __init__(self, username, password):
       self.driver = webdriver.Chrome()
       self.driver.get('http://172.16.10.20:1000/login?'
                       )
       self.driver.find_element_by_xpath('//input[@name="username"]'
               ).send_keys(username)
       self.driver.find_element_by_xpath('//input[@name="password"]'
               ).send_keys(password)
       self.driver.find_element_by_xpath('//button[@type="submit"]'
               ).click()
       sleep(3)


fortinetBot(<username>, <password>)
