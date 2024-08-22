from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from данные import *

def test_calculator_form(chrome_broweser):
    chrome_broweser.get(URL_2)
    delay_input = chrome_broweser.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys(45)
    chrome_broweser.find_element(By.XPATH, "//span[text() = '7']").click()
    chrome_broweser.find_element(By.XPATH, "//span[text() = '+']").click()
    chrome_broweser.find_element(By.XPATH, "//span[text() = '8']").click()
    chrome_broweser.find_element(By.XPATH, "//span[text() = '=']").click()
    
    result = WebDriverWait(chrome_broweser, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    result_text = chrome_broweser.find_element(By.CLASS_NAME, "screen").text

    assert result_text == "15"