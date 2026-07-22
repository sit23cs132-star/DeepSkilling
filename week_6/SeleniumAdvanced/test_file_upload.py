from selenium import webdriver
from selenium.webdriver.common.by import By

def test_file_upload():
    driver = webdriver.Chrome()
    driver.get("https://example.com/upload")
    driver.find_element(By.ID, "fileInput").send_keys("/path/to/file.txt")
    driver.find_element(By.ID, "uploadBtn").click()
    assert "Upload successful" in driver.page_source
    driver.quit()
