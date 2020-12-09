import string
import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import random


class Test_003_AddCustomer:
    baseUrl= ReadConfig.getApplicationUrl()
    username= ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger= LogGen.log_gen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("********Test_003_AddCustomer")
        self.driver=setup
        self.driver.get(self.baseUrl)

        self.driver.maximize_window()

        self.lp= LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Successful **********")

        self.logger.info("********** Starting Add Customer Test **********")
        self.addCust= AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        time.sleep(3)
        self.addCust.clickOnCustomerMenuItem()
        self.addCust.clickOnAddNew()

        self.logger.info("********** Providing Customer Info **********")

        self.email= random_generator() + '@gmail.com'
        self.addCust.setEmail(self.email)
        self.addCust.setPassword('Test@123')
        self.addCust.setCustomerRoles('Guests')
        self.addCust.setManagerOfVendor("Vendor 2")
        self.addCust.setGender("Male")
        self.addCust.setFirstName("Rahul")
        self.addCust.setLastName("Singh")
        self.addCust.setDOB("11/09/1980")         #Format: 'DD/MM/YY'
        self.addCust.setCompanyName("QAautomation Testing Ltd.")
        self.addCust.setAdminComment("This content is added for testing purpose")

        self.addCust.clickOnSave()

        self.logger.info("*********** Saving Customer Information *************")

        self.logger.info("********************* Add customer Validation Started **************")

        self.msg=self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg :
            assert True == True
            self.logger.info("************ Add customer Test Passed *************")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_addCustomer_scr.png") #screenshot with path +name
            self.logger.info("************ Add customer Test Failed *************")
            assert True == False

        self.driver.close()
        self.logger.info("********* Test Add customer is done **********")


def random_generator():
    letters= string.ascii_lowercase[:12]
    return ''.join(random.choice(letters) for i in range(7))



