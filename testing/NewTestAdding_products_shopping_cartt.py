import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager

class NewTestAddingProductsToShoppingCart:
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

    def test_click_product(self):
        # Find and click the product
        product = self.driver.find_element(By.CLASS_NAME, "card-img-top")
        product.click()

    def test_click_add_to_cart(self):
        # Find and click the 'Add to cart' link
        add_cart = self.driver.find_element(By.LINK_TEXT, "Add to cart")
        add_cart.click()

    def test_accept_popup(self):
        # Assuming the previous action triggers a popup
        # Switch to the alert and accept it
        alert = Alert(self.driver)
        alert_text = alert.text
        print("Alert text: " + alert_text)  # Optional: Print the alert text for verification
        alert.accept()

if __name__ == "__main__":
    unittest.main()
