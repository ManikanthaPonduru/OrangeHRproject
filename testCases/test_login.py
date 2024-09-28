import pytest
import time
from Utilities.readProperties import ReadConfig
from pageObjects.LoginPage_PageObjects import OrangeHrm
from Utilities.customLogger import LogGen


# @pytest.mark.usefixtures("test_browser_invoke")
class TestSeleniumBasics:
    User_name = ReadConfig.getUsername()
    Password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    print("Logger initialized")  # Debugging step
    logger.info("Test message")

    @pytest.fixture(autouse=True)
    # The login method is marked as a fixture with autouse=True, meaning it will run automatically before every test that inherits from BaseTest.
    def test_One(self, browser_setup):
        self.logger.info("*********Browser Invoked*************")
        self.driver = browser_setup
        self.orange_hrm = OrangeHrm(self.driver)
        self.logger.info("*********Username Entered*************")
        self.orange_hrm.enter_username(self.User_name)
        self.logger.info("*********Password Entered*************")
        self.orange_hrm.enter_password(self.Password)
        self.orange_hrm.wait_for_few_seconds()
        self.logger.info("*********Submit button clicked*************")
        self.orange_hrm.click_login()
        self.orange_hrm.wait_for_few_seconds()



