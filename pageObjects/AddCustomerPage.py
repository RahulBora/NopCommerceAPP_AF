import time
from selenium import webdriver as wb
from selenium.webdriver.support.select import Select


class AddCustomer():
    # Locating all the elements of the add customer page
    customersMenu_xpath= "//a[@href='#']//span[contains(text(),'Customers')]"
    customersMenuItem_xpath= "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    add_New_Btn_lnkText= "Add new"
    email_input_id= 'Email'
    password_input_id= "Password"
    firstname_input_id= "FirstName"
    lastname_input_id = "LastName"
    gender_male_id= "Gender_Male"
    gender_female_id = "Gender_Female"
    dob_id= "DateOfBirth"
    companyName_input_id ="Company"
    isTaxExempt_id= "IsTaxExempt"
    #newsletter_xpath= "//"
    customerRoles_xpath= "//*[@id='customer-info']/div[2]/div[1]/div[10]/div[2]/div/div[1]"
    customerRoleAdministrator_xpath= "//li[contains(text(),'Administrators')]"
    customerRoleRegistered_xpath = "//li[contains(text(),'Registered')]"
    customerRoleGuests_xpath = "//li[contains(text(),'Guests')]"
    customerRoleVendors_xpath = "//li[contains(text(),'Vendors')]"
    mgr_of_vendor_xpath= "//*[@id='VendorId']"
    adminComment_id= "AdminComment"
    saveBtn_xpath= "//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.customersMenu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.customersMenuItem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_link_text(self.add_New_Btn_lnkText).click()

    def setEmail(self,email):
        self.driver.find_element_by_id(self.email_input_id).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.password_input_id).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.customerRoles_xpath).click()
        time.sleep(3)

        if role== 'Registered':
            listItem= self.driver.find_element_by_xpath(self.customerRoleRegistered_xpath)

        elif role == 'Administrators':
            listItem = self.driver.find_element_by_xpath(self.customerRoleAdministrator_xpath)

        elif role== 'Guests':
            listItem= self.driver.find_element_by_xpath(self.customerRoleGuests_xpath)
            #Here user cana be eiter Guests or Registered, only one
            #so if registerd option is already there then we have to remove that role so that guest can be selected
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            listItem = self.driver.find_element_by_xpath(self.customerRoleGuests_xpath)

        elif role == 'Vendors':
            listItem = self.driver.find_element_by_xpath(self.customerRoleVendors_xpath)

        else:
            listItem = self.driver.find_element_by_xpath(self.customerRoleGuests_xpath)

        #listItem.click()
        self.driver.execute_script("arguments[0].click();",listItem)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element_by_xpath(self.mgr_of_vendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender=="Male":
            self.driver.find_element_by_id(self.gender_male_id).click()

        elif gender=="Female":
            self.driver.find_element_by_id(self.gender_female_id).click()

        else:
            self.driver.find_element_by_id(self.gender_male_id).click()

    def setFirstName(self,fname):
            self.driver.find_element_by_id(self.firstname_input_id).send_keys(fname)

    def setLastName(self,lname):
            self.driver.find_element_by_id(self.lastname_input_id).send_keys(lname)

    def setDOB(self,dob):
            self.driver.find_element_by_id(self.dob_id).send_keys(dob)

    def setCompanyName(self,comp_name):
            self.driver.find_element_by_id(self.companyName_input_id).send_keys(comp_name)

    def setAdminComment(self,content):
            self.driver.find_element_by_id(self.adminComment_id).send_keys(content)

    def clickOnSave(self):
            self.driver.find_element_by_xpath(self.saveBtn_xpath).click()






