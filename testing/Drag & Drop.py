from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://demos.telerik.com/kendo-ui/treeview/dragdrop")
driver.implicitly_wait(10)

act = ActionChains(driver)
src = driver.find_element(By.XPATH, "//span[text()='Occasional Furniture']")
dest = driver.find_element(By.XPATH, "//span[text()='Kids Storage']")
act.drag_and_drop(src,dest).perform()
driver.quit()