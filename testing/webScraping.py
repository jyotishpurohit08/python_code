from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("Samsung phone")
driver.find_element(By.XPATH, "//*[@id='nav-search-submit-button']").click()
driver.find_element(By.XPATH, "//span[text()='Samsung']").click()
listElement = driver.find_elements(By.XPATH, "//span[contains(@class,'a-size-medium a-color-base a-text-normal')]")
listElement2 = driver.find_elements(By.XPATH, "//span[contains(@class,'price-whole')]")


for ele in listElement:
    print(ele.text)

print("*"*50)

for ele2 in listElement2:
    print(ele2.text)

    driver.quit()
