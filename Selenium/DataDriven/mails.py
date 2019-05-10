from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\selenium_scripts\Selenium\driver\chromedriver.exe")
driver.maximize_window()

#driver.get("https://seleniumhq.github.io/selenium/docs/api/java/")
#driver.get("http://demo.automationtesting.in/Windows.html")
#driver.get("http://demo.automationtesting.in/WebTable.html")
driver.get("http://10.100.245.88:81/login")

#driver.find_element_by_css_selector("input#UserId").send_keys("tihollan")  #tag and id
#driver.find_element_by_css_selector("input[type='text']").send_keys("tihollan") # tag and attribute
#driver.find_element_by_css_selector("input#UserId[type='text']").send_keys("tihollan") #tag, id and attribute

#driver.find_element_by_xpath("//*[@name='UserId']").send_keys("tihollan") 

#driver.find_element_by_css_selector("input#btnSubmit").click() #tag and and id
#driver.find_element_by_css_selector("input.Button").click() # tag and class name
#driver.find_element_by_css_selector("input.Button[type='submit']").click() # tag,class name and attribute
#driver.find_element_by_css_selector("input.Button[value='Login']").click() # tag,class name and attribute

'''
tag = driver.find_elements_by_tag_name("a")
for i in tag:
    print(i.get_attribute("href"))
'''

'''
driver.switch_to.frame("packageListFrame") 
driver.find_element_by_xpath("//*[text()='com.thoughtworks.selenium']").click()  
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame("packageFrame")
hd_txt=driver.find_element_by_class_name("bar")
print(hd_txt.text)
driver.find_element_by_xpath("//*[text()='BrowserConfigurationOptions']").click()
time.sleep(2)

'''
'''
action_chain = ActionChains(driver)
ele = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a")
action_chain.move_to_element(ele).click().perform()

#driver.find_element_by_xpath("//a[@href='http://demo.automationtesting.in/Windows.html#Seperate']").click()
bfr_wnd_title = driver.title
print(bfr_wnd_title)
before_window = driver.window_handles[0]

driver.find_element_by_xpath("//*[text()='click']").click()
time.sleep(3)

current_window = driver.window_handles[1]
driver.switch_to.window(current_window)
crt_win_title = driver.title
print(crt_win_title)
if crt_win_title != bfr_wnd_title:
    print("window switched")
driver.switch_to.window(before_window)
print(driver.title)
time.sleep(3)
'''
'''
time.sleep(3)
ac = ActionChains(driver)
dc = driver.find_element_by_xpath("//*[@id='1550037386061-0-uiGrid-000B-cell']/user-click-select/div[1]/button/i")
ac.double_click(dc).perform()
time.sleep(2)
'''
driver.find_element_by_id("UserId").send_keys("tihollan")
driver.find_element_by_id("btnSubmit").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='liCheckInOut']/a/span[1]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='liVisitorCheckOut']").click()
time.sleep(2)
print("success")



driver.close()
driver.quit()
        




