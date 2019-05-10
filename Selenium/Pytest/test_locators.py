'''
Created on Nov 14, 2018

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
    welcome_user  = "//*[@id='side-menu']/li[1]/div[1]"
    delete_button = "//*[@id='delP']/i"
    edit_button   = "//*[@id='btnEdit']/i"
    

    
    
    #Appointment page objects
    mul = "EndDate"
    end_date = "txtEnddate"
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
    srch_box_input = "//*[@id='AptTable']/tbody/tr[1]/td[2]"
    srch_no_record = "//*[@id='AptTable']/tbody/tr/td"
    appointment_visitor="//*[@id='page-wrapper']/div[2]/div/div[1]/ol/li[2]/strong"
    Appointment_Visitor = "//*[@id='page-wrapper']/div[2]/div/div[1]/ol/li[1]/a"
    app_cpnfirm_head = "//*[@id='myModal6']/div/div/div[1]/h4"
    app_confirm_msg = "//*[@id='myModal6']/div/div/div[2]/p[1]"
    app_confirm_ok_btn = "//*[@id='myModal6']/div/div/div[3]/div/button" 
    app_exists_ok_btn  = "//*[@id='myModal8']/div/div/div[3]/div/button"
    update_button   = "//*[@id='savebut']"
    show_entries_drpdown = "//*[@id='AptTable_length']/label/select"
    show_entries_count   ="//*[@id='AptTable_info']"
    show_next ="//*[@id='AptTable_next']/a"
    show_previous = "//*[@id='AptTable_previous']/a"
    
    #Check menu objects
    check_menu = "//*[@id='liCheckInOut']/a/span[1]"
    check_in = "//*[@id='liVisitorCheckIn']/a"
    
    check_out = "//*[@text()=' Check Out']"  #link_text and utf-8 encoding save
    check_out_france = "→ vérifier"
    check_out_poland = "→ Wymeldować się"
    check_out_netherlands = "→ Uitchecken"
    
  
    bulk_appointment = "//*[@id='liBulkAppointment']/a/span"
    bulk_check_out ="→ Bulk Check Out"
    bulk_france = "→ Vente en gros"
    bulk_poland = "→ Zbiorcze wyrejestrowanie"
    bulk_netherlands = "→ Bulk uitchecken"
    
    
    #Check In page objects
    appointment_id ="//*[@id='DataTables_Table_0']/tbody/tr[1]/td[2]/a"
   
    location_check = "//*[@id='Location']"
    check_box = "checkmark"
    confirm_check_button ="btnConfirm"
    cancel_check_button = "/html/body/div[1]/div[3]/div/div/div[1]/div/div[4]/button[2]"
    rules_ok_button = "//*[@id='myModal35']/div[2]/div/div[3]/div/button"
    rules_body ="//*[@id='myModal35']/div[2]/div/div[2]/p"
    rules_head = "//*[@id='myModal35']/div[2]/div/div[1]/h4"
    check_in_print_badge ="//*[@id='DataTables_Table_0']/tbody/tr[1]/td[9]/a/img"
    search_checkin = "//*[@id='DataTables_Table_0_filter']/label/input"
    confirm_message = "//*[@id='Confirmationmodal1']/div[2]/div/div[2]/p"
   
    ok_button = "//*[@id='Confirmationmodal1']/div[2]/div/div[3]/div/button"
    link_check_in = "//*[@id='DataTables_Table_0']/tbody/tr/td[2]/a"
    
    
    #Check Out page objects
    check_out_image = "//*[@id='CheckOutTbl']/tbody/tr[1]/td[7]/p/img"
    reprint_badge_drop_down = "ddlAction"
    reprint_badge_head = "//*[@id='CheckoutEdit']/div[3]/h4/label[2]"
    reprint_badge_body = "//*[@id='CheckoutEdit']/table/tbody/tr[1]/td[1]"
    remarks_drop_down = "selectedRemark"
    reprint_submit_button = "//*[@id='btnSubmit']/label"
    checkedout_button ="//*[@id='btnCheckout']/label"
    check_out_search = "//*[@id='CheckOutTbl_filter']/label/input"
    click_checkout_img ="//*[@id='CheckOutTbl']/tbody/tr/td[7]/p/img"
    
    badge_number = "//*[@id='CheckoutEdit']/table/tbody/tr[1]/td[1]/label"
    badge_number_value ="//*[@id='CheckoutEdit']/table/tbody/tr[1]/td[2]"
    badge_date = "//*[@id='CheckoutEdit']/table/tbody/tr[2]/td[1]/label"
    badge_date_value = "//*[@id='CheckoutEdit']/table/tbody/tr[2]/td[2]"
    visitor_name_head = "//*[@id='CheckoutEdit']/table/tbody/tr[3]/td[1]/label"
    visitor_name_value = "//*[@id='CheckoutEdit']/table/tbody/tr[3]/td[2]"
    visitor_org_head = "//*[@id='CheckoutEdit']/table/tbody/tr[4]/td[1]/label[2]"
    visitor_org_value = "//*[@id='CheckoutEdit']/table/tbody/tr[4]/td[2]"
    host_name_head = "//*[@id='CheckoutEdit']/table/tbody/tr[5]/td[1]/label"
    host_name_value="//*[@id='CheckoutEdit']/table/tbody/tr[5]/td[2]"
    
    
    #Bulk check out
    
    bulk_check_out_btn = "btnCheckOut"
    bulk_check_box = "chkBoxAll"
    #//*[@id="dynamicModal"]/div/div/div[1]/h4
    bulk_check_out_modal_content ="modal-content"
    bulk_check_out_close = "//*[@id='dynamicModal']/div/div/div[3]/span"
    bulk_check_single = "input.chkBoxActual[name='SelectedCheckRecord']"  #css selector , combination of Tag, class and attribute
    #Bulk appointment 
    browse_file ="buttonText" #class name
    upload_submit_button ="BtnSubmit"
    table_error ="TBLErrorSummary"
    error_cancel = "//*[@id='myModal78']/div/div/div[1]/button/span[1]"
    bulk_table_summary ="TblSummaryDetailsBulkAppointment"
    discrepancy_title="//*[@id='myModal78']/div/div/div[1]/h4"
    click_here_link = "//*[@id='DivBulkAppoitmentSummary']/div[2]/p/a"
    no_records_for_bulk_check_out = "//*[@id='divBulkAccessRight']/div"
    
    #Reports
    report_app_menu ="→ Appointment Report"
    report_menu ="//*[@id='liReport']/a/span[1]"
    archived_menu = "//*[@id='liArchReport']/a/span[1]"
    rep_run_btn = "button[type='submit']"   #css selector tag(button) and attribute(submit)
    badge_report = "→ Badge Report"
    alert_report = "→ Alert Report"
    report_from_date="txtStartDateFF"
    report_france = "→ Rapport de rendez-vous"
    report_poland = "→ Raport o powołaniu"
    report_netherlands = "→ Afspraak rapport"
    
    #Dashboards
    
    tool_tip = "//*[@id='ct-chartdefault']/div"
    legend_1 = "//*[@id='tabCity']/div/div/div[2]/div[2]/div[1]/div[2]"
    legend_2 = "//*[@id='tabCity']/div/div/div[2]/div[2]/div[2]/div[2]"
    legend_3 = "//*[@id='tabCity']/div/div/div[2]/div[2]/div[3]/div[2]"
    
    
    #India appointment page locators
    visitor_type = "ddlVisitortype"
    visitor_email = "txtEmail"
    visitor_nationality = "ddlNationality"
    visitor_purpose = "ddlPurpose"
    
    