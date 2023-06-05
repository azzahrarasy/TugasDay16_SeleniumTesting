import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class TestUser(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_failed_login(self): #TestCase1
        baseurl = "https://www.saucedemo.com/"
        driver = self.browser 
        driver.get(baseurl)  
        time.sleep(3) 
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(3) 
        driver.find_element(By.ID, "password").send_keys("")
        time.sleep(3) 
        driver.find_element(By.NAME, "login-button").click()
        time.sleep(3)  
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        self.assertIn("Epic sadface: Password is required", error_message)

    def test_success_login(self): # Test Case2
        baseurl = "https://www.saucedemo.com/"
        driver = self.browser 
        driver.get(baseurl)  
        time.sleep(3) 
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(3)  
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("secret_sauce")
        time.sleep(3)  
        driver.find_element(By.NAME, "login-button").click()
        time.sleep(3)
        
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()