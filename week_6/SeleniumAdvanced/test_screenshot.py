from selenium import webdriver

def test_screenshot():
    driver = webdriver.Chrome()
    driver.get("https://example.com/profile")
    driver.save_screenshot("profile_page.png")
    driver.quit()
