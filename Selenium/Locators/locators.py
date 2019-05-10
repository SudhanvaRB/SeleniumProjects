'''
Created on Oct 12, 2018

@author: subharad
'''
class Locators():
    
    #login page objects
    username_text_box = "UserId"
    login_button = "btnSubmit"
    
    #Home page objects
    logout_button = "//*[@id='lnkLogout']"
    appointment   = " //*[@id='liAppointment']/a/span"
    appointment_1 = "//*[@id='page-wrapper']/div[2]/div/div[2]/div/div[1]/div/a/button"
    #graph_color = "/html"
    
    #Appointment page objects
    date = "//*[@id='txtStartDate']"
    location ="//*[@id='ddlLocation']"
    visitor_name="//*[@id='txtVisitor']"
    visitor_organization = "//*[@id='txtVisitorOrg']"
    visitor_mobile_no = "//*[@id='txtMobNo']"
    save_btn ="//*[@id='savebut']"
    start_date_error="//*[@id='lblStartDate']"
    phone_error="//*[@id='lblMob']"
    character_error="//*[@id='lblVisitorOrg']"
    cancel_btn ="//*[@id='cancel']"
    title_image="//*[@id='page-wrapper']/div[1]/nav/div[1]/div/div[1]/img"
    search_box = "//*[@id='AptTable_filter']/label/input"
    appointment_visitor="//*[@id='page-wrapper']/div[2]/div/div[1]/ol/li[2]/strong"
    Appointment_Visitor = "//*[@id='page-wrapper']/div[2]/div/div[1]/ol/li[1]/a"
   
    