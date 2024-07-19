import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class VerifyProductTest:
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

    def test_products_displayed(self):
        driver = self.driver

        # Find the product elements (adjust the locator to match the actual HTML structure)
        products = driver.find_elements(By.CSS_SELECTOR, ".col-lg-9")

        # Assert that products are displayed
        self.assertTrue(len(products) > 0, "No products are displayed on the homepage.")

        # Additional check to ensure each product is visible
        for product in products:
            self.assertTrue(product.is_displayed(), "Product is not visible: " + product.text)

if __name__ == "__main__":
    unittest.main()
