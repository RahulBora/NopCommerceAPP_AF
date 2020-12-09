from selenium import webdriver as wb
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = wb.Chrome()
        print("Launching chrome browser..........")
    elif browser == 'firefox':
        driver = wb.Firefox()
        print("Launching firefox browser..........")
    return driver

def pytest_addoption(parser):    #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  #This will return the browser value to setup method
    return request.config.getoption("--browser")

############# Pytest HTML Reports ###############

# It is hook for Adding Environment info to Html Report
def pytest_configure(config):
    config._metadata['Project Name'] = "NOP Commerce"
    config._metadata['Module name'] = "Customers"
    config._metadata['Tester'] = "Rahul"

############ It is hook for Delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Java_HOME", None)
    metadata.pop("Plugins", None)