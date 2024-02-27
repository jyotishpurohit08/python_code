from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.globalsqa.com/demo-site/")
ele = driver.find_element(By.NAME, 's')
ele.send_keys("selenium")
print("=============== Text fill successfully==========="+driver.title)
click_button = driver.find_element(By.CLASS_NAME, 'button_search')
click_button.click()
print("=============== click successfully==========="+driver.current_url)
driver.quit()
