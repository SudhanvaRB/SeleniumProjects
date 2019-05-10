'''
Created on Dec 4, 2018

Data Driven framework

Vims Appointment creation

Covers all countries but India

@author: subharad
'''
from DataDriven import xlutil
#import openpyxl
from selenium import webdriver
from test_locators import Locators
import time
from selenium.common.exceptions import NoSuchElementException,UnexpectedAlertPresentException,ElementNotVisibleException
from test_homepage import homepage
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#import pyautogui
#from DataDriven.ddtmozilla import capabilities_argument

'''

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities #firefox
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary #firfox

#for firefox
binary = FirefoxBinary("C:\\Users\\subharad\\AppData\\Local\\Mozilla Firefox\\firefox.exe")
capabilities_argument = DesiredCapabilities().FIREFOX
capabilities_argument["marionette"] = True
driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities_argument,executable_path="C:\\selenium_scripts\\Selenium\\driver\\geckodriver.exe")



cap = DesiredCapabilities().INTERNETEXPLORER
cap['ignoreProtectedModeSettings'] = True
cap['IntroduceInstabilityByIgnoringProtectedModeSettings'] = True
cap['nativeEvents'] = True
cap['ignoreZoomSetting'] = True
cap['requireWindowFocus'] = True
cap['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True
driver = webdriver.Ie(capabilities = cap,executable_path="C:\selenium_scripts\Selenium\driver\IEDriverServer.exe")

'''

driver = webdriver.Chrome("C:\selenium_scripts\Selenium\driver\chromedriver.exe")
#driver.implicitly_wait(10)
driver.maximize_window()


path = "C:/selenium_scripts/upload/DDT.xlsx"


