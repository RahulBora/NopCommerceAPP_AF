import pytest

from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.AddCustomerPage import AddCustomer
import time

class Test_004_SearchCustomer:
    baseUrl= ReadConfig.getApplicationUrl()
    username= ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger= LogGen.log_gen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("********** Search Customer By Email 004 **********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("********* Login SuccessFul *********")

        self.logger.info("********** Starting search by Customer email *********")

        self.addCust= AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        time.sleep(3)
        self.addCust.clickOnCustomerMenuItem()

        self.searchCust= SearchCustomer(self.driver)
        self.searchCust.setEmail("victoria_victoria@nopCommerce.com")
        self.searchCust.clickSearch()
        time.sleep(10)

        status= self.searchCust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")

        assert True == status
        self.logger.info("************* TC_ Search Customer by Email_004 Finished *************")
        self.driver.close()


    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("********** Search Customer By Email 004 **********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("********* Login SuccessFul *********")

        self.logger.info("********** Starting search by Customer FirstName *********")

        self.addCust= AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        time.sleep(3)
        self.addCust.clickOnCustomerMenuItem()

        self.searchCust= SearchCustomer(self.driver)
        self.searchCust.setFirstname("Brenda")
        self.searchCust.clickSearch()
        time.sleep(10)

        status= self.searchCust.searchCustomerByName("Brenda")

        assert True == status
        self.logger.info("************* TC_ Search Customer by Email_004 Finished *************")
        self.driver.close()
