
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class SauceDemoAutomation(unittest.TestCase):

    BASE_URL = "https://www.saucedemo.com/"

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(
            self.driver,
            20,
            ignored_exceptions=(StaleElementReferenceException,)
        )

        self.driver.get(self.BASE_URL)

        self.wait.until(
            EC.visibility_of_element_located((By.ID, "login-button"))
        )

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def click_element(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def test_AT01_valid_login(self):
        self.login("standard_user", "secret_sauce")

        self.wait.until(EC.url_contains("inventory.html"))

        self.assertIn("inventory.html", self.driver.current_url)
        print("AT01: Valid login - PASS")

    def test_AT02_invalid_login(self):
        self.login("standard_user", "wrong_password")

        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "[data-test='error']"),
                "do not match"
            )
        )

        print("AT02: Invalid login - PASS")

    def test_AT03_add_product(self):
        self.login("standard_user", "secret_sauce")

        self.wait.until(EC.url_contains("inventory.html"))

        self.click_element(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )

        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "shopping_cart_badge"),
                "1"
            )
        )

        print("AT03: Add product - PASS")

    def test_AT04_verify_cart(self):
        self.login("standard_user", "secret_sauce")

        self.wait.until(EC.url_contains("inventory.html"))

        self.click_element(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )

        self.click_element(
            (By.CLASS_NAME, "shopping_cart_link")
        )

        self.wait.until(EC.url_contains("cart.html"))

        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "inventory_item_name"),
                "Sauce Labs Backpack"
            )
        )

        print("AT04: Cart verification - PASS")

    def test_AT05_remove_product(self):
        self.login("standard_user", "secret_sauce")

        self.wait.until(EC.url_contains("inventory.html"))

        self.click_element(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )

        self.click_element(
            (By.CLASS_NAME, "shopping_cart_link")
        )

        self.wait.until(EC.url_contains("cart.html"))

        self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "cart_item")
            )
        )

        self.click_element(
            (By.ID, "remove-sauce-labs-backpack")
        )

        self.wait.until(
            lambda driver: len(
                driver.find_elements(By.CLASS_NAME, "cart_item")
            ) == 0
        )

        print("AT05: Remove product - PASS")

    def tearDown(self):
        if hasattr(self, "driver"):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
