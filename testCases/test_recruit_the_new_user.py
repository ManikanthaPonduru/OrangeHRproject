from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.readProperties import ReadConfig
from pageObjects.Recruitment_PageObjects import Test_Recruitment
from Utilities.customLogger import LogGen
from testCases.test_login import TestSeleniumBasics


class TestRecruitNewUser(TestSeleniumBasics):
    First_Name = ReadConfig.getFirstUserName()
    Email_address = ReadConfig.getEmailAddress()
    option_text = 'test'
    logger = LogGen.loggen()

    def test_recruit_new_person(self):
        self.logger.info("*********Browser Invoked*************")
        self.recruit = Test_Recruitment(self.driver)

        # *********Browser Invoked*************
        wait = WebDriverWait(self.driver, 10)
        self.logger.info("*********waiting to identify the xpath of recruitment button*************")
        wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.recruit.xpath_for_recruitment_option)))
        self.logger.info("**********Clicking the recruitment option************")
        self.recruit.click_the_recruitment_option()
        self.logger.info("*********waiting to identify the xpath of add button*************")
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.recruit.xpath_for_add_button)))
        self.logger.info("**********Clicking the add button************")
        self.recruit.click_the_add_button()
        self.logger.info("*********waiting to identify the xpath of firstname field*************")
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.recruit.xpath_for_first_name)))
        self.logger.info("*********Sending the name into First Name field*************")
        self.recruit.enter_the_first_name(self.First_Name)
        self.logger.info("*********waiting to identify the xpath of email field*************")
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.recruit.xpath_for_email)))
        self.logger.info("*********Sending the name into Email field*************")
        self.recruit.enter_the_email(self.Email_address)
        self.logger.info("*********waiting to identify the xpath of save button************")
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.recruit.xpath_for_save_button)))
        self.logger.info("*********Click the save button*************")
        self.recruit.click_the_save_button()
