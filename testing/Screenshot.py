from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.google.com")
driver.implicitly_wait(10)
driver.get_screenshot_as_file("Selenium.png")
driver.get("http://www.facebook.com")
driver.get_screenshot_as_file("Selenium.png1")
driver.quit()