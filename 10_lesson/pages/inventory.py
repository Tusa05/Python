from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure


class Inventory:
    """
    Класс для работы со страницей инвентаря.
    """
    def __init__(self, browser: WebDriver):
        self._driver = browser

    def _click_element(self, locator: str) -> None:
        """
        Приватный метод для клика по элементу с заданным CSS-селектором.

        Args:
            locator: CSS-селектор элемента.
        """
        self._driver.find_element(By.CSS_SELECTOR, locator).click()

    @allure.step("Добавляет несколько товаров в корзину.")
    def add_to_cart(self) -> None:
        """
        Добавляет несколько товаров в корзину.
        """
        self._click_element("#add-to-cart-sauce-labs-backpack")
        self._click_element("#add-to-cart-sauce-labs-bolt-t-shirt")
        self._click_element("#add-to-cart-sauce-labs-onesie")

    def go_to_cart(self) -> None:
        """
        Переходит в корзину.
        """
        self._click_element(".shopping_cart_link")
