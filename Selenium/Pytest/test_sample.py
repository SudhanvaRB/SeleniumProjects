'''
Created on Nov 27, 2018

@author: subharad
'''

from selenium import webdriver
import time
import pytest
from test_login import Login
from test_homepage import homepage
from test_locators import Locators

class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome("C:/selenium_scripts/Selenium/driver/chromedriver.exe")
        #driver.delete_all_cookies()
        driver.implicitly_wait(10)
        driver.maximize_window()
        #driver.get("http://10.100.245.80:92/VMS/login")
        yield
        time.sleep(2)
        driver.close()
        driver.quit()
        
    def test_login(self,test_setup):
        self.driver.get("http://10.100.245.80:92/VMS/login")
        #wk = openpyxl.load_workbook()
        self.driver.find_element_by_id(Locators.username_text_box).send_keys("tihollan")
        self.driver.find_element_by_id(Locators.login_button).click()
        time.sleep(1)
    
        
        
        
        