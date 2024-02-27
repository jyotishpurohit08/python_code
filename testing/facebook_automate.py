from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")
driver.implicitly_wait(5)
button = driver.find_element(By.XPATH,
                             "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a")
button.click()
driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Aman")
driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Agrwal")
driver.find_element(By.XPATH, "//input[@name='reg_email__']").send_keys("amanagrwal19@gmail.com")
driver.find_element(By.XPATH, "//input[@name='reg_email_confirmation__']").send_keys("amanagrwal19@gmail.com")
driver.find_element(By.XPATH, "//input[@name='reg_passwd__']").send_keys("Aman@19")
day = Select(driver.find_element(By.XPATH, "//select[@name='birthday_day']"))
day.select_by_visible_text("10")
month = Select(driver.find_element(By.XPATH, "//select[@name='birthday_month']"))
month.select_by_visible_text("Mar")
year = Select(driver.find_element(By.XPATH, "//select[@name='birthday_year']"))
year.select_by_visible_text("2001")
driver.find_element(By.XPATH, "//label[text()='Male']").click()
# time.sleep(2)
driver.find_element(By.XPATH,
                    "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[11]/button").click()
print("======Registration compelete successfully=====", driver.current_url)
driver.quit()
