'''
Created on Jan 16, 2019

@author: subharad
'''
from selenium import webdriver

import unittest
import time

from Teamxfinal.test_methods import TeamxLogin
from teamx_locators import TeamxLocators

'''
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
'''


class LoginTestTeamx(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(LoginTestTeamx, cls).setUpClass()
        cls.driver = webdriver.Chrome("C:\selenium_scripts\Selenium\driver\chromedriver.exe")
        
        '''
        #for firefox
        binary = FirefoxBinary("C:\\Users\\subharad\\AppData\\Local\\Mozilla Firefox\\firefox.exe")
        capabilities_argument = DesiredCapabilities().FIREFOX
        capabilities_argument["marionette"] = True
        cls.driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities_argument,executable_path="C:\\selenium_scripts\\Selenium\\driver\\geckodriver.exe")
        cls.driver.implicitly_wait(10)
        '''
        cls.driver.maximize_window()
        
    def test_login(self):
        driver = self.driver
        log = TeamxLogin(driver)
        log.login_employee()
        print(driver.title)
        
   
        log.my_approvals()
        time.sleep(3)
        ele = driver.find_element_by_xpath(TeamxLocators.img_scc_1)
        driver.execute_script("arguments[0].scrollIntoView()", ele)
        time.sleep(2)
        log.my_ideas()
        #time.sleep(2)
        val = self.driver.find_element_by_xpath("//*[@id='myIdeasList']/tbody/tr[1]/td[2]")
        print(val.text)
        ro = self.driver.find_elements_by_xpath("//*[@id='myIdeasList']/tbody/tr")
        lenth = len(ro)
        print(lenth)
        co = self.driver.find_elements_by_xpath("//*[@id='myIdeasList']/tbody/tr[1]/td")
        cols = len (co)
        print(cols)
        
        for r in range(1,lenth+1): #iterates over webtable and prints all values
            for c in range(1,cols+1):
                if r <= 1:
                    val = self.driver.find_element_by_xpath("//*[@id='myIdeasList']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
                    print(val,end='           ')
            print()
        


    
        
        

    
    @classmethod
    def tearDownClass(cls):
        super(LoginTestTeamx, cls).tearDownClass()
        cls.driver.close()
        cls.driver.quit()