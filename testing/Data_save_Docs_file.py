from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Selenium WebDriver
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(10)

# Search for Samsung phone
search_box = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
search_box.send_keys("Samsung phone")
search_button = driver.find_element(By.XPATH, "//*[@id='nav-search-submit-button']")
search_button.click()

# Filter for Samsung products
samsung_filter = driver.find_element(By.XPATH, "//span[text()='Samsung']")
samsung_filter.click()

# Extract product names
product_names = driver.find_elements(By.XPATH, "//span[contains(@class,'a-size-medium a-color-base a-text-normal')]")
product_names_list = [product.text for product in product_names]

# Extract product prices
product_prices = driver.find_elements(By.XPATH, "//span[contains(@class,'price-whole')]")
product_prices_list = [price.text for price in product_prices]

# Combine product names and prices into a string
data = ""
for name, price in zip(product_names_list, product_prices_list):
    data += f"{name}: {price}\n"

# Save data to a text file
with open('amazon_products.txt', 'w') as f:
    f.write(data)

# Close the browser
driver.quit()
