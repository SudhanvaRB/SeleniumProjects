'''
Created on Feb 18, 2019

@author: subharad
'''
from selenium import webdriver
from test_login import Login
from test_homepage import homepage
import unittest
import time








class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(LoginTest, cls).setUpClass()
        cls.driver = webdriver.Chrome("C:\selenium_scripts\Selenium\driver\chromedriver.exe")
        #cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        
        
    def test_appointment_submit(self):
        driver = self.driver
        login = Login(driver)
        login.login()
        apt =homepage(driver)
        apt.click_appointment()
        try:
            apt.delete_btn()
            time.sleep(2)
            apt.delete_yes_message()
            time.sleep(2)
        except:
            print("no entries to delete")
        
        
        
        
    
    @classmethod
    def tearDownClass(cls):
        super(LoginTest, cls).tearDownClass()
        cls.driver.close()
        cls.driver.quit()