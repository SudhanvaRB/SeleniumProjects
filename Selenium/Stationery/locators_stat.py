'''
Created on Apr 29, 2019

@author: subharad

*** Stationery Application locators
'''
class LocatorsStat():
    #login page locators
    url = "http://10.100.245.83:8080/stationery/Login.htm"
    loginid = "loginId"
    pwd = "password"
    loginbutton = "//*[@id='login']/table/tbody/tr[4]/td/input"
    logoutbtn = "LogOut"
    
    #Home page locators
    projectid = "PROJECT_ID"
    loc_drpdwn = "location"
    scrblngpad = "//*[text()='SCRIBBLING PADS (1/4) SIZE']"
    scrblngpad8 = "//*[text()='SCRIBBLING PADS (1/8) FULL SIZE']"
    add = "actionbutton_116"
    add1 = "actionbutton_118"
    cart = "id_GoToMyCart"
    save = "id_SaveChanges"
    dialog123 = "dialog123"
    Ok_btn = "//*[text()='Ok']"
    submitbtn = "id_CollectStationery"
    successmsg = "//*[text()='Success']"
    cancelcart = "id_CancelMyCart"
    dalogconfrm = "dialogConfirm"
    cancel = "cancel_ok"
    add_more_products = "id_AddMoreProducts"
    rem_link = "//*[@id='116']/td[9]/a/img"
    mycartlink = "handcursor"
    mycartemptybtn = "myCartButtonEmpty"
    emptydialog = "dialogEmptyConfirm"
    cancelok = "cancel_ok1"
    productinfo = "productcart_info"
