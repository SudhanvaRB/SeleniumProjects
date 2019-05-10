'''
Created on Apr 29, 2019

@author: subharad

*** Stationery Application Login Page Class, it has 1 Class and  2 methods
'''
import time
from Stationery.locators_stat import LocatorsStat as L
class Login():
    
    def __init__(self,driver):
        self.driver = driver
        
    
    def login_func(self,userid,passwrd):
        driver = self.driver
        driver.get(L.url)
        driver.maximize_window() # to maximize the chrome window
        driver.find_element_by_id(L.loginid).send_keys(userid)# to enter login id 
        driver.find_element_by_id(L.pwd).send_keys(passwrd) #to enter password
        driver.find_element_by_xpath(L.loginbutton).click() # to click
        #print("Application Title name is :" ,driver.title)
        #print(driver.find_element_by_class_name("user_panel").text)
        #print(driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr[1]/td/div[2]/font").text)
        time.sleep(2)
        
    
    def log_out(self):
        self.driver.find_element_by_class_name(L.logoutbtn).click()
        time.sleep(2)

