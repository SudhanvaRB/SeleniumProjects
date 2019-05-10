'''
Created on Jan 11, 2019

@author: subharad

pytest format
'''
from selenium import webdriver
import pytest
import time
from test_methods import TeamxLogin # added in window-->preference-->python int-->forced builtins

from teamx_locators import TeamxLocators

class TestTeamx():
    
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome("C:/selenium_scripts/Selenium/driver/chromedriver.exe")
        driver.maximize_window()
        yield
        time.sleep(2)
        driver.close()
        driver.quit()
        
    def test_login(self,test_setup):
        log = TeamxLogin(driver)
        log.login()
        print(driver.title)
        wel = driver.find_element_by_xpath(TeamxLocators.welcome_msg)
        print(wel.text)
        
    def test_publish(self,test_setup):# submits an idea and checks weather idea is submitted successfully and reflecting in My Ideas
        log = TeamxLogin(driver)
        log.login_employee()
        log.publish()
        log.iuc()
        log.inn_unit_name()
        log.inn_champ()
        #log.idea_theme_input()
        log.idea_name_enter()
        log.scroll_down()
        log.idea_desc_enter()
        log.submit_button()
        log.success_msg()
        log.ok_button()
        log.scroll_to_myidea()
        log.my_ideas()
        log.get_idea_name()
        log.get_idea_details()
        log.assert_idea_name()
        
    def test_recommend(self,test_setup):
        recom = TeamxLogin(driver)
        recom.login_innovation_champion()
        recom.welcome_message()
        recom.my_approvals()
        recom.scroll_to_ideawaiting_rec()
        recom.ideas_awaiting_recommendation()
        recom.action_button()
        recom.recommend_button()
        recom.scroll_down()
        
        recom.roi_calculator_link()
        recom.resource_matrix()
        recom.scroll_to_nonlabor()
        recom.non_labor_cost()
        recom.fin_details()
        recom.scroll_to_ROI()
        recom.calculate_button()
        recom.submit_recommendation()
        recom.iuh_drop_down()
        recom.send_for_funding()
        
    
    
        
    
        
        