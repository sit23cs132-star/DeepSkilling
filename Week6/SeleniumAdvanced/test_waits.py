from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_explicit_wait():
    driver = webdriver.Chrome()
    driver.get("https://example.com/dashboard")

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "welcomeMsg"))
    )
    assert element.text == "Welcome!"
    driver.quit()