data_row_count  = xlutil.getRowCount(path, 'Inputs')
data_col_count  = xlutil.getColCount(path, 'Inputs')

        
for r in range(2,data_row_count+1):
    username = xlutil.readData(path,"Inputs",r,1)

    dateval  = xlutil.readData(path,"Inputs",r,2)
    visitor_name = xlutil.readData(path,"Inputs",r,3)

    visitor_org = xlutil.readData(path,"Inputs",r,4)
    visitor_phone = xlutil.readData(path,"Inputs",r,5)
    cities = xlutil.readData(path,"Inputs",r,6)
    end_date = xlutil.readData(path,"Inputs",r,7)
    appointment_type = xlutil.readData(path,"Inputs",r,8)
    
    driver.get("https://fanditcloudtest.in.capgemini.com/vms/login")
    
    if username is not None:
        driver.find_element_by_id(Locators.username_text_box).send_keys(username)
        driver.find_element_by_id(Locators.login_button).click()
        time.sleep(1)
 

        try:
        
            if driver.title:
                xlutil.writeData(path, 'Inputs', r,14, "Login success with login id :" + username)
                apt = homepage(driver)
                apt.click_appointment()
                apt.new_appointment()
                
                #######################multiple appointment######################
                if appointment_type == "Multiple":
                    apt.multiple_appointment()
                    if end_date is None:
                        pass
                    else:
                        apt.insert_enddate(end_date)
                    #print("input date is blank")
                  
                #######################multiple appointment######################
                
                if dateval is None:
                    pass
                
                    #print("input date is blank")
               
                elif type(dateval) == str:
                    print(dateval)
                    apt.date_string(dateval)
                    time.sleep(2)
                    dt1 = driver.find_element_by_id("txtStartDate")
                    xlutil.writeData(path, 'Inputs', r,9, dt1.text)
                    time.sleep(1)
                
                else:
                    apt.insert_date(dateval)    
                
           
           
                if visitor_name is None:
                    pass
                  
                else:
                    apt.enter_vis_name(visitor_name)
                
                if visitor_org is None:
                    pass
                 
                else:
                    apt.enter_vis_org(visitor_org)
                    
                if visitor_phone is None:
                    pass
                  
                else:
                    apt.enter_visphone(visitor_phone)

                #apt.location_dropdown()
                try:
                
                    if cities is None:
                        pass
                    else:
                        
                        apt.city_list(cities)
                        
                except NoSuchElementException:
                    
                    msg_city= "no such location for this login"
                    print(msg_city)
                    xlutil.writeData(path, 'Inputs', r,15, msg_city)
                    time.sleep(1) 
                    driver.find_element_by_xpath(Locators.logout_button).click()
                    continue

                apt.scroll_up()
                apt.save_button()
                time.sleep(4)
           
    
                try:
                    if driver.find_element_by_xpath(Locators.app_cpnfirm_head).is_displayed():
                        msg = driver.find_element_by_xpath(Locators.app_confirm_msg).text
                        apt.app_confirm_ok()
                        xlutil.writeData(path, 'Inputs', r,11, msg)
                        time.sleep(4)
                        str1 = xlutil.readData(path,"Inputs",r,11)
                        str1 = str1.split(":", 1)[1]
                        print(str1)
                        apt.search_record(str1)
                        time.sleep(1)
                        apt.click_check_menu()
                        apt.click_check_in()
                        try:
                            apt.language_translate()
                        except:
                            pass
                        apt.search_app_id(str1)
                        apt.click_app_id()
                        #driver.save_screenshot('C:/selenium_scripts/screenshots/check_in.png')
                        #apt.scroll_down()
                        
                        if cities == "New York-79 Fifth Ave":
                            edited = " - ".join([a.strip() for a in cities.split("-")])
                            print(edited)
                            cities = edited
                            
                        apt.check_in_location_dropdown(cities)   
                        apt.scroll_down()                    
                        apt.click_check_box()
                        apt.rules_ok_button()
                        apt.confirm_cancel()
                        apt.search_app_id(str1)
                        apt.window_handles()
                        xlutil.writeData(path, 'Inputs', r,16, "check in successful")
                        try:
                            apt.language_translate()
                        except:
                            pass
                        apt.click_check_out()
                        apt.search_check_out(str1)
                        apt.click_check_out_image()
                        apt.reprint_content_print()
                        apt.reprint_dropdown()
                        apt.remark_dropdown()
                        apt.checkedout_button_click()
                        xlutil.writeData(path, 'Inputs', r,17, "check out successful")

                        #apt.click_confirm_check()
                        driver.find_element_by_xpath(Locators.logout_button).click()
 
                    else : 
                        obj = driver.switch_to.active_element.text
                        #obj = driver.switch_to_active_element().text
                        apt.app_exists_ok()
                        xlutil.writeData(path, 'Inputs', r,11, obj)
                        time.sleep(2)
                        driver.find_element_by_xpath(Locators.logout_button).click()
                        
                except UnexpectedAlertPresentException:
                    txt = driver.switch_to_alert().text
                    xlutil.writeData(path, 'Inputs', r,9, txt)
                    time.sleep(1)
                    driver.switch_to_alert().accept()
    
                        
                except ElementNotVisibleException:
                    dt = driver.find_element_by_id("lblStartDate")
                    print(dt.text)
                    xlutil.writeData(path, 'Inputs', r,9, dt.text)
                    time.sleep(1)
                    
                    dt = driver.find_element_by_id("lblEndDate")
                    print(dt.text)
                    xlutil.writeData(path, 'Inputs', r,18, dt.text)
                    time.sleep(1)
                    
                    org_name= driver.find_element_by_id("lblVisitorOrg")
                    xlutil.writeData(path, 'Inputs', r,10, org_name.text)
                    time.sleep(1)
                    
                    mob_no = driver.find_element_by_id("lblMob")
                    xlutil.writeData(path, 'Inputs', r,13, mob_no.text)
                    time.sleep(1)
                    
                    city = driver.find_element_by_id("lblLocation")
                    xlutil.writeData(path, 'Inputs', r,15, city.text)
                    time.sleep(1) 
                    
                    
                    msss = driver.find_element_by_id("lblVisitorName")
                    print(msss.text)
                    xlutil.writeData(path, 'Inputs', r,12, msss.text)
                    time.sleep(1)
                    driver.find_element_by_xpath(Locators.logout_button).click()
                    print("entered except block")

        except UnexpectedAlertPresentException:
            driver.switch_to_alert().accept()
            xlutil.writeData(path, 'Inputs', r,14, "Invalid login id :" + username)
            
        
        except NoSuchElementException:
            msg_city= "this role has no access for CheckIn and Check out or appointment is future dated"
            print(msg_city)
            xlutil.writeData(path, 'Inputs', r,16, msg_city)
            time.sleep(1) 
            driver.find_element_by_xpath(Locators.logout_button).click()
       
            
                    
    else:
        driver.find_element_by_id(Locators.login_button).click()
        driver.switch_to_alert().accept()
        xlutil.writeData(path, 'Inputs', r, 14, "Login id is blank" )
 
time.sleep(2)       
driver.close()    
driver.quit()   
                    


