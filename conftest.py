import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import allure

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests (e.g., chrome, firefox)")

@pytest.fixture
@allure.title("Настройка и закрытие браузера")
def browser(request):
    """
    Фикстура для инициализации и закрытия браузера.
    """
    browser_name = request.config.getoption("--browser").lower()
    driver = None
    
    with allure.step(f"Запуск браузера: {browser_name}"):
        if browser_name == "chrome":
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
        elif browser_name == "firefox":
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service)
        else:
            pytest.fail(f"Браузер '{browser_name}' не поддерживается.")

    driver.maximize_window()
    
    # Отчетность о браузере, используемом в тесте
    allure.environment(browser=driver.capabilities['browserName'], version=driver.capabilities['browserVersion'])
    
    yield driver
    
    with allure.step("Закрытие браузера"):
        driver.quit()
