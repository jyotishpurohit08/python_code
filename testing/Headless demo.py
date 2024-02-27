from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

opt=Options()
opt.add_argument("--headless")
driver = webdriver.Firefox(GeckoDriverManager().install(), firefox_options=opt)
driver.maximize_window()
driver.get("http://www.google.com")
driver.implicitly_wait(10)
driver.find_element(By.NAME, "q").send_keys("jyotish purohit")
driver.quit()
print("jyotish")