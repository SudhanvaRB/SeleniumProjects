'''
Created on Nov 9, 2018

@author: subharad
'''

from selenium import webdriver
import time
import pytest
from test_login import Login
from test_homepage import homepage
#from selenium.webdriver.support.ui import Select

class TestSample():
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
    
        
    def test_login(self,test_setup):
        login = Login(driver)
        login.login()
        
        
        
    def test_logout(self,test_setup):    
        login = Login(driver)
        login.login()
        logout = homepage(driver)
        logout.click_logout()
        
       
        
    def test_welcome(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.welcome_message()#assert welcome message
        
        
    
    def test_appointment(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_appointment()
        apt.app_appointment_assert()#asserting the Appointment
        apt.app_visitor_assert()#asserting the Appointment > Visitor 
        apt.new_appointment()
        
        #print("test_appointment success")
        
    def test_location_dropdown(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_appointment()
        apt.new_appointment()
        apt.location_dropdown()
        #driver.save_screenshot('C:/selenium_scripts/screenshots/location_dropdown.png')
        #print("test_location_dropdwon success")
        
    def test_date_picker(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_appointment()
        apt.new_appointment()
        apt.select_date_picker()
        #driver.save_screenshot('C:/selenium_scripts/screenshots/date_picker.png')
        #print("test_date_picker success")
        
    def test_visitor_name(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_appointment()
        apt.new_appointment()
        apt.get_visitor_name()
       
        #print("test_visitor_name success")
        
    def test_visitor_org(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_appointment()
        apt.new_appointment()
        apt.get_visitor_org()
        
        #print("test_visitor_org success")
        
    def test_visitor_phone(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_appointment()
        apt.new_appointment()
        apt.get_visitor_phone()
        driver.save_screenshot('C:/selenium_scripts/screenshots/visitor_phone.png')
        #print("test_visitor_phone success")
        
    def test_save_button(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_appointment()
        apt.new_appointment()
        apt.save_button()
        time.sleep(2)
        apt.blank_date_assert()
        apt.character_only_assert()
        apt.mobilno_error_assert()
        #print("test_save_button success")
        
    def test_cancel_button(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_appointment()
        apt.new_appointment()
        apt.get_visitor_name()
        apt.cancel_button()
        time.sleep(1)
        #print("test_cancel_button success")
        
    def test_search_field(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_appointment()
        apt.search_field()
        time.sleep(2)
        #print("test_search_field success")
     
    def test_search_no_record_found(self,test_setup):   
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_appointment()
        apt.search_no_record()
        time.sleep(1)
        
    def test_appointment_submit(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_appointment()
        apt.new_appointment()
        apt.select_date_picker()
        apt.location_dropdown()
        apt.get_visitor_name()
        apt.get_visitor_org()
        apt.get_visitor_phone()
        apt.save_button()
        time.sleep(4)
        apt.app_confirm_head()
        apt.app_confirm_body()
        apt.app_confirm_ok()
        time.sleep(1)
        
    def test_app_already_exists(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_appointment()
        apt.new_appointment()
        apt.select_date_picker()
        apt.location_dropdown()
        apt.get_visitor_name()
        apt.get_visitor_org()
        apt.get_visitor_phone()
        apt.save_button()
        time.sleep(2)
        apt.app_exist_msg()
        try:
            apt.app_exists_ok()
        except:
            print("no duplicate entries found")
        
    def test_delete_message(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_appointment()
        try:
            apt.delete_btn()
            apt.delete_btn_pop_up_message()
        except:
            print("no entries to delete")
            
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
      
        
    def test_delete_no(self,test_setup):
        login = Login(driver)
        login.login()
        apt =homepage(driver)
        apt.click_appointment()
        try:
            apt.delete_btn()
            time.sleep(1)
            apt.delete_cancel()
        except:
            print("no entries to delete")
        
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
        
    def test_show_entries(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_appointment()
        apt.show_entries()
        
        
    # Check In page
    
    def test_check_in(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_check_menu()
        apt.click_check_in()
        apt.click_badge_icon()
       
    def test_check_in_details(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_check_menu()
        apt.click_check_in()
        try:
            apt.click_appointment_id()
            driver.save_screenshot('C:/selenium_scripts/screenshots/check_in.png')
            apt.check_location_dropdown()
            apt.click_check_box()
            apt.rules_ok_button()
        except:
            print("No appointments to Check In")
       
        #apt.click_confirm_check()
        
    def test_check_out(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_check_menu()
        apt.click_check_out()
        apt.click_check_out_image()
        apt.reprint_content_print()
        apt.reprint_dropdown()
        apt.remark_dropdown()
        apt.checkedout_button_click()
        
    def test_bulk_upload(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_bulk_app()
        time.sleep(2)
        apt.click_browse_file()
        apt.file_upload_usa()
        apt.file_submit()
        apt.click_here()
        
    def test_report(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.report_menu_click()
        apt.appointment_report_run()
        apt.report_parameters()
        
    def test_bulk_check_out_single(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_check_menu()
        apt.bulk_check_out_menu()
        apt.bulk_check_box_single()
        apt.bulk_check_out_btn()
        apt.bulk_check_out_success_message()
        apt.bulk_checl_out_close()
        
    def test_bulk_check_out(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.click_check_menu()
        apt.bulk_check_out_menu()
        apt.bulk_check_box()
        apt.bulk_check_out_btn()
        apt.bulk_check_out_success_message()
        apt.bulk_checl_out_close()
        
        
    def test_dashboard(self,test_setup):
        login = Login(driver)
        login.login()
        apt = homepage(driver)
        apt.dashboard_appointments()
#===============================================================================
# 
#         driver.get("http://10.100.245.80:92/VMS/login")
#         driver.find_element_by_id("UserId").send_keys("tihollan")
#         driver.find_element_by_id("btnSubmit").click()
#         x = driver.title
#         assert x =="Visitor Management System"
#===============================================================================
        
    
    
    
    