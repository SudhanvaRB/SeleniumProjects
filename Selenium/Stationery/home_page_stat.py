'''
Created on Apr 29, 2019

@author: subharad

*** Stationery Application Home Page Class
'''
import time
from selenium.webdriver.support.select import Select
#from selenium.webdriver.common.action_chains import ActionChains
from Stationery.locators_stat import LocatorsStat as L


class HomePageStat():
    
    def __init__(self,driver):
        self.driver = driver
        
    def project_selection(self):
        #self.driver.find_element_by_id("PROJECT_ID").click()
        time.sleep(1)
        Select(self.driver.find_element_by_id(L.projectid)).select_by_index("1") # to select dropdown
        time.sleep(1)
    
    def location_selection(self):
        Select(self.driver.find_element_by_id(L.loc_drpdwn)).select_by_index("8") # to select location
        time.sleep(1)
        
 
    def scroll_to_item(self):
        driver = self.driver
        
        
        elementToFocus = driver.find_element_by_xpath(L.scrblngpad)
        driver.execute_script("arguments[0].scrollIntoView();", elementToFocus)
        time.sleep(2)
        driver.find_element_by_id(L.add).click()
        time.sleep(3)
        #driver.switch_to.frame('products')
        
    def scroll_to_update_item(self):
        driver = self.driver

        elementToFocus = driver.find_element_by_xpath(L.scrblngpad8)
        driver.execute_script("arguments[0].scrollIntoView();", elementToFocus)
        driver.find_element_by_id(L.add1).click()
        time.sleep(2)
        driver.find_element_by_id(L.cart).click()
        time.sleep(1)
        driver.find_element_by_id(L.save).click()
        time.sleep(1)
        print(self.driver.find_element_by_id(L.dialog123).text)
        self.driver.find_element_by_xpath(L.Ok_btn).click()
        time.sleep(2)   
        
        '''
        ele = driver.find_elements_by_xpath("//div[@id='jqgh_producttable_rn']")
        
        for l in ele :
            driver.execute_script("arguments[0].scrollIntoView();", l )
      
        ele1 = driver.find_element_by_xpath("//*[text()='BINDER CLIP - 51MM']")
        ele = driver.find_element_by_xpath("//img[@src='http://10.100.245.83:8080/stationery/images/custom/AddtoCart.png']")
        actions = ActionChains(driver)
        actions.move_to_elemetn(ele1).move_to_element(ele).click(ele).perform()
        #self.driver.execute_script("arguments[0].scrollIntoView()", ele)
        '''
       
        
        
    def submit_button(self):
        self.driver.find_element_by_id(L.submitbtn).click() # to Add product everytime need to update numeric values available 
        time.sleep(2)
        
    def success_message(self):
        time.sleep(2)
        print(self.driver.find_element_by_xpath(L.successmsg).text)
        print(self.driver.find_element_by_id(L.dialog123).text)
        self.driver.find_element_by_xpath(L.Ok_btn).click()     
        
    def cancel_cart(self):  
        self.driver.find_element_by_id(L.cancelcart).click()
        time.sleep(3)
        print(self.driver.find_element_by_id(L.dalogconfrm).text)
        self.driver.find_element_by_id(L.cancel).click()
        time.sleep(3)
        print(self.driver.find_element_by_id(L.dialog123).text)
        self.driver.find_element_by_xpath(L.Ok_btn).click()
        time.sleep(3)
        
    def add_more_products(self):
        driver = self.driver
        driver.find_element_by_id(L.add_more_products).click()
        time.sleep(2)
        
    def empty_cart_message(self):
        print(self.driver.find_element_by_id(L.dialog123).text)
        self.driver.find_element_by_xpath(L.Ok_btn).click()
        time.sleep(2)
        
    def remove_link(self):
        #self.driver.find_element_by_xpath("add_to_cart").click()
        self.driver.find_element_by_xpath(L.rem_link).click()
        time.sleep(2)
        self.driver.find_element_by_id(L.cancel).click()
        print(self.driver.find_element_by_id(L.dialog123).text)
        time.sleep(2)
        self.driver.find_element_by_xpath(L.Ok_btn).click()
        time.sleep(1)
        
    def my_cart_link(self):
        self.driver.find_element_by_class_name(L.mycartlink).click()
        time.sleep(2)
    
    def empty_cart_button(self):
        self.driver.find_element_by_id(L.mycartemptybtn).click()
        time.sleep(2)
        print(self.driver.find_element_by_id(L.emptydialog).text)
        self.driver.find_element_by_id(L.cancelok).click()
        time.sleep(2)
        print(self.driver.find_element_by_id(L.dialog123).text)
        self.driver.find_element_by_xpath(L.Ok_btn).click()
        time.sleep(1)
        print(self.driver.find_element_by_id(L.productinfo).text)
        
    def product_list(self):
        
        driver = self.driver
        ro = driver.find_elements_by_xpath("//*[@id='producttable']/tbody/tr")
        lenth = len(ro)
        print(lenth)
        co = driver.find_elements_by_xpath("//*[@id='producttable']/tbody/tr[1]/td")
        cols = len (co)
        print(cols)
        
  
        for r in range(1,lenth+1): #iterates over webtable and prints all values
            for c in range(1,cols+1):
                val = driver.find_element_by_xpath("//*[@id='producttable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
                val1 = driver.find_element_by_xpath("//*[@id='producttable']/tbody/tr["+str(r)+"]/td[3]").text
                try:
                    if int(val1) > 0:
                        print(val,end='            ')
                except ValueError:
                    pass

            
      
        '''   
        for r in range(1,lenth+1): #iterates over each row and print 2nd column values of each row
            
            val = driver.find_element_by_xpath("//*[@id='producttable']/tbody/tr["+str(r)+"]/td[3]").text
            try:
                if int(val) > 0:
                    print(int(val))
            except ValueError:
                pass
        '''

       

        
        
  
        


        