from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


class CheckoutStepOne:
    """
    Класс для работы со страницей оформления заказа.
    """
    def __init__(self, browser: webdriver):
        self._driver = browser

    def _fill_field(self, locator: str, text: str) -> None:
        """
        Приватный метод для заполнения поля по CSS-селектору.
        
        Args:
            locator: CSS-селектор элемента.
            text: Текст для ввода.
        """
        self._driver.find_element(By.CSS_SELECTOR, locator).send_keys(text)

    def filling_form(self, first_name: str, last_name: str, zip_code: str) -> None:
        """
        Заполняет форму информации о покупателе.
        
        Args:
            first_name: Имя.
            last_name: Фамилия.
            zip_code: Почтовый индекс.
        """
        self._fill_field("#first-name", first_name)
        self._fill_field("#last-name", last_name)
        self._fill_field("#postal-code", zip_code)
    
    @allure.step("Нажимает кнопку 'Continue'.")
    def click_continue(self) -> None:
        """
        Нажимает кнопку "Continue".
        """
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()
