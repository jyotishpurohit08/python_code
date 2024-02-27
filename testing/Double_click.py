from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://demos.telerik.com/kendo-ui/treeview/dragdrop")
driver.implicitly_wait(10)

act = ActionChains(driver)
element = driver.find_element(By.XPATH, "//span[text()='Furniture']")
act.double_click(element).perform()
txt = driver.find_element(By.XPATH, "//span[text()='Tables & Chairs']").text
print("capture text is ", txt)
assert "Tables" in txt
print("assert compeleted")
driver.quit()