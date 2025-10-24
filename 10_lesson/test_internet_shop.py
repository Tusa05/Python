from selenium import webdriver
from pages.authorization import Authorization
from pages.inventory import Inventory
from pages.cart import Cart
from pages.checkout_step_one import CheckoutStepOne
from pages.checkout_step_two import CheckoutStepTwo
import allure


@allure.title("Автотест на интернет-магазин")
@allure.description("Авторизация в интернет-магазине, добавление товаров в \
                     корзину, оформление заказа и проверка итоговой суммы.")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.NORMAL)
def test_internet_shop():
    username = "standard_user"
    password = "secret_sauce"
    first_name = "Natallia"
    last_name = "Sazonava"
    zip_code = "210039"

    browser = webdriver.Firefox()

    authorization_page = Authorization(browser)
    authorization_page.authorization(username, password)

    inventory_page = Inventory(browser)
    inventory_page.add_to_cart()

    inventory_page.go_to_cart()

    cart_page = Cart(browser)
    cart_page.checkout()

    checkout_step_one_page = CheckoutStepOne(browser)
    checkout_step_one_page.filling_form(first_name, last_name, zip_code)
    checkout_step_one_page.click_continue()

    checkout_step_two_page = CheckoutStepTwo(browser)

    total = checkout_step_two_page.read_total()
    assert total[total.find("$"):] == "$58.29"

    browser.quit()