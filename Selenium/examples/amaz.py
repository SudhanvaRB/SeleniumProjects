from selenium import webdriver
import time

driver = webdriver.Chrome("C:/selenium_scripts/Selenium/driver/chromedriver.exe")
#driver.get("https://www.amazon.in")
#driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
driver.get("https://passport.beqom.com/capgeminitest")
#driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(3)
driver.switch_to.active_element
driver.find_element_by_id("ext-gen1010").click()

time.sleep(10)


################################

#driver.find_element_by_xpath("//*[text()='Hello, Sign in']").click()
#driver.find_element_by_xpath("//*[contains(text(),'Hello')]").click()
#driver.find_element_by_xpath("//*[starts-with(text(),'Hello')]").click()

###############

#driver.find_element_by_class_name("nav-line-1").click()
#river.find_element_by_id("nav-link-yourAccount").click()
time.sleep(2)
#driver.find_element_by_xpath("//*[text()='Sign in']")




'''
driver.find_element_by_id("ap_email").send_keys("9980906380")
driver.find_element_by_id("continue").click()
driver.find_element_by_id("ap_password").send_keys("Amazon90")
driver.find_element_by_id("signInSubmit").click()
'''

#driver.find_element_by_css_selector("#user-message").send_keys("hello")
#driver.find_element_by_css_selector(".form-control").send_keys("hello sudhanva")
#driver.find_element_by_css_selector("input").send_keys("hello sudhanva")


###################################
time.sleep(2)

driver.close()
driver.quit()