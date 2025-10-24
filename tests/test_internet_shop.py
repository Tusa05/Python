from pages.authorization import Authorization
from pages.inventory import Inventory
from pages.cart import Cart
from pages.checkout_step_one import CheckoutStepOne
from pages.checkout_step_two import CheckoutStepTwo
import allure

@allure.title("Проверка интернет-магазина")
@allure.description("Авторизация, добавление товаров в корзину и проверка общей суммы.")
@allure.feature("Покупки")
@allure.severity(allure.severity_level.NORMAL)
def test_internet_shop(browser):
    username = "standard_user"
    password = "secret_sauce"
    first_name = "Natallia"
    last_name = "Sazonava"
    zip_code = "210039"

    with allure.step("Шаг 1: Авторизация пользователя"):
        authorization_page = Authorization(browser)
        authorization_page.authorization(username, password)

    with allure.step("Шаг 2: Добавление товаров в корзину"):
        inventory_page = Inventory(browser)
        inventory_page.add_to_cart()
        inventory_page.go_to_cart()

    with allure.step("Шаг 3: Переход к оформлению заказа"):
        cart_page = Cart(browser)
        cart_page.checkout()

    with allure.step("Шаг 4: Заполнение информации о доставке"):
        checkout_step_one_page = CheckoutStepOne(browser)
        checkout_step_one_page.filling_form(first_name, last_name, zip_code)
        checkout_step_one_page.click_continue()

    with allure.step("Шаг 5: Проверка итоговой суммы"):
        checkout_step_two_page = CheckoutStepTwo(browser)
        total = checkout_step_two_page.read_total()
        assert total[total.find("$"):] == "$58.29"
        allure.attach(f"Итоговая сумма: {total}", name="Проверка суммы", attachment_type=allure.attachment_type.TEXT)
