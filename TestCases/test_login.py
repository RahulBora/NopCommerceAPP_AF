import pytest
from selenium import webdriver as wb
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_Login_001:
    base_url= ReadConfig.getApplicationUrl()
    username= ReadConfig.getUsername()
    password= ReadConfig.getPassword()

    logger = LogGen.log_gen()

    @pytest.mark.regression
    def test_HomePage(self, setup):
        self.logger.info("****************Test_001_Login************")
        self.logger.info("*************** Verifying Home Page Title *************" )


        self.driver = setup
        self.driver.get(self.base_url)
        act_url = self.driver.title

        if act_url=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*************** Home Page Title is passed *************")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\"+"test_HomePage_Title.png")
            self.driver.close()
            self.logger.error("*************** Home Page Title is failed *************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*************** Verifying the Login test *************")
        self.driver = setup
        self.driver.get(self.base_url)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title=self.driver.title

        if act_title=='Dashboard / nopCommerce administration':
            assert True
            self.logger.info("*************** Login test is passed *************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_HomePage_Title_AfterLogout.png")
            self.driver.close()
            self.logger.error("*************** Login test is failed *************")
            assert False



