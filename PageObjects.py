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

    def enter_username(self, User_name):
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(User_name)

    def enter_password(self, Password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(Password)

    def wait_for_few_seconds(self):
        time.sleep(5)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_xpath).click()
