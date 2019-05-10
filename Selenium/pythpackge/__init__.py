from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\selenium_scripts\Selenium\driver\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("http://10.100.245.80:92/VMS/login")
driver.find_element_by_name("UserId").send_keys("tihollan")
driver.find_element_by_name("btnSubmit").click()
time.sleep(4)
driver.quit()
