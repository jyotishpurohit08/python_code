import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class VerifyCartItemTest:
    def setUp(self):
        # Set up the Chrome WebDriver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.demoblaze.com/")
        self.driver.maximize_window()
        print("Chrome opened successfully")

    def tearDown(self):
        # Close the browser
        if self.driver:
            self.driver.quit()

    def test_add_item_to_cart(self):
        driver = self.driver

        # Find and click the 'Add to Cart' button (adjust the locator to match the actual element)
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Add to cart"))
        )
        add_to_cart_button.click()

        # Accept the alert
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()

        # Navigate to the cart page
        driver.get("https://www.demoblaze.com/cart.html")

        # Find the cart item elements (adjust the locator to match the actual HTML structure)
        cart_item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img[width='100']"))
        )

        # Assert that the item is in the cart
        self.assertTrue(cart_item.is_displayed(), "Item was not added to the cart.")

if __name__ == "__main__":
    unittest.main()
