import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link2)

    #заполнение обязательных полей при регистрации
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    first_name.send_keys("sdad")
    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    last_name.send_keys("sdaas")
    email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    email.send_keys("sadqw")

    #зарегать
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()
    time.sleep(2)

    #проверка на успешность
    expect_result = "Congratulations! You have successfully registered!"
    fact_result = browser.find_element(By.TAG_NAME, "h1")
    fact_result_str = fact_result.text
    assert expect_result == fact_result_str

finally:
    time.sleep(5)
    browser.quit()
