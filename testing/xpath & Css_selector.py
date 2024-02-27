from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
assert "Swag Labs" in driver.title
print(driver.title)
username = driver.find_element(By.XPATH, "//input[@id='user-name']")
username.send_keys("standard_user")
password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
password.send_keys("secret_sauce")
login_button = driver.find_element(By.ID, 'login-button')
login_button.click()
print("URL after login", driver.current_url)
assert "inventory.html" in driver.current_url
print(driver.current_url + "======== login successfully ===========" + driver.title)
driver.quit()
