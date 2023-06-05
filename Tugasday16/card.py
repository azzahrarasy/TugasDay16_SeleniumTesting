import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class TestCard(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_card(self): # Test Case3
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
        driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(3)
        url = driver.current_url
        self.assertIn (url, "https://www.saucedemo.com/cart.html")
        
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()