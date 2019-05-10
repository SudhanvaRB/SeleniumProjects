from selenium import webdriver

import unittest

from Teamxfinal.test_methods import TeamxLogin





class LoginTestTeamx(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(LoginTestTeamx, cls).setUpClass()
        cls.driver = webdriver.Chrome("C:\selenium_scripts\Selenium\driver\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        
    def test_login(self):
        driver = self.driver
        log = TeamxLogin(driver)
        log.login()
        log.publish()
        print("test_login success")
        

    
    @classmethod
    def tearDownClass(cls):
        super(LoginTestTeamx, cls).tearDownClass()
        cls.driver.close()
        cls.driver.quit()
        


