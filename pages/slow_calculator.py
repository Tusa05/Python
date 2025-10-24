from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure

class SlowCalculator:

    # Выносим локаторы в переменные класса
    _DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    _DISPLAY_DISPLAY = (By.XPATH, '//*[@id="calculator"]/div[1]/div')
    _BUTTON_7 = (By.XPATH, '//*[@id="calculator"]/div[2]/span[1]')
    _BUTTON_PLUS = (By.XPATH, '//*[@id="calculator"]/div[2]/span[4]')
    _BUTTON_8 = (By.XPATH, '//*[@id="calculator"]/div[2]/span[2]')
    _BUTTON_EQUAL = (By.XPATH, '//*[@id="calculator"]/div[2]/span[15]')

    def __init__(self, browser: WebDriver, url: str):
        self._driver = browser
        with allure.step(f"Переход по URL: {url}"):
            self._driver.get(url)
        self._driver.maximize_window()

    @allure.step("Установка задержки в {timeout} секунд")
    def set_timeout(self, timeout: int) -> None:
        """
        Устанавливает задержку для калькулятора.
        """
        # Сначала очищаем поле ввода
        self._driver.find_element(*self._DELAY_INPUT).clear()
        # Затем вводим новое значение
        self._driver.find_element(*self._DELAY_INPUT).send_keys(str(timeout))
        
    def _click_element(self, locator: tuple, name: str) -> None:
        """
        Приватный метод для клика по элементу с заданным локатором.
        """
        with allure.step(f"Нажатие кнопки '{name}'"):
            self._driver.find_element(*locator).click()

    @allure.step("Нажатие кнопок на калькуляторе")
    def pressing_buttons(self) -> None:
        """
        Нажимает на заданную последовательность кнопок калькулятора.
        """
        self._click_element(self._BUTTON_7, "7")
        self._click_element(self._BUTTON_PLUS, "+")
        self._click_element(self._BUTTON_8, "8")
        self._click_element(self._BUTTON_EQUAL, "=")

    @allure.step("Получение результата с дисплея")
    def get_result(self) -> str:
        """
        Возвращает текст из поля с результатом.
        """
        return self._driver.find_element(*self._CALCULATOR_DISPLAY).text
