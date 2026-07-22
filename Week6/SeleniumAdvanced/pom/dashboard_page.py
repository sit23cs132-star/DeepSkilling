from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_msg = (By.ID, "welcomeMsg")

    def get_welcome_message(self, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.welcome_msg)
        )
        return element.text
