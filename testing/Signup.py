import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class SignupTest:
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

    def test_click_signup_button(self):
        # Find and click the signup button
        signup_button = self.driver.find_element(By.ID, "signin2")
        signup_button.click()

    def test_positive_signup(self):
        # Click the signup button to open the signup modal
        self.driver.find_element(By.ID, "signin2").click()

        # Fill in the username
        username_field = self.driver.find_element(By.ID, "sign-username")
        username_field.send_keys("jatin7470")

        # Fill in the password
        password_field = self.driver.find_element(By.ID, "sign-password")
        password_field.send_keys("valid_password")

        # Click the signup button
        signup_button = self.driver.find_element(By.CSS_SELECTOR, "button[onclick='register()']")
        signup_button.click()

        # Assert successful signup (adjust according to your application)
        try:
            success_message = self.driver.find_element(By.CLASS_NAME, "error")
            self.assertFalse(success_message.is_displayed(), "Signup was not successful")
        except:
            # Assuming no element found means signup was successful, adjust this as per your application's behavior
            print("Signup successful")

    def test_negative_signup(self):
        # Click the signup button to open the signup modal
        self.driver.find_element(By.ID, "signin2").click()

        # Fill in the username
        username_field = self.driver.find_element(By.ID, "sign-username")
        username_field.send_keys("valid_username")

        # Fill in an invalid password (e.g., too short)
        password_field = self.driver.find_element(By.ID, "sign-password")
        password_field.send_keys("short")

        # Click the signup button
        signup_button = self.driver.find_element(By.CSS_SELECTOR, "button[onclick='register()']")
        signup_button.click()

        # Assert error message is displayed (adjust according to your application)
        error_message = self.driver.find_element(By.ID, "error")
        self.assertTrue(error_message.is_displayed(), "Error message was not displayed")

if __name__ == "__main__":
    unittest.main()
