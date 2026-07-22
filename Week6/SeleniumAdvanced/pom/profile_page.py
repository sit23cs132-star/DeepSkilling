from selenium.webdriver.common.by import By

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.profile_header = (By.ID, "profileHeader")
        self.file_input = (By.ID, "fileInput")
        self.upload_btn = (By.ID, "uploadBtn")

    def take_screenshot(self, filename="profile_page.png"):
        self.driver.save_screenshot(filename)

    def upload_profile_picture(self, file_path):
        self.driver.find_element(*self.file_input).send_keys(file_path)
        self.driver.find_element(*self.upload_btn).click()
