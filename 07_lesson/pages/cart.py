from selenium.webdriver.common.by import By


class Cart:

    def __init__(self, browser):
        self._driver = browser

    def checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()