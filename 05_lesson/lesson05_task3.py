from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")


search_field = driver.find_element(By.CSS_SELECTOR, "input")
search_field.send_keys("Sky")
sleep(1)

search_field.clear()

search_field.send_keys("Pro")

driver.quit()
