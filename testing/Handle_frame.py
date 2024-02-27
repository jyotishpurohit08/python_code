from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.redbus.in/")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//li[@id='account_dd']").click()
driver.find_element(By.XPATH, "//li[@id='user_sign_in_sign_up']").click()
print("sigup button click", driver.title)
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='modalIframe']"))
parent_frame = driver.switch_to.parent_frame
print("parent frame is ", parent_frame)
driver.quit()