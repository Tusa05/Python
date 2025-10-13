from selenium import webdriver
from selenium.webdriver.common.by import By

def test_form_validation():
        driver = webdriver.Edge()
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        first_name_field = driver.find_element(By.NAME,'first-name')
        first_name_field.send_keys("Иван")

        last_name_field = driver.find_element(By.NAME,'last-name')
        last_name_field.send_keys("Петров")

        address_field = driver.find_element(By.NAME,'address')
        address_field.send_keys("Ленина, 55-3")

        email_field = driver.find_element(By.NAME,'e-mail')
        email_field.send_keys("test@skypro.com")

        phone_field = driver.find_element(By.NAME,'phone')
        phone_field.send_keys("+7985899998787")

        city_field = driver.find_element(By.NAME,'city')
        city_field.send_keys("Москва")

        country_field = driver.find_element(By.NAME,'country')
        country_field.send_keys("Россия")

        job_position_field = driver.find_element(By.NAME,'job-position')
        job_position_field.send_keys("QA")

        company_field = driver.find_element(By.NAME,'company')
        company_field.send_keys("SkyPro")

        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

    
        pole_z = driver.find_element(By.ID, "zip-code").get_attribute("class")
        assert pole_z == "alert py-2 alert-danger"

   
        poles = ["#first-name", "#last-name", "#address", "#city", "#country", "#e-mail", "#phone", "#company"]
        for pole in poles:
                pole_class = driver.find_element(By.CSS_SELECTOR, pole).get_attribute("class")
                assert pole_class == "alert py-2 alert-success"

        driver.quit()


