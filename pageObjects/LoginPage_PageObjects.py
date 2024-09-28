from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class OrangeHrm:
    # Constructor
    def __init__(self, driver):
        self.driver = driver
        self.username_xpath = "//input[@placeholder='Username']"
        self.password_xpath = "//input[@placeholder='Password']"
        self.login_xpath = "//button[@type='submit']"
        self.dashboard_text_xpath = "//span[@class='oxd-topbar-header-breadcrumb']"
        self.profile_button_xpath = "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"
        self.logout_xpath = "//a[text()='Logout']"

    def enter_username(self, User_name):
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(User_name)

    def enter_password(self, Password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(Password)

    def wait_for_few_seconds(self):
        time.sleep(5)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_xpath).click()

    def Dashboard_text(self):
        Dashboard_text_element = self.driver.find_element(By.XPATH, self.dashboard_text_xpath)

    def profile_button(self):
        user_profile_button = self.driver.find_element(By.XPATH, self.profile_button_xpath)
        user_profile_button.click()

    def click_logout_button(self):
        self.driver.find_element(By.XPATH, self.logout_xpath).click()
