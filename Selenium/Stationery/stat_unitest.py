'''
Created on Apr 29, 2019

*** Stationery Application Test Cases
*** Unittest with Page Object Model Framework
*** Total 12 Test Scripts


@author: subharad
'''

from selenium import webdriver
import unittest
from login_page_stat import Login #Import Login class from login_page_stat page 
from Stationery.home_page_stat import HomePageStat  #Import HomePageStat class from home_page_stat page



class StatLogin(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        '''
        this method is run before every test case
        
        '''
        super(StatLogin, cls).setUpClass()
        cls.driver = webdriver.Chrome("C:\selenium_scripts\Selenium\driver\chromedriver.exe") # path of chromedriver
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        
    
        
    def test_01_login(self):
        '''
        Login method
        
        '''
        driver = self.driver
        log = Login(driver)
        log.login_func("anaraju","Test") #login_func function takes two parameters 1. username and 2. password
        
       
     
    def test_02_logout(self):
        driver = self.driver
        l = StatLogin()
        l.test_01_login()
        log = Login(driver)
        log.log_out()
      
    def test_03_select_project(self):
        driver = self.driver
        l = StatLogin()
        l.test_01_login()
        home = HomePageStat(driver)
        home.project_selection()
        
    
    def test_04_select_location(self):
        driver = self.driver
        l = StatLogin()
        l.test_01_login()
        home = HomePageStat(driver)
        home.location_selection()
        
  
        
    def test_05_add_product(self):
        driver = self.driver
        l = StatLogin()
        l.test_01_login()
        home = HomePageStat(driver)
        home.project_selection()
        home.location_selection()
        home.scroll_to_item()
        
    
    def test_06_submit_button(self):
        driver = self.driver
        l = StatLogin()
        l.test_01_login()
        home = HomePageStat(driver)
        home.project_selection()
        home.location_selection()
        home.scroll_to_item()
        home.submit_button()
        home.success_message()
        
    def test_07_update_cart(self):
        driver = self.driver
        l = StatLogin()
        l.test_01_login()
        home = HomePageStat(driver)
        home.add_more_products()
        home.scroll_to_update_item()
        
    def test_08_cancel_cart(self):
        driver = self.driver
        l = StatLogin()
        l.test_01_login()
        home = HomePageStat(driver)
        home.cancel_cart()
        
    def test_09_submit_with_empty_cart(self):
        driver = self.driver
        l = StatLogin()
        l.test_01_login()
        home = HomePageStat(driver)
        home.submit_button()
        home.empty_cart_message()
        
    def test_10_remove_button(self):
        driver = self.driver
        l = StatLogin()
        #l.test_01_login()
        l.test_06_submit_button()
        home = HomePageStat(driver)
        home.remove_link()
        
    def test_11_my_cart_link(self):
        driver = self.driver
        l = StatLogin()
        l.test_01_login()
        home = HomePageStat(driver)
        home.project_selection()
        home.location_selection()
        home.scroll_to_item()
        home.my_cart_link()
        home.empty_cart_button()
      
    def test_12_products_list(self):
        driver = self.driver
        l = StatLogin()
        l.test_01_login()
        home = HomePageStat(driver)
        home.project_selection()
        home.location_selection()
        home.product_list()
    
        
 
       

    @classmethod
    def tearDownClass(cls):
        super(StatLogin, cls).tearDownClass()
        cls.driver.close()
        cls.driver.quit()
        