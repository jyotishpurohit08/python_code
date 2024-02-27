from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-autocomplete-feature-in.html")
parentwindow = driver.current_window_handle
print("parent window handle", parentwindow)
driver.find_element(By.XPATH, "//*[@id='Blog1']/div[1]/div/div/div/div[1]/div[3]/div[1]/div/a[1]/span").click()
childwindow = driver.window_handles
print("type of all window", childwindow)

for child in childwindow:
    print(child)
    if parentwindow!= child:
        print("switchingto new window/tab")
        driver.switch_to.window(child)
        print("title is", driver.title)
        driver.close()

driver.switch_to.window(parentwindow)
print(driver.title)
driver.quit()