'''
Created on Nov 14, 2018

@author: subharad

Created on Nov 2, 2018

@author: subharad
'''

#from DataDriven import xlutil
from test_locators import Locators
from datetime import date
from datetime import timedelta
import time
import names
import random
from selenium.webdriver.support.ui import Select  #mainly used for drop downs
import autoit
import pyautogui

class homepage():
    
    def __init__(self,driver):
        self.driver = driver
        
    
    def click_logout(self):
        self.driver.find_element_by_xpath(Locators.logout_button).click()
        time.sleep(1)
        
    def click_appointment(self):
        self.driver.find_element_by_xpath(Locators.appointment).click()
        time.sleep(1)
    
    def new_appointment(self):
        self.driver.find_element_by_xpath(Locators.appointment_1).click()
        time.sleep(1)
        
    def location(self):
        element = self.driver.find_element_by_xpath(Locators.location)
        return element
    
    def location_dropdown(self):
        element = self.driver.find_element_by_xpath(Locators.location)
        drp =  Select(element)
        drp.select_by_index(1)
        time.sleep(1)
        

            
    def city_list(self,city_name):#data driven
        element = self.driver.find_element_by_xpath(Locators.location)
        drp =  Select(element)
        time.sleep(1)
        drp.select_by_visible_text(city_name)
        time.sleep(1)
        

        
    def multiple_appointment(self):
        self.driver.find_element_by_id(Locators.mul).click()
        time.sleep(1)
    

    
    def select_date_picker(self):
        self.driver.find_element_by_xpath(Locators.date).clear()
        date_picker = self.driver.find_element_by_xpath(Locators.date)
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", date_picker)
        act_dt = date.today() + timedelta(days=1)
        act_dt = act_dt.strftime("%Y/%m/%d")
        date_picker.send_keys(act_dt)
        time.sleep(1)
        
    def date_picker_validations(self):
        driver = self.driver
        driver.find_element_by_id(Locators.end_date).clear()
        date_picker = driver.find_element_by_id(Locators.end_date)
        driver.execute_script("arguments[0].removeAttribute('readonly')", date_picker)
        act_dt = date.today() + timedelta(days=2)
        act_dt = act_dt.strftime("%Y/%m/%d")
        date_picker.send_keys(act_dt)
        time.sleep(1)
        hp = homepage(driver)
        hp.save_button()
        
    def insert_date(self,enterdate): #data driven
        self.driver.find_element_by_xpath(Locators.date).clear()
        date_picker = self.driver.find_element_by_xpath(Locators.date)
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", date_picker)
        act_dt = enterdate
        
        act_dt = act_dt.strftime("%Y/%m/%d %H:%M")
        date_picker.send_keys(act_dt)
        time.sleep(1)
        
    def insert_enddate(self,enterdate): #data driven
        self.driver.find_element_by_id(Locators.end_date).clear()
        date_picker = self.driver.find_element_by_id(Locators.end_date)
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", date_picker)
        act_dt = enterdate
        
        act_dt = act_dt.strftime("%Y/%m/%d %H:%M")
        date_picker.send_keys(act_dt)
        time.sleep(1)
        
    def date_string(self,inp):
        self.driver.find_element_by_xpath(Locators.date).clear()
        date_picker = self.driver.find_element_by_xpath(Locators.date)
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", date_picker)
        act_dt = inp
        date_picker.send_keys(act_dt)
        time.sleep(1)
    
    def enddate_string(self,inp):
        self.driver.find_element_by_id(Locators.end_date).clear()
        date_picker = self.driver.find_element_by_id(Locators.end_date)
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", date_picker)
        act_dt = inp
        date_picker.send_keys(act_dt)
        time.sleep(1)    
        
        
        
        
        
        
        
        
    
    def get_visitor_name(self):
        #self.driver.find_element_by_xpath(Locators.visitor_name).send_keys("nimbrt")
        self.driver.find_element_by_xpath(Locators.visitor_name).clear()
        self.driver.find_element_by_xpath(Locators.visitor_name).send_keys(names.get_last_name())
        time.sleep(1)
        
    def enter_vis_name(self,visname): #data driven
        self.driver.find_element_by_xpath(Locators.visitor_name).clear()
        self.driver.find_element_by_xpath(Locators.visitor_name).send_keys(visname)
        time.sleep(1)
        
        
        
    def get_visitor_org(self):
        #self.driver.find_element_by_xpath(Locators.visitor_organization).send_keys("MNfCorpggssa")
        self.driver.find_element_by_xpath(Locators.visitor_organization).clear()
        self.driver.find_element_by_xpath(Locators.visitor_organization).send_keys(names.get_last_name())
        time.sleep(1)
        
    def enter_vis_org(self,visorg):   #data driven
        #self.driver.find_element_by_xpath(Locators.visitor_organization).send_keys("MNfCorpggssa")
        self.driver.find_element_by_xpath(Locators.visitor_organization).clear()
        self.driver.find_element_by_xpath(Locators.visitor_organization).send_keys(visorg)
        time.sleep(1)
        
    def get_visitor_phone(self):
        rad = random.randint(1000000000,9999999999)
        self.driver.find_element_by_xpath(Locators.visitor_mobile_no).send_keys(rad)
        time.sleep(1)
        #self.driver.find_element_by_xpath(Locators.visitor_mobile_no).send_keys("8731245930")
        
    def enter_visphone(self,visphone):  #datadriven
        
        self.driver.find_element_by_xpath(Locators.visitor_mobile_no).send_keys(visphone)
        time.sleep(1)
     
    def save_button(self): 
        self.driver.find_element_by_xpath(Locators.save_btn).click() 
        time.sleep(4)
        
    def welcome_message(self): 
        ele = self.driver.find_element_by_xpath(Locators.welcome_user)
        print(ele.text)
        #assert ele.text == "Welcome Timothy Holland"
        
    def blank_date_assert(self):
        element = self.driver.find_element_by_xpath(Locators.start_date_error)
        print(element.text)
        #assert  == 'Please Enter Appointment Start date123123.'
        
    def character_only_assert(self):
        element = self.driver.find_element_by_xpath(Locators.character_error)
        print(element.text)
        #assert element.text == 'Use Characters only.'
        
    def mobilno_error_assert(self):
        element = self.driver.find_element_by_xpath(Locators.phone_error)
        print(element.text)
        #assert element.text == 'Please enter valid mobile number.'
        
    def cancel_button(self):
        self.driver.find_element_by_xpath(Locators.cancel_btn).click()
        
    def search_field(self):
        #self.driver.find_element_by_xpath(Locators.search_box).send_keys("AU1311180004")
        srch = self.driver.find_element_by_xpath(Locators.search_box)
        inpt= self.driver.find_element_by_xpath(Locators.srch_box_input)
        srch.send_keys(inpt.text)
        print("searched element is:" + inpt.text)
        
    def search_record(self,appointment_id): #ddt
        self.driver.find_element_by_xpath(Locators.search_box).send_keys(appointment_id)
        
        
        
    def search_no_record(self):
        inpt = names.get_last_name()
        self.driver.find_element_by_xpath(Locators.search_box).send_keys(inpt)
        outpt = self.driver.find_element_by_xpath(Locators.srch_no_record)
        print("searched element is:" + inpt)
        print(outpt.text)
        
    def app_visitor_assert(self):
        element = self.driver.find_element_by_xpath(Locators.appointment_visitor)
        print(element.text)
        #assert element.text == 'Visitor'
        
    def app_appointment_assert(self):
        element = self.driver.find_element_by_xpath(Locators.Appointment_Visitor)
        print(element.text)
        #assert element.text == 'Appointment'
        
    def delete_btn(self):
        self.driver.find_element_by_xpath(Locators.delete_button).click()
        time.sleep(1)
        
        
    def edit_button(self):
        self.driver.find_element_by_xpath(Locators.edit_button).click()
        time.sleep(1)
        
           
        
        
    #===========================================================================
    # def edit_button_find(self):
    #     if self.driver.find_element_by_xpath(Locators.edit_button) is None:
    #         self.driver.find_element_by_xpath("//*[@id='AptTable_next']/a").click()
    #         time.sleep(2)
    #         self.driver.find_element_by_xpath(Locators.edit_button).click()
    #     else:
    #         self.driver.find_element_by_xpath(Locators.edit_button).click()
    #===========================================================================
        
    def update_button(self):
        self.driver.find_element_by_xpath(Locators.update_button).click()
        
    def delete_btn_pop_up_message(self):
        obj = self.driver.switch_to_alert()
        msg = obj.text
        print("Clicking on delete button shows the following message" + msg)
        
    def delete_yes_message(self):
        obj = self.driver.switch_to_alert()
        time.sleep(2)
        obj.accept()
        time.sleep(2)
        obj = self.driver.switch_to_alert()
        time.sleep(2)
        msg = obj.text
        print("Delete confirm shows the following message: "+ msg)
        
    def delete_cancel(self):
        obj = self.driver.switch_to_alert()
        time.sleep(2)
        obj.dismiss
        time.sleep(1)
        
    def app_confirm_head(self):
        hdr = self.driver.find_element_by_xpath(Locators.app_cpnfirm_head)
        print("Header Text :" + hdr.text)
        
    def app_confirm_body(self):
        print(self.driver.find_element_by_xpath(Locators.app_confirm_msg).text)
        
        
    def app_confirm_ok(self):
        ok = self.driver.find_element_by_xpath(Locators.app_confirm_ok_btn)
        ok.click()
        
    def app_exists_ok(self):
        ok = self.driver.find_element_by_xpath(Locators.app_exists_ok_btn)
        ok.click()
        
    def app_exist_msg(self):
        obj = self.driver.switch_to_active_element()
        print(obj.text)
        
    def show_entries(self):  #scroll functionality used here
        ent = self.driver.find_element_by_xpath(Locators.show_entries_drpdown)
        drop = Select(ent)
        lst = ["10","25","50","100"]
        for i in lst:
            drop.select_by_value(value=i)
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            cnt = self.driver.find_element_by_xpath(Locators.show_entries_count)
            print(cnt.text)
            self.driver.find_element_by_xpath(Locators.show_next).click()
            time.sleep(1)
            self.driver.find_element_by_xpath(Locators.show_previous).click()
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
            time.sleep(1)
            
            
    ############################################### CHECK IN PAGE METHODS##############################################
            
            
    def click_check_menu(self):
        self.driver.find_element_by_xpath(Locators.check_menu).click()
        time.sleep(1)
        
    def click_check_in(self):
        self.driver.find_element_by_xpath(Locators.check_in).click()
        time.sleep(1)
        
    def click_check_out(self):
        self.driver.find_element_by_xpath("//*[@id='liVisitorCheckOut']").click()
        time.sleep(3)
        
    def click_check_out_france(self):
        self.driver.find_element_by_link_text(Locators.check_out_france).click()
        time.sleep(1)
        
    def click_check_out_poland(self):
        self.driver.find_element_by_link_text(Locators.check_out_poland).click()
        time.sleep(1)
        
    def click_check_out_netherlands(self):
        self.driver.find_element_by_link_text(Locators.check_out_netherlands).click()
        time.sleep(1)
        
        
        
        
    def click_appointment_id(self):
        self.driver.find_element_by_xpath(Locators.appointment_id).click()
        time.sleep(1)
        
    def search_app_id(self,app_id): #ddt
        self.driver.find_element_by_xpath(Locators.search_checkin).send_keys(app_id)
        time.sleep(1)
        
    def click_app_id(self):
        self.driver.find_element_by_xpath(Locators.link_check_in).click()
        time.sleep(1)
        
        
    def check_location_dropdown(self):
        element = self.driver.find_element_by_xpath(Locators.location_check)
        drp =  Select(element)
        drp.select_by_index(2)
        time.sleep(1)
        
    def check_in_location_dropdown(self,location):
        element = self.driver.find_element_by_xpath(Locators.location_check)
        self.driver.save_screenshot('C:/selenium_scripts/screenshots/check_in.png')
        drp =  Select(element)
        drp.select_by_visible_text(location)
        time.sleep(1)
        
    def click_check_box(self):
        self.driver.find_element_by_class_name(Locators.check_box).click()
        time.sleep(2)
        
        
    def rules_ok_button(self):
        hed = self.driver.find_element_by_xpath(Locators.rules_head)
        print(hed.text.encode("utf-8"))
        bdy = self.driver.find_element_by_xpath(Locators.rules_body)
        print(bdy.text.encode("utf-8"))
        self.driver.find_element_by_xpath(Locators.rules_ok_button).click()
        time.sleep(1)
        
    def click_badge_icon(self):
        try:
            self.driver.find_element_by_xpath(Locators.check_in_print_badge).click()
            time.sleep(15)
        except:
            print("there are no badges to print at this moment")
            
            
    def window_handles(self):#ddt
        driver = self.driver
        window_before = driver.window_handles[0] #handling browser windows during print
        time.sleep(1)
        apt = homepage(driver)
        apt.click_badge_icon()
        window_after = driver.window_handles[1] #handling browser windows during print
        driver.switch_to_window(window_after)
        time.sleep(5)
        pyautogui.moveTo(587,10)
        time.sleep(2)
        driver.save_screenshot('C:/selenium_scripts/screenshots/badge_check_in.png')
        time.sleep(2)
        pyautogui.click()
        time.sleep(5)
        driver.switch_to_window(window_before)
        time.sleep(2)
        print("here")
        
    def window_handles_new(self):
        driver = self.driver
        print(driver.title)
        window_before = driver.window_handles[0] #handling browser windows during print
        time.sleep(2)
        apt = homepage(driver)
        apt.click_badge_icon()
        time.sleep(2)
        window_after = driver.window_handles[1] #handling browser windows during print
        driver.switch_to_window(window_after)
        print(driver.title)
        time.sleep(2)
        driver.maximize_window()
        driver.close()
        driver.switch_to_window(window_before)
        print(driver.title)
        time.sleep(2)

                                        
            
            
    def confirm_cancel(self):
        '''
        pyautogui.moveTo(601,698)
        time.sleep(1)
        pyautogui.click()
        '''
        self.driver.find_element_by_id("btnConfirm").click()
        time.sleep(2)
        txt = self.driver.switch_to_active_element().text
        print(txt.encode("utf-8"))
        time.sleep(1)
        self.driver.find_element_by_xpath(Locators.ok_button).click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[text()='Cancel']").click()
        #self.driver.find_element_by_xpath("/html/body/section/div/div[3]/div/div/div[1]/div/div[4]/button[2]").click()
        time.sleep(1)
        '''
        pyautogui.moveTo(750,698)
        time.sleep(1)
        pyautogui.click()
        time.sleep(3)
        '''
       
       
            
      
       
       
    ###########################################CHECK OUT PAGE METHODS##################################################
    
    def search_check_out(self,check_out_id):
        self.driver.find_element_by_xpath(Locators.check_out_search).send_keys(check_out_id)
        time.sleep(1)
        
    def click_confirm_check(self):
        self.driver.find_element_by_id(Locators.confirm_check_button).click()
        time.sleep(1)
        
    def click_check_out_image(self):
        self.driver.find_element_by_xpath(Locators.click_checkout_img).click()
        time.sleep(6)
        
    def reprint_content_print(self):
        print(self.driver.find_element_by_xpath(Locators.badge_number).text)
        print(self.driver.find_element_by_xpath(Locators.badge_number_value).text)
        print(self.driver.find_element_by_xpath(Locators.badge_date).text)
        print(self.driver.find_element_by_xpath(Locators.badge_date_value).text)
        print(self.driver.find_element_by_xpath(Locators.visitor_name_head).text)
        print(self.driver.find_element_by_xpath(Locators.visitor_name_value).text)
        print(self.driver.find_element_by_xpath(Locators.visitor_org_head).text)
        print(self.driver.find_element_by_xpath(Locators.visitor_org_value).text)
        print(self.driver.find_element_by_xpath(Locators.host_name_head).text)
        print(self.driver.find_element_by_xpath(Locators.host_name_value).text)
       
        
   
    def reprint_dropdown(self):
        element = self.driver.find_element_by_id(Locators.reprint_badge_drop_down)
        drp =  Select(element)
        drp.select_by_value(value="2")
        time.sleep(2)
    
    def remark_dropdown(self):
        ele = self.driver.find_element_by_id(Locators.remarks_drop_down)
        drp = Select(ele)
        drp.select_by_value(value="18")
        time.sleep(2)
        
    def remark_submit_click(self):
        self.driver.find_element_by_xpath(Locators.reprint_submit_button).click()
        time.sleep(1)
        
    def checkedout_button_click(self):
        self.driver.find_element_by_xpath(Locators.checkedout_button).click()
        time.sleep(1)
        
        
    ############################################BULK CHECK OUT##################################################
    
    def bulk_check_out_menu(self):
        self.driver.find_element_by_link_text(Locators.bulk_check_out).click()
        time.sleep(2)
     
    def bulk_check_out_france(self):
        self.driver.find_element_by_link_text(Locators.bulk_france).click()
        time.sleep(2)
        
    def bulk_check_out_poland(self):
        self.driver.find_element_by_link_text(Locators.bulk_poland).click()
        time.sleep(2)
        
    def bulk_check_out_netherlands(self):
        self.driver.find_element_by_link_text(Locators.bulk_netherlands).click()
        time.sleep(2)
    
        
    def bulk_check_out_btn(self):
        self.driver.find_element_by_id(Locators.bulk_check_out_btn).click()
        time.sleep(2)
        
    def bulk_check_box(self):
        self.driver.find_element_by_id(Locators.bulk_check_box).click()
        time.sleep(1)
        self.driver.find_element_by_id(Locators.bulk_check_box).click()
        time.sleep(1)
        self.driver.find_element_by_id(Locators.bulk_check_box).click()
        time.sleep(1)
        
        
    def bulk_check_box_single(self):
        self.driver.find_element_by_css_selector(Locators.bulk_check_single).click()
        time.sleep(2)
        
    def bulk_check_out_success_message(self):
        print(self.driver.find_element_by_class_name(Locators.bulk_check_out_modal_content).text)
        
    def bulk_checl_out_close(self):
        self.driver.find_element_by_xpath(Locators.bulk_check_out_close).click()
        
    ###################################################BULK APPOINTMENT METHODS##############################################
    def click_bulk_app(self):
        self.driver.find_element_by_xpath(Locators.bulk_appointment).click()
        time.sleep(1)
    
    def click_browse_file(self):
        self.driver.find_element_by_class_name(Locators.browse_file).click()
        time.sleep(3)
        
    def file_upload_usa(self):
        autoit.win_active("Open") 
        autoit.control_set_text("Open","Edit1",r"C:\selenium_scripts\upload\AppointmentUpload_US (1).xlsx")
        autoit.control_send("Open","Edit1","{ENTER}")
        time.sleep(2)
        
    def file_upload_aus(self):
        autoit.win_active("Open") 
        autoit.control_set_text("Open","Edit1",r"C:\selenium_scripts\upload\AppointmentUpload_AUS.xlsx")
        autoit.control_send("Open","Edit1","{ENTER}")
        time.sleep(2)
        
        
    def file_submit(self):
        self.driver.find_element_by_id(Locators.upload_submit_button).click()
        time.sleep(20)
        ele =self.driver.find_element_by_xpath(Locators.discrepancy_title)
        scrll = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        if ele.is_displayed():
            print(self.driver.find_element_by_id(Locators.table_error).text)
            self.driver.find_element_by_xpath(Locators.error_cancel).click()
            scrll
        else:
            scrll
            
        print(self.driver.find_element_by_id(Locators.bulk_table_summary).text)
        time.sleep(2)
        
    def click_here(self):
        self.driver.find_element_by_xpath(Locators.click_here_link).click()
        time.sleep(2)
        
    ####################################REPORTS OBJECTS#######################################
    def report_menu_click(self):
        self.driver.find_element_by_xpath(Locators.report_menu).click()
        time.sleep(1)
        
    def archived_report_menu_click(self):
        self.driver.find_element_by_xpath(Locators.archived_menu).click()
        time.sleep(1)
        
    def appointment_report_run(self):
        self.driver.find_element_by_link_text(Locators.report_app_menu).click()
        time.sleep(1)
        
    def appointment_report_run_france(self):
        self.driver.find_element_by_link_text(Locators.report_france).click()
        time.sleep(1)
        
    def appointment_report_run_netherlands(self):
        self.driver.find_element_by_link_text(Locators.report_netherlands).click()
        time.sleep(1)
        
    def appointment_report_run_poland(self):
        self.driver.find_element_by_link_text(Locators.report_poland).click()
        time.sleep(1)

    def badge_report_run(self):
        self.driver.find_element_by_link_text(Locators.badge_report).click()
        time.sleep(1)

    def alert_report_run(self):
        self.driver.find_element_by_link_text(Locators.alert_report).click()
        time.sleep(1)
        
      
    
    def report_parameters(self):
        self.driver.find_element_by_id(Locators.report_from_date).clear()
        date_picker = self.driver.find_element_by_id(Locators.report_from_date)
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", date_picker)
        act_dt = date.today() - timedelta(days=4)
        act_dt = act_dt.strftime("%d-%b-%Y")
        date_picker.send_keys(act_dt)
        time.sleep(3)
        self.driver.find_element_by_css_selector(Locators.rep_run_btn).click()
        time.sleep(3)
        
        
        
    #####################################################DASHBOARDS############################################
   
   
    def dashboard_appointments(self):
        driver = self.driver
        time.sleep(2)
        pyautogui.moveTo(400,383)
        time.sleep(2)
        #print(driver.find_element_by_css_selector("#ct-chartdefault > svg > g.ct-series.ct-series-c > line").value_of_css_property("color"))
        total = driver.find_element_by_xpath(Locators.tool_tip).text
        time.sleep(2)
        pyautogui.moveTo(400,390)#Badge created
        time.sleep(2)
        created = driver.find_element_by_xpath(Locators.tool_tip).text
        time.sleep(2)
        pyautogui.moveTo(400,400)#Check out
        time.sleep(2)
        #print(driver.find_element_by_css_selector("#ct-chartdefault > svg > g.ct-series.ct-series-c > line").value_of_css_property("color"))
        checkedout = driver.find_element_by_xpath(Locators.tool_tip).text
        time.sleep(2)
        leg1 = driver.find_element_by_xpath(Locators.legend_1).text
        leg2 = driver.find_element_by_xpath(Locators.legend_2).text
        leg3 = driver.find_element_by_xpath(Locators.legend_3).text
        print(leg1 + ":" + total)
        print(leg2 + ":" + created)
        print(leg3 + ":" + checkedout)
        time.sleep(2)
        
        
        ###############################################India Appointment page objects##############################
        
    def visitor_type(self):
        ele = self.driver.find_element_by_id(Locators.visitor_type)
        drp = Select(ele)
        drp.select_by_index(1)
        time.sleep(1)
        
    def visitor_type_ddt(self,vis_type): #ddt
        ele = self.driver.find_element_by_id(Locators.visitor_type)
        drp = Select(ele)
        drp.select_by_visible_text(vis_type)
        
    def vis_email(self):
        em = names.get_first_name() + names.get_last_name() + "@test.com"
        self.driver.find_element_by_id(Locators.visitor_email).send_keys(em)
        time.sleep(1)
        
    def vis_email_ddt(self,mail_id): #ddt
        self.driver.find_element_by_id(Locators.visitor_email).send_keys(mail_id)
        
    def vis_nationality(self):
        ele = self.driver.find_element_by_id(Locators.visitor_nationality)
        drp = Select(ele)
        drp.select_by_index(1)
        time.sleep(1)
        
    def vis_nation_ddt(self,nation):#ddt
        ele = self.driver.find_element_by_id(Locators.visitor_nationality)
        drp = Select(ele)
        drp.select_by_visible_text(nation)
    
    def vis_purpose(self):
        drp = self.driver.find_element_by_id(Locators.visitor_purpose)
        down = Select(drp)
        down.select_by_index(1)
        time.sleep(1)
        
    def vis_purpose_ddt(self,purpose):
        drp = self.driver.find_element_by_id(Locators.visitor_purpose)
        down = Select(drp)
        down.select_by_visible_text(purpose)
        
    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        
    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
        time.sleep(1)
        
    def file_upload_india(self):
        autoit.win_active("Open") 
        autoit.control_set_text("Open","Edit1",r"C:\selenium_scripts\upload\AppointmentUpload_IND.xlsx")
        autoit.control_send("Open","Edit1","{ENTER}")
        time.sleep(2)
        
        
    ##translate##
    
    def language_translate(self):
        ele = self.driver.find_element_by_id("DropDownProductList")
        drp = Select(ele)
        drp.select_by_value("0")
        time.sleep(1)
        
    
    def links_images(self, tag , att): # img -->tag , src -->attribute :: a-->tag , href-->attribute
        tags = self.driver.find_elements_by_tag_name(tag)
        for i in tags:
            print(i.get_attribute(att))
        
    
        
        
        
        
    
        
        
    
        
        

        
        
        
        
        
    
    #===========================================================================
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