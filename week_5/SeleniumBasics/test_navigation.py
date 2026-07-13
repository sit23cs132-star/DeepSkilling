from selenium import webdriver
from selenium.webdriver.common.by import By

def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://example.com")

    driver.find_element(By.LINK_TEXT, "Courses").click()
    assert "Courses" in driver.title

    driver.quit()
