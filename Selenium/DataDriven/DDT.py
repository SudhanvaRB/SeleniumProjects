from DataDriven import xlutil
#import openpyxl
from selenium import webdriver
from test_locators import Locators
import time
from selenium.common.exceptions import NoSuchElementException,UnexpectedAlertPresentException,ElementNotVisibleException
from test_homepage import homepage

driver = webdriver.Chrome("C:\selenium_scripts\Selenium\driver\chromedriver.exe")
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
    
    driver.get("http://10.100.245.80:92/VMS/login")
    
    if username is not None:
        driver.find_element_by_id(Locators.username_text_box).send_keys(username)
        driver.find_element_by_id(Locators.login_button).click()
        time.sleep(1)
 

        try:
        
            if driver.title:
                xlutil.writeData(path, 'Inputs', r,6, "Login success with login id :" + username)
                apt = homepage(driver)
                apt.click_appointment()
                apt.new_appointment()
                
                if dateval is None:
                    pass
                    #print("input date is blank")
                elif type(dateval) == str:
                    print(dateval)
                    apt.date_string(dateval)
                    time.sleep(2)
                    dt1 = driver.find_element_by_id("txtStartDate")
                    xlutil.writeData(path, 'Inputs', r,7, dt1.text)
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
                
                apt.location_dropdown()
                apt.save_button()
                time.sleep(4)
           
    
                try:
                    if driver.find_element_by_xpath(Locators.app_cpnfirm_head).is_displayed():
                        msg = driver.find_element_by_xpath(Locators.app_confirm_msg).text
                        apt.app_confirm_ok()
                        xlutil.writeData(path, 'Inputs', r,9, msg)
                        time.sleep(3)
                        driver.find_element_by_xpath(Locators.logout_button).click()
 
                    else :
                        obj = driver.switch_to_active_element().text
                        apt.app_exists_ok()
                        xlutil.writeData(path, 'Inputs', r,9, obj)
                        time.sleep(2)
                        driver.find_element_by_xpath(Locators.logout_button).click()
                        
                except UnexpectedAlertPresentException:
                    txt = driver.switch_to_alert().text
                    xlutil.writeData(path, 'Inputs', r,7, txt)
                    time.sleep(1)
                    driver.switch_to_alert().accept()
    
                        
                except ElementNotVisibleException:
                    dt = driver.find_element_by_id("lblStartDate")
                    print(dt.text)
                    xlutil.writeData(path, 'Inputs', r,7, dt.text)
                    time.sleep(1)
                    
                    org_name= driver.find_element_by_id("lblVisitorOrg")
                    xlutil.writeData(path, 'Inputs', r,8, org_name.text)
                    time.sleep(1)
                    
                    mob_no = driver.find_element_by_id("lblMob")
                    xlutil.writeData(path, 'Inputs', r,11, mob_no.text)
                    time.sleep(1)
                    
                    
                    msss = driver.find_element_by_id("lblVisitorName")
                    print(msss.text)
                    xlutil.writeData(path, 'Inputs', r,10, msss.text)
                    time.sleep(1)
                    driver.find_element_by_xpath(Locators.logout_button).click()
                    print("entered except block")

        except UnexpectedAlertPresentException:
            driver.switch_to_alert().accept()
            xlutil.writeData(path, 'Inputs', r, 6, "Invalid login id :" + username)
            

    else:
        driver.find_element_by_id(Locators.login_button).click()
        driver.switch_to_alert().accept()
        xlutil.writeData(path, 'Inputs', r, 6, "Login id is blank" )
 
time.sleep(2)       
driver.close()    
driver.quit()   
                    
                    

                 
                    
            
                
            
                
            
            
            
            
          
            
            
    
      
      
       
        
 
      
    
   
        
        
   
        
   
    
    


