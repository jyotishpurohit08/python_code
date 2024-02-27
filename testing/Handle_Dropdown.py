from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")
button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a")
button.click()
time.sleep(3)
day = driver.find_element(By.ID, "day")
dayDD = Select(day)
dayDD.select_by_value("2")
time.sleep(3)
month = driver.find_element(By.ID, "month")
monthDD = Select(month)
ddlist = monthDD.options
firstItem = monthDD.first_selected_option
print("first option is", firstItem.text)
print(len(ddlist))
for ele in ddlist:
    print(ele.text)
monthDD.select_by_index(2)
time.sleep(3)
driver.quit()
