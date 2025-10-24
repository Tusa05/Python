from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


class Authorization:
    """
    Класс содержит методы для авторизации пользователя.

    """

    def __init__(self, browser: webdriver):
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/")
        self._driver.maximize_window()

    @allure.step("Авторизация с логином {username} и паролем {password}")
    def authorization(self, username: str, password: str):
        """
        Вводим логин и пароль пользователя. 
        Нажимаем кнопку "Login".
        
        """
        self._driver.find_element(By.CSS_SELECTOR, 'input[id="user-name"]').\
            send_keys("standard_user")
        self._driver.find_element(By.CSS_SELECTOR, 'input[id="password"]').\
            send_keys("secret_sauce")
        self._driver.find_element(By.CSS_SELECTOR,
                                  'input[id="login-button"]').click()
