'''
Created on Oct 12, 2018

@author: subharad
'''
from selenium import webdriver
import time
import unittest
from Pages.Loginpage import loginpage
from Pages.Homepage import homepage
import HtmlTestRunner
from selenium.webdriver.support.ui import Select




class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(LoginTest, cls).setUpClass()
        cls.driver = webdriver.Chrome("C:\selenium_scripts\Selenium\driver\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        
    def test_login(self):
        driver = self.driver
        login = loginpage(driver)
        login.login()
        time.sleep(2)
        print("test_login success")
        
    #===========================================================================
    # def test_login_valid(self):
    #     driver = self.driver
    #     global username,path1
    #     path1 = "http://10.100.245.80:92/VMS/login"
    #     username = "tihollan"
    #     driver.get(path1)
    #     login = loginpage(driver)
    #     login.enter_username(username)
    #     login.click_login()
    #     time.sleep(2)
    #===========================================================================
    
    def test_logout(self):    
        driver = self.driver
        login = loginpage(driver)
        login.login()
        time.sleep(2)
        logout = homepage(driver)
        logout.click_logout()
        time.sleep(2)
        print("test_logout success")
        
    #===========================================================================
    # def test_logout(self):
    #     driver = self.driver
    #     driver.get(path1)
    #     login = loginpage(driver)
    #     login.enter_username(username)
    #     login.click_login()
    #     time.sleep(1)
    #     logout = homepage(driver)
    #     logout.click_logout()
    #     time.sleep(1)
    #===========================================================================
    
    def test_appointment(self):
        driver = self.driver
        login = loginpage(driver)
        login.login()
        time.sleep(1)
        apt = homepage(driver)
        apt.click_appointment()
        time.sleep(1)
        apt.app_appointment_assert()#asserting the Appointment
        apt.app_visitor_assert()#asserting the Appointment > Visitor 
        apt.new_appointment()
        time.sleep(1)
        print("test_appointment success")
        
    
    #===========================================================================
    # def test_location_dropdown_new(self):
    #     driver = self.driver
    #     dpdwn = LoginTest(driver)
    #     dpdwn.test_appointment()
    #     time.sleep(2)
    #     apt = homepage(driver)
    #     loc = apt.location()
    #     drp = Select(loc)
    #     drp.select_by_value(value="1009")
    #     time.sleep(1)
    #     print("test_location_dropdown success")
    #     
    #===========================================================================
        
         
    #===========================================================================
    # def test_appointment(self):
    #     driver = self.driver
    #     driver.get(path1)
    #     login = loginpage(driver)
    #     login.enter_username(username)
    #     login.click_login()
    #     time.sleep(2)
    #     apt = homepage(driver)
    #     apt.click_appointment()
    #     time.sleep(2)
    #===========================================================================
#         
    #===========================================================================
    # def test_new_appointment(self):
    #     driver = self.driver
    #     driver.get(path1)
    #     login = loginpage(driver)
    #     login.enter_username(username)
    #     login.click_login()
    #     time.sleep(4)
    #     apt = homepage(driver)
    #     apt.click_appointment()
    #     time.sleep(4)
    #     apt.new_appointment()
    #     time.sleep(4)
    #     
    #===========================================================================
    def test_location_dropdown(self):
        driver = self.driver
        login = loginpage(driver)
        login.login()
        time.sleep(1)
        apt = homepage(driver)
        apt.click_appointment()
        time.sleep(1)
        apt.new_appointment()
        time.sleep(1)
        loc = apt.location()
        drp = Select(loc)
        drp.select_by_value(value="1009")
        time.sleep(1)
        driver.save_screenshot('C:\selenium_scripts\screenshots\screenshot.png')
        print("test_location_dropdwon success")
        
   
    def test_date_picker(self):
        driver = self.driver
        login = loginpage(driver)
        login.login()
        time.sleep(1)
        apt = homepage(driver)
        apt.click_appointment()
        time.sleep(1)
        apt.new_appointment()
        time.sleep(1)
        sb_dt = apt.select_date()
        driver.execute_script("arguments[0].removeAttribute('readonly')", sb_dt)
        sb_dt.send_keys(apt.get_date())
        time.sleep(1)
        print("test_date_picker success")
        
    def test_visitor_name(self):
        driver = self.driver
        login = loginpage(driver)
        login.login()
        time.sleep(1)
        apt = homepage(driver)
        apt.click_appointment()
        time.sleep(1)
        apt.new_appointment()
        time.sleep(1)
        apt.get_visitor_name()
        time.sleep(1)
        print("test_visitor_name success")
        
    def test_visitor_org(self):
        driver = self.driver
        login = loginpage(driver)
        login.login()
        time.sleep(1)
        apt = homepage(driver)
        apt.click_appointment()
        time.sleep(1)
        apt.new_appointment()
        time.sleep(1)
        apt.get_visitor_org()
        time.sleep(1)
        print("test_visitor_org success")
        
    def test_visitor_phone(self):
        driver = self.driver
        login = loginpage(driver)
        login.login()
        time.sleep(1)
        apt = homepage(driver)
        apt.click_appointment()
        time.sleep(1)
        apt.new_appointment()
        time.sleep(1)
        apt.get_visitor_phone()
        time.sleep(1)
        print("test_visitor_phone success")
        
    def test_save_button(self):
        driver = self.driver
        login = loginpage(driver)
        login.login()
        time.sleep(1)
        apt = homepage(driver)
        apt.click_appointment()
        time.sleep(1)
        apt.new_appointment()
        time.sleep(1)
        apt.save_button()
        time.sleep(2)
        apt.blank_date_assert()
        apt.character_only_assert()
        apt.mobilno_error_assert()
        print("test_save_button success")
        
    def test_cancel_button(self):
        driver = self.driver
        login = loginpage(driver)
        login.login()
        time.sleep(1)
        apt = homepage(driver)
        apt.click_appointment()
        time.sleep(1)
        apt.new_appointment()
        time.sleep(1)
        apt.get_visitor_name()
        time.sleep(1)
        apt.cancel_button()
        time.sleep(1)
        print("test_cancel_button success")
        
    def test_search_field(self):
        driver = self.driver
        login = loginpage(driver)
        login.login()
        time.sleep(1)
        apt = homepage(driver)
        apt.click_appointment()
        time.sleep(1)
        apt.search_field()
        time.sleep(2)
        print("test_search_field success")

        
        
    @classmethod
    def tearDownClass(cls):
        super(LoginTest, cls).tearDownClass()
        cls.driver.close()
        cls.driver.quit()
        
        
if __name__ == '__main__':
   
    #unittest.main(testRunner=xmlrunner.XMLTestRunner(output="C:\selenium_scripts\Selenium\Reports"))
    
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/selenium_scripts/Selenium/Reports"))