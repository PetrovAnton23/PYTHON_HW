from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from lesson_7.links import test_form_URL 
from lesson_7.data_types.data import * 

class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(test_form_URL)

    def find_fields(self):
        self.first_name = "first_name"
        self.last_name = "last_name"
        self.address = "address"
        self.email = "email"
        self.phone = "phone"
        self.zip_code = "zip_code"
        self.city = "city"
        self.country = "country"
        self.job_position = "job_position"
        self.company = "company"

    def filling_in_the_fields(self):
        self.browser.find_element(By.NAME, self._first_name).send_keys(first_name)
        self.browser.find_element(By.NAME, self._last_name).send_keys(last_name)
        self.browser.find_element(By.NAME, self._address).send_keys(address)
        self.browser.find_element(By.NAME, self._email).send_keys(email)
        self.browser.find_element(By.NAME, self._phone).send_keys(phone)
        self.browser.find_element(By.NAME, self._zip_code).send_keys(zip_code)
        self.browser.find_element(By.NAME, self._city).send_keys(city)
        self.browser.find_element(By.NAME, self._country).send_keys(country)
        self.browser.find_element(By.NAME, self._job_position).send_keys(job_position)
        self.browser.find_element(By.NAME, self._company).send_keys(company)

    def click_submit_button(self):
        WebDriverWait(self.browser, 40, 0.1).until(EC.element_to_be_clickable(self._button)).click()