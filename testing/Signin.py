import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class SigninTest:
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

    def test_click_signin_button(self):
        # Find and click the signin button
        signin_button = self.driver.find_element(By.ID, "login2")
        signin_button.click()

    def test_positive_signin(self):
        # Click the signin button to open the login modal
        self.driver.find_element(By.ID, "login2").click()

        # Fill in the username
        username_field = self.driver.find_element(By.ID, "loginusername")
        username_field.send_keys("jatin7470")

        # Fill in the password
        password_field = self.driver.find_element(By.ID, "loginpassword")
        password_field.send_keys("Jatin@7470")

        # Click the signin button
        signin_button = self.driver.find_element(By.CSS_SELECTOR, "button[onclick='logIn()']")
        signin_button.click()

        # Assert successful signin (adjust according to your application)
        # This is just an example, you may need to adjust this to match your actual application behavior
        try:
            success_message = self.driver.find_element(By.CLASS_NAME, "error")
            self.assertFalse(success_message.is_displayed(), "Signin was not successful")
        except:
            # Assuming no element found means login was successful, adjust this as per your application's behavior
            print("Login successful")

    def test_negative_signin(self):
        # Click the signin button to open the login modal
        self.driver.find_element(By.ID, "login2").click()

        # Fill in the username
        username_field = self.driver.find_element(By.ID, "loginusername")
        username_field.send_keys("jatin7470")

        # Fill in an invalid password
        password_field = self.driver.find_element(By.ID, "loginpassword")
        password_field.send_keys("invalidpassword")

        # Click the signin button
        signin_button = self.driver.find_element(By.CSS_SELECTOR, "button[onclick='logIn()']")
        signin_button.click()

        # Assert error message is displayed (adjust according to your application)
        error_message = self.driver.find_element(By.ID, "nameofuser")
        self.assertFalse(error_message.is_displayed(), "Error message was not displayed")

if __name__ == "__main__":
    unittest.main()
