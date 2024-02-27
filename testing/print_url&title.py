from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service

#s=Service("C:\\Users\\HP\\Downloads\\geckodriver.exe")
driver = webdriver.Firefox()
driver.get("http://learn-automation.com")
print(driver.title)
print(driver.current_url)
print("================ Title & Url print successfully===============")
driver.quit()
