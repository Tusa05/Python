from selenium.webdriver.common.by import By


class SlowCalculator:

    def __init__(self, browser, url):
        self._driver = browser
        self._driver.get(url)
        self._driver.maximize_window()

    def set_timeout(self, timeout):
        # В поле ввода по локатору #delay вводим значение 45.
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").\
            send_keys(str(timeout))

    def pressing_buttons(self):
        self._driver.find_element(By.XPATH,
                                  '//*[@id="calculator"]/div[2]/span[1]').\
            click()
        self._driver.find_element(By.XPATH,
                                  '//*[@id="calculator"]/div[2]/span[4]').\
            click()
        self._driver.find_element(By.XPATH,
                                  '//*[@id="calculator"]/div[2]/span[2]').\
            click()
        self._driver.find_element(By.XPATH,
                                  '//*[@id="calculator"]/div[2]/span[15]').\
            click()