from selenium import webdriver
from selenium.webdriver.common.service import Service

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.google.com")
myPageTitle = driver.title
print(myPageTitle)
assert "Google" in myPageTitle
driver.quit()