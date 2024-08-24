from selenium.webdriver.common.by import By
from данные import *

def test_shop_form(chrome_broweser):
    chrome_broweser.get(URL_3)
    chrome_broweser.find_element(By.ID, "first_name").send_keys("ИВАН")
    chrome_broweser.find_element(By.ID, "last_name").send_keys("ИВАНОВ")
    chrome_broweser.find_element(By.ID, "user_name").send_keys("standart_user")
    chrome_broweser.find_element(By.ID, "password").send_keys("secred")
    chrome_broweser.find_element(By.ID, "login_button").click("")
    chrome_broweser.find_element(By.ID, "add_to_cart_sauce_labs_backpack").click("")
    chrome_broweser.find_element(By.ID, "add_to_cart_sauce_labs_bolt_t_shirt").click("")
    chrome_broweser.find_element(By.ID, "add_to_cart_sauce_labs_onesie").click("")
    chrome_broweser.find_element(By.ID, "shopping_cart_container").click("")
    chrome_broweser.find_element(By.ID, "checkout").click("")
    chrome_broweser.find_element(By.ID, "postal_code").send_keys("601500")
    chrome_broweser.find_element(By.ID, "continue").click("")
    total_prise = chrome_broweser.find_element(By.CLASS_NAME, 'summary_total_label')
    total = total_prise.text.strip().replace("Total: $", "")

    expected_total = "58.29"
    assert total == expected_total
    print("ИТОГО = $58.29")
