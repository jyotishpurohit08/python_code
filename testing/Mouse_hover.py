import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-perform-mouse-hover-in-selenium.html")
mouse_hover = driver.find_element(By.XPATH, "//button[text()='Automation Tools']")
act = ActionChains(driver)

#first way
#act.move_to_element(mouse_hover).perform()

# Second way
act.move_to_element(mouse_hover).pause(3).click(driver.find_element(By.XPATH, "//a[text()='Appium']")).perform()
print("********* successfull*******")
driver.quit()
