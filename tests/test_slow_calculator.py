from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.slow_calculator import SlowCalculator
import allure


@allure.title("Проверка медленного калькулятора")
@allure.description("Тестирует корректность вычислений на странице 'Slow Calculator'.")
@allure.feature("Функциональность калькулятора")
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calculator(browser):
    """
    Тестовый сценарий для проверки калькулятора.
    
    Args:
        browser: Экземпляр веб-драйвера, предоставленный фикстурой pytest.
    """
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    timeout = 45

    # Создание экземпляра класса страницы, передавая ему браузер.
    # Переход по URL происходит внутри конструктора SlowCalculator.
    main_page = SlowCalculator(browser, url)
    
    with allure.step("Шаг 1: Установка таймаута на странице и нажатие кнопок"):
        main_page.set_timeout(timeout)
        main_page.pressing_buttons()
    
    with allure.step("Шаг 2: Использование явного ожидания"):
        waiter = WebDriverWait(browser, timeout)
        waiter.until(
            EC.text_to_be_present_in_element(main_page._DISPLAY_DISPLAY, "15")
        )
    
    with allure.step("Шаг 3: Проверка результата"):
        result_text = main_page.get_result()
        assert result_text == "15"
        allure.attach(f"Проверенный результат: {result_text}", name="Результат калькулятора", attachment_type=allure.attachment_type.TEXT)

