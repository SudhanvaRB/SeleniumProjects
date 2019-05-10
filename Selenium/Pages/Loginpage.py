'''
Created on Oct 12, 2018

@author: subharad
'''
from Locators.locators import Locators
class loginpage():
    
    def __init__(self,driver):
        self.driver = driver
        
    #===========================================================================
    # def enter_username(self, username):
    #     self.driver.find_element_by_id(self.username_text_box).clear()
    #     self.driver.find_element_by_id(Locators.username_text_box).send_keys(username)
    #     
    # def click_login(self):
    #     self.driver.find_element_by_id(Locators.login_button).click()
    #===========================================================================
        
    def login(self):
        self.driver.get("http://10.100.245.80:92/VMS/login")
        self.driver.find_element_by_id(Locators.username_text_box).send_keys("tihollan")
        self.driver.find_element_by_id(Locators.login_button).click()