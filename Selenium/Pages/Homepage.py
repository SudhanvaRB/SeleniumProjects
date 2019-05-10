'''
Created on Nov 2, 2018

@author: subharad
'''
from Locators.locators import Locators
from datetime import date
from datetime import timedelta

class homepage():
    
    def __init__(self,driver):
        self.driver = driver
        
    
    def click_logout(self):
        self.driver.find_element_by_xpath(Locators.logout_button).click()
        
    def click_appointment(self):
        self.driver.find_element_by_xpath(Locators.appointment).click()
    
    def new_appointment(self):
        self.driver.find_element_by_xpath(Locators.appointment_1).click()
        
    def location(self):
        element = self.driver.find_element_by_xpath(Locators.location)
        return element
    
    def select_date(self):
        date_picker = self.driver.find_element_by_xpath(Locators.date)
        return date_picker
    
    def get_date(self):
        act_dt = date.today() + timedelta(days=1)
        act_dt = act_dt.strftime("%Y/%m/%d")
        return act_dt
    
    def get_visitor_name(self):
        self.driver.find_element_by_xpath(Locators.visitor_name).send_keys("sudhanva")
        
    def get_visitor_org(self):
        self.driver.find_element_by_xpath(Locators.visitor_organization).send_keys("MNCorp")
        
    def get_visitor_phone(self):
        self.driver.find_element_by_xpath(Locators.visitor_mobile_no).send_keys("9738283930")
     
    def save_button(self): 
        self.driver.find_element_by_xpath(Locators.save_btn).click()  
        
    def blank_date_assert(self):
        element = self.driver.find_element_by_xpath(Locators.start_date_error)
        assert element.text == 'Please Enter Appointment Start date.'
        
    def character_only_assert(self):
        element = self.driver.find_element_by_xpath(Locators.character_error)
        assert element.text == 'Use Characters only.'
        
    def mobilno_error_assert(self):
        element = self.driver.find_element_by_xpath(Locators.phone_error)
        assert element.text == 'Please enter valid mobile number.'
        
    def cancel_button(self):
        self.driver.find_element_by_xpath(Locators.cancel_btn).click()
        
    def search_field(self):
        self.driver.find_element_by_xpath(Locators.search_box).send_keys("AU1311180004")
        
    def app_visitor_assert(self):
        element = self.driver.find_element_by_xpath(Locators.appointment_visitor)
        assert element.text == 'Visitor'
        
    def app_appointment_assert(self):
        element = self.driver.find_element_by_xpath(Locators.Appointment_Visitor)
        assert element.text == 'Appointment'
    #===========================================================================
    #     
    # def graph_color(self):
    #     colr = self.driver.find_element_by_xpath(Locators.graph_color).get_color()
    #     print("color is" + colr)
    #===========================================================================
    #===========================================================================
    # def image_assert(self):
    #     images = self.driver.find_element_by_xpath(Locators.title_image)
    #     assert images == "http://10.100.245.80:92/vms/images/logo.png"
    #===========================================================================
    #===========================================================================
    # def enter_date(self):
    #     next_day = date.today() + timedelta(days=1) 
    #     return next_day
    #     
    #===========================================================================