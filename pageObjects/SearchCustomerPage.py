from selenium import webdriver as wb

class SearchCustomer():
    # Searching customer on Add customer Page
    email_id= "SearchEmail"
    firstname_id= "SearchFirstName"
    lastname_id= "SearchLastName"
    searchBtn_id= "search-customers"
    searchResultTable_xpath= "//table[@role=grid]"
    table_xpath= "//*[@id='customers-grid']"
    tableRows_xpath= "//*[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//*[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver= driver

    def setEmail(self,email):
        self.driver.find_element_by_id(self.email_id).clear()
        self.driver.find_element_by_id(self.email_id).send_keys(email)

    def setFirstname(self,fname):
        self.driver.find_element_by_id(self.firstname_id).clear()
        self.driver.find_element_by_id(self.firstname_id).send_keys(fname)

    def setLastname(self,lname):
        self.driver.find_element_by_id(self.lastname_id).clear()
        self.driver.find_element_by_id(self.lastname_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element_by_id(self.searchBtn_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag=False

        for r in range(1,self.getNoOfRows()+1):
            table= self.driver.find_element_by_xpath(self.table_xpath)
            emailId= table.find_element_by_xpath("//table[@id='customers-grid']//tbody/tr['+str(r)+']/td[2]").text

            if email == emailId:
                flag= True
                break
        return flag

    def searchCustomerByName(self,Name):
        flag=False

        for r in range(1,self.getNoOfRows()+1):
            table= self.driver.find_element_by_xpath(self.table_xpath)
            name= table.find_element_by_xpath("//table[@id='customers-grid']//tbody/tr['+str(r)+']/td[3]").text

            if Name in name:
                flag= True
                break
        return flag



