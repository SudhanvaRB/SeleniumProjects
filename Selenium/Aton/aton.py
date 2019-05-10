'''
Created on May 6, 2019

@author: subharad
'''
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\selenium_scripts\Selenium\driver\chromedriver.exe")
driver.get("https://atonappstest.capgemini.com/aton/Login.htm")
#driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element_by_id("loginId").send_keys("bmidatan")
driver.find_element_by_id("passWordId").send_keys("123")
driver.find_element_by_name("login1").click()
time.sleep(2)
driver.find_element_by_id("ui-accordion-accordion-header-1").click()
time.sleep(2)
driver.find_element_by_id("39_href").click()
time.sleep(10)
driver.find_element_by_xpath("//*[@id='1']/i").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='2']/i").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='113']/i").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='114']/i").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='340']/i").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='341']/i").click()
time.sleep(1)
driver.find_element_by_id("351_anchor").click()
time.sleep(5)
driver.find_element_by_id("ui-id-2").click()
time.sleep(2)
driver.find_element_by_id("gotoSpaceOrg").click()
time.sleep(15)

#src = driver.find_element_by_id("114912_code")
driver.find_element_by_xpath("//span[text()='Select an Option']").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 60);")
ele = driver.find_element_by_id("seatCategory")
drp = Select(ele)
drp.select_by_visible_text("WorkStations ( 168 )")
time.sleep(2)
'''


#ele = driver.find_element_by_xpath("//span[contains(text(),'WorkStations')]")

ActionChains(driver).move_to_element(driver.find_element_by_id("267804")).perform()
ele = driver.find_element_by_id("267804").text

driver.find_element_by_xpath("//input[@type='text']").send_keys(ele)
time.sleep(2)
'''
'''
print(driver.execute_script("arguments[0].scrollIntoView()", ele).text)
time.sleep(2)
'''


'''
driver.find_element_by_id("notOrgCnt").click()
time.sleep(1)
src = driver.find_element_by_xpath("//*[@id='267809']/p[1]")
dest = driver.find_element_by_id("114770")
ActionChains(driver).click_and_hold(src).move_to_element(dest).release(dest).perform()
#driver.find_element_by_id("saveSeats").click()

#ActionChains(driver).drag_and_drop_by_offset(src, 356,308).perform()

#ActionChains(driver).click_and_hold(src).pause(5).release().pause(2).perform()


time.sleep(2)
'''




'''
driver.find_element_by_id("70_href").click()
time.sleep(10)
driver.find_element_by_xpath("//*[text()='SBU / BU']").click()
time.sleep(2)

ele = driver.find_element_by_id("cntryId")
drp = Select(ele)
drp.select_by_visible_text("UAE")
time.sleep(2)
driver.find_element_by_xpath("//*[text()='OK']").click()
time.sleep(2)
driver.find_element_by_id("mapSbuBu").click()
time.sleep(2)



ro = driver.find_elements_by_xpath("//*[@id='allSBUBUTable']/tbody/tr")
lenth = len(ro)
print(lenth)

co = driver.find_elements_by_xpath("//*[@id='allSBUBUTable']/tbody/tr[1]/td")
cols = len (co)
print(cols)

        


for r in range(1,lenth+1): #iterates over each row and print 2nd column values of each row
    val = driver.find_element_by_xpath("//*[@id='allSBUBUTable']/tbody/tr["+str(r)+"]/td[2]").text
    if val =="Capgemini Consulting":
        
        val1 = driver.find_element_by_xpath("//*[@id='allSBUBUTable']/tbody/tr["+str(r)+"]/td[3]").text
        if val1 == "Fahrenhiet 212":
            print(r)
            print(val)
            print(val1)
            xp ="//*[@id='allSBUBUTable']/tbody/tr["+str(r)+"]/td[1]/input"
            driver.find_element_by_xpath(xp).click()
            #//*[@id="allSBUBUTable"]/tbody/tr[6]/td[1]/input
            
        

time.sleep(2)

'''

driver.close()
driver.quit()
