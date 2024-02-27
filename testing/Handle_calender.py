from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//input[@id='datepicker']").click()
driver.find_element(By.XPATH, "//a[text()='25']").click()
