import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/form/div[1]/div[2]/div[2]/div[2]/div/input[2]").click()
print("click")
time.sleep(5)
alt = driver.switch_to.alert
alt_text = alt.text
print("Alert text is", alt_text)
alt.accept()
driver.find_element(By.XPATH, "//*[@id='login1']").send_keys("selenium")
#driver.find_element(By.Name, "passwd").send_keys("123456")
driver.quit()
