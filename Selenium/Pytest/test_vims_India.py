'''
Created on Dec 4, 2018

@author: subharad
'''

from selenium import webdriver
import time
import pytest
from test_login import Login
from test_homepage import homepage
#from selenium.webdriver.support.ui import Select

class TestVimsIndia():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome("C:/selenium_scripts/Selenium/driver/chromedriver.exe")
        #driver.delete_all_cookies()
        #driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        time.sleep(2)
        driver.close()
        driver.quit()
    
    def test_appointment_submit(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_appointment()
        apt.new_appointment()
        apt.visitor_type()
        apt.select_date_picker()
        apt.location_dropdown()
        apt.get_visitor_name()
        apt.get_visitor_org()
        apt.get_visitor_phone()
        apt.scroll_down()
        apt.vis_email()
        apt.vis_nationality()
        apt.vis_purpose()
        apt.scroll_up()
        apt.save_button()
        apt.app_confirm_head()
        apt.app_confirm_body()
        apt.app_confirm_ok()
        time.sleep(1)
        
    def test_update_entry(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_appointment()
        try:
            apt.edit_button()
            apt.select_date_picker()
            apt.get_visitor_name()
            apt.get_visitor_org()
            apt.update_button()
            time.sleep(4)
            apt.app_confirm_head()
            apt.app_confirm_body()
            apt.app_confirm_ok()
            time.sleep(1)
        except:
            print("there are no editable entries")
            
    def test_delete_yes(self,test_setup):
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
      
    def test_bulk_upload(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_bulk_app()
        time.sleep(2)
        apt.click_browse_file()
        apt.file_upload_india()
        apt.file_submit()
        apt.click_here()
        
    def test_report_appointment(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.report_menu_click()
        apt.appointment_report_run()
        apt.report_parameters()
        
    def test_report_badge(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.report_menu_click()
        apt.badge_report_run()
        apt.report_parameters()
        
    def test_report_alert(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.report_menu_click()
        apt.alert_report_run()
        apt.report_parameters()
        
    def test_archived_appointment(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.archived_report_menu_click()
        apt.appointment_report_run()
        apt.report_parameters()
        
    def test_archived_badge(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.archived_report_menu_click()
        apt.badge_report_run()
        apt.report_parameters()
        
        
    def test_archived_alert(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.archived_report_menu_click()
        apt.alert_report_run()
        apt.report_parameters()
        
        
        
        
        