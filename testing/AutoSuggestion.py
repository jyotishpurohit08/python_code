from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-autocomplete-feature-in.html")
driver.implicitly_wait(10)
driver.find_element(By.ID, 'tags').send_keys("S")
listElement = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']//div")

print("total suggestion are", len(listElement))
for ele in listElement:
    print(ele.text)
    if ele.text=='Selenium':
        print("record found")
        ele.click()
        break
driver.quit()
