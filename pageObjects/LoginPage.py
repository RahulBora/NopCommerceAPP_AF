from selenium import webdriver

class LoginPage:
    #LOGIN Page Elements
    Email_textbox_id="Email"
    Password_textbox_id="Password"
    Login_button_xpath="//div/input[contains(@class, 'login-button')]"
    Logout_linkText="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,username) :
        self.driver.find_element_by_id(self.Email_textbox_id).clear()
        self.driver.find_element_by_id(self.Email_textbox_id).send_keys(username)

    def setPassword(self,password) :
        self.driver.find_element_by_id(self.Password_textbox_id).clear()
        self.driver.find_element_by_id(self.Password_textbox_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.Login_button_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.Logout_linkText).click()