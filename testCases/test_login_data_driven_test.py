import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.readProperties import ReadConfig
from pageObjects.LoginPage_PageObjects import OrangeHrm
from Utilities.customLogger import LogGen
from Utilities import XLUtils


# @pytest.mark.usefixtures("test_browser_invoke")
class Test_Data_Driven:
    path = ".//TestData/LoginData.xlsx"

    logger = LogGen.loggen()

    def test_login_data_driven(self, browser_setup):
        self.logger.info("*********Test_Data_Driven*************")
        self.logger.info("*********Browser Invoked*************")
        self.driver = browser_setup
        self.orange_hrm = OrangeHrm(self.driver)

        # Get number of rows in Excel
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("No.of rows in Excel:", self.rows)

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.expectation = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.logger.info(f"Test case: User={self.user}, Password={self.password}, Expectation={self.expectation}")

            # Enter the username and password and click submit button
            self.orange_hrm.enter_username(self.user)
            # Enter the password using the Excel
            self.orange_hrm.enter_password(self.password)
            # Click the submit button
            self.orange_hrm.click_login()

            # Validating the page title
            actual_title = self.orange_hrm.driver.title
            print(actual_title)
            exp_title = "OrangeHRM"

            if actual_title == exp_title:
                if self.expectation == "Pass":
                    self.logger.info("Login successful - expected PASS")

                    wait = WebDriverWait(self.driver, 10)
                    # Waiting to locate the Dashboard element on the page
                    dashboard_element = wait.until(
                        expected_conditions.visibility_of_element_located(
                            (By.XPATH, self.orange_hrm.dashboard_text_xpath)))
                    # Printing the Dashboard text
                    print(dashboard_element.text)
                    wait.until(
                        expected_conditions.visibility_of_element_located(
                            (By.XPATH, self.orange_hrm.profile_button_xpath)))
                    self.orange_hrm.profile_button()
                    wait.until(
                        expected_conditions.visibility_of_element_located((By.XPATH, self.orange_hrm.logout_xpath)))
                    self.orange_hrm.click_logout_button()
                    time.sleep(20)
                    if self.expectation == "Pass":
                        print("expectation is pass")
                    else:
                        print("expectation is fail")


