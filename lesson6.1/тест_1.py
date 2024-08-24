from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from данные import *
from time import sleep

def test_data_types_form(chrome_broweser):
    chrome_broweser.get(URL_1)
    chrome_broweser.find_element(By.NAME, "first_name").send_keys(first_name)
    chrome_broweser.find_element(By.NAME, "last_name").send_keys(last_name)
    chrome_broweser.find_element(By.NAME, "address").send_keys(address)
    chrome_broweser.find_element(By.NAME, "email").send_keys(email)
    chrome_broweser.find_element(By.NAME, "phone").send_keys(phone)
    chrome_broweser.find_element(By.NAME, "zip_code").send_keys(zip_code)
    chrome_broweser.find_element(By.NAME, "city").send_keys(city)
    chrome_broweser.find_element(By.NAME, "country").send_keys(country)
    chrome_broweser.find_element(By.NAME, "job_position").send_keys(job_position)
    chrome_broweser.find_element(By.NAME, "company").send_keys(company)
    WebDriverWait(chrome_broweser, 40, 0.1).until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
    sleep(2)
    assert "success" in chrome_broweser.find_element(By.ID, "first_name").get_attribute("class")
    assert "success" in chrome_broweser.find_element(By.ID, "last_name").get_attribute("class")
    assert "success" in chrome_broweser.find_element(By.ID, "address").get_attribute("class")
    assert "success" in chrome_broweser.find_element(By.ID, "email").get_attribute("class")
    assert "success" in chrome_broweser.find_element(By.ID, "phone").get_attribute("class")
    assert "danger" in chrome_broweser.find_element(By.ID, "zip_code").get_attribute("class")
    assert "success" in chrome_broweser.find_element(By.ID, "city").get_attribute("class")
    assert "success" in chrome_broweser.find_element(By.ID, "country").get_attribute("class")
    assert "success" in chrome_broweser.find_element(By.ID, "job_position").get_attribute("class")
    assert "success" in chrome_broweser.find_element(By.ID, "company").get_attribute("class")