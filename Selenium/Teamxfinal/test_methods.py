'''
Created on Jan 11, 2019

@author: subharad
'''

from teamx_locators import TeamxLocators
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import names

class TeamxLogin():
    
    def __init__(self,driver):
        self.driver = driver
        
    def login_employee(self):
        driver = self.driver
        driver.get("https://teamxdev.fs.capgemini.com/TEAMx30/service/uatLogin")
        driver.find_element_by_id(TeamxLocators.user_id).send_keys("111980")
        driver.find_element_by_name(TeamxLocators.submit_button).click()
        
    def login_innovation_champion(self):
        driver = self.driver
        driver.get("https://teamxdev.fs.capgemini.com/TEAMx30/service/uatLogin")
        driver.find_element_by_id(TeamxLocators.user_id).send_keys("104164")
        driver.find_element_by_name(TeamxLocators.submit_button).click()
        
    def publish(self):
        driver = self.driver
        mainmenu = driver.find_element_by_link_text(TeamxLocators.main_menu)
        action=ActionChains(driver)
        action.move_to_element(mainmenu).perform()
        submenu = wait(driver, 10).until(EC.element_to_be_clickable((By.ID, TeamxLocators.sub_menu)))
        submenu.click()
        
    def welcome_message(self):
        wel = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]")
        print(wel.text)
        
    def iuc(self): # innovation unit category
        self.driver.find_element_by_id(TeamxLocators.innovation_unit_category).click()
        time.sleep(2)
        
    def inn_unit_name(self): 
        exp = self.driver.find_element_by_id(TeamxLocators.iun)
        drp = Select(exp)
        drp.select_by_visible_text("Centrica")
        time.sleep(2)
    
    def inn_champ(self):
        val = self.driver.find_element_by_id(TeamxLocators.inn_champ)
        drp = Select(val)
        drp.select_by_index(1)
        time.sleep(2)
     
    '''   
    def idea_theme_input(self):
        val = self.driver.find_element_by_id(TeamxLocators.idea_theme)
        drp = Select(val)
        drp.select_by_index(1)
        time.sleep(2)
    '''
        
    def idea_name_enter(self):
        global idea_name 
        idea_name = names.get_full_name()
        self.driver.find_element_by_id(TeamxLocators.idea_name).send_keys(idea_name)
        print(idea_name)
        time.sleep(2)
        
    def idea_desc_enter(self):
        self.driver.find_element_by_id(TeamxLocators.idea_desc).send_keys(names.get_full_name())
        self.driver.find_element_by_id(TeamxLocators.idea_desc).send_keys(names.get_full_name())
        time.sleep(2)
        
    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        
    def submit_button(self):
        self.driver.find_element_by_id(TeamxLocators.submit_btn).click()
        time.sleep(3)
        
    def success_msg(self):
        print(self.driver.find_element_by_id(TeamxLocators.success_text).text)
        time.sleep(1)
    
    def ok_button(self):
        self.driver.find_element_by_css_selector("button[type='button']").click()
        time.sleep(2)
        
    def my_approvals(self):
        #self.driver.find_element_by_link_text(TeamxLocators.my_queue)
        driver = self.driver
        mainmenu = driver.find_element_by_link_text(TeamxLocators.main_menu)
        action=ActionChains(driver)
        action.move_to_element(mainmenu).perform()
        submenu = wait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, TeamxLocators.my_queue)))
        submenu.click()
    
    def my_ideas(self):
        self.driver.find_element_by_xpath(TeamxLocators.img_scc_1).click()
        time.sleep(2)
        
    def ideas_awaiting_recommendation(self):
        self.driver.find_element_by_xpath(TeamxLocators.idea_waiting_rec).click()
        time.sleep(2)
        
    def scroll_to_ideawaiting_rec(self):
        ele = self.driver.find_element_by_xpath(TeamxLocators.idea_waiting_rec)
        self.driver.execute_script("arguments[0].scrollIntoView()", ele)
        time.sleep(2)
        
    def get_idea_name(self):
        global val
        val = self.driver.find_element_by_xpath("//*[@id='myIdeasList']/tbody/tr[1]/td[2]")
        print(val.text)
    
    def assert_idea_name(self):
        assert idea_name == val.text
        
    def scroll_to_myidea(self):
        ele = self.driver.find_element_by_xpath(TeamxLocators.img_scc_1)
        self.driver.execute_script("arguments[0].scrollIntoView()", ele)
        time.sleep(2)
        
    def action_button(self):
        self.driver.find_element_by_xpath(TeamxLocators.action_btn).click()
        time.sleep(2)
        
    def recommend_button(self):
        self.driver.find_element_by_id("recommend").click()
        time.sleep(2)
        
    def iuh_drop_down(self):
        ele = self.driver.find_element_by_id("SPONSOR")
        drp = Select(ele)
        drp.select_by_visible_text("Arun Varghese")
        time.sleep(2)
        
    def roi_calculator_link(self):
        self.driver.find_element_by_link_text("ROI Calculator").click()
        time.sleep(2)
        
    def resource_matrix(self):
        driver = self.driver
        driver.find_element_by_id("sseCount").send_keys("1")
        driver.find_element_by_id("acCount").send_keys("1")
        driver.find_element_by_id("sseCountManDays").send_keys("5")
        driver.find_element_by_id("acCountManDays").send_keys("8")
        driver.find_element_by_id("getTotalLabourCostButton").click()
        time.sleep(3)
        
    def non_labor_cost(self):
        driver = self.driver
        driver.find_element_by_id("hardwareCost").send_keys("20")
        driver.find_element_by_id("softwareCost").send_keys("100")
        time.sleep(2)
        
    
    def scroll_to_nonlabor(self):
        ele = self.driver.find_element_by_xpath(TeamxLocators.non_labor)
        self.driver.execute_script("arguments[0].scrollIntoView()", ele)
        time.sleep(2)
        
    
    def fin_details(self):
        self.driver.find_element_by_name("textbox").send_keys("lot of financial benefits")
        self.driver.find_element_by_name("textbox1").send_keys("850")
        time.sleep(1)
        
    def calculate_button(self):
        self.driver.find_element_by_id("CalculateValues").click()
        time.sleep(2)

      
    def scroll_to_ROI(self):
        ele = self.driver.find_element_by_xpath("//*[@id='logoutForm']/div/div[4]/div/table[4]/tbody/tr[1]/th")
        self.driver.execute_script("arguments[0].scrollIntoView()", ele)
        time.sleep(2)
        
    def submit_recommendation(self):
        self.driver.find_element_by_id("btnSubmit").click()
        time.sleep(4)
        
    def send_for_funding(self):
        self.driver.find_element_by_id("sendForFunding").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("button[type='button']").click()
        time.sleep(2)

        
    def get_idea_details(self):
        ro = self.driver.find_elements_by_xpath("//*[@id='myIdeasList']/tbody/tr")
        lenth = len(ro)
        print(lenth)
        co = self.driver.find_elements_by_xpath("//*[@id='myIdeasList']/tbody/tr[1]/td")
        cols = len (co)
        print(cols)
        
        for r in range(1,lenth+1): #iterates over webtable and prints all values
            for c in range(1,cols+1):
                if r <= 1:
                    val = self.driver.find_element_by_xpath("//*[@id='myIdeasList']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
                    print(val,end='           ')
            print()
        
        
        
        