from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


class Cart:
    """
    Класс содержит методы для нажатия кнопки "Checkout".
    """

    def __init__(self, browser: webdriver):
        self._driver = browser
    
    @allure.step("Нажатие кнопки 'Checkout'.")
    def checkout(self) -> None:
        """
        Нажатие кнопки 'Checkout'.
        """
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()
