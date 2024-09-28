from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Recruitment:

    def __init__(self, driver):
        self.driver = driver
        self.xpath_for_recruitment_option = "(//li[@class='oxd-main-menu-item-wrapper'])[5]"
        self.xpath_for_add_button = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
        self.xpath_for_first_name = "//input[@placeholder='First Name']"
        self.xpath_for_email = "(//input[@class='oxd-input oxd-input--active'])[2]"
        self.xpath_for_save_button = "//button[@type='submit']"

    def click_the_recruitment_option(self):
        self.driver.find_element(By.XPATH, self.xpath_for_recruitment_option).click()

    def click_the_add_button(self):
        self.driver.find_element(By.XPATH, self.xpath_for_add_button).click()

    def enter_the_first_name(self, First_Name):
        self.driver.find_element(By.XPATH, self.xpath_for_first_name).send_keys(First_Name)

    def enter_the_email(self, Email_address):
        self.driver.find_element(By.XPATH, self.xpath_for_email).send_keys(Email_address)

    def click_the_save_button(self):
        self.driver.find_element(By.XPATH, self.xpath_for_save_button).click()



