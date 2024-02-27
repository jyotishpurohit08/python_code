from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(GeckoDriverManager().install())
driver.maximize_window()
driver.get("http://www.google.com")
driver.find_element(By.NAME, "q").send_keys("jyotish purohit")