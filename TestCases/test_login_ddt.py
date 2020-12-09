import pytest
from selenium import webdriver as wb
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils
import time

class Test_Login_002_DDT:
    base_url= ReadConfig.getApplicationUrl()
    path= ".//TestData/LoginData.xlsx"
    username= ReadConfig.getUsername()
    password= ReadConfig.getPassword()

    logger = LogGen.log_gen()


    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("*************** Test_Login_002_DDT *************")
        self.logger.info("*************** Verifying the Login test *************")
        self.driver = setup
        self.driver.get(self.base_url)

        self.lp = LoginPage(self.driver)
        lst_status=[]

        rows=ExcelUtils.getRowCount(self.path, 'Sheet1')
        print('No. of rows in the Sheet1: ', rows)

        for r in range(2,rows+1):
            username = ExcelUtils.readData(self.path, "Sheet1", r, 1)
            password= ExcelUtils.readData(self.path, "Sheet1", r, 2)
            expected_result= ExcelUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setUsername(username)
            self.lp.setPassword(password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title

            if act_title=='Dashboard / nopCommerce administration':
                if expected_result=="Pass":
                    assert True
                    self.logger.info("*************** Login test is passed *************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif expected_result=="Fail":
                    self.logger.info("*************** Login test is failed *************")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
                elif act_title !='Dashboard / nopCommerce administration':
                    if expected_result== 'Pass':
                        self.logger.info("*************** Login test is failed *************")
                        lst_status.append("Fail")
                    elif expected_result == "Fail":
                        self.logger.info("*************** Login test is Passed} *************")
                        lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT is passsed............")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT is failed............")
            self.driver.close()
            assert False

        self.logger.info(" End of Login DDT test")
        self.logger.info(" Completed TC_LoginDDT_002")


