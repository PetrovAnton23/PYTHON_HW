from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()

chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")

for a in range(5):
    add_button = chrome.find_element("xpath", "//button[text()="Add Element"]").click()
    #add_button = chrome.find_element(By.XPATH, "//button[text()="Add Element"]").click()
    sleep(1)

chrome_delete_buttons = chrome.find_elements(
    "xpath", '//button[text()="Delete"]')

print(f"Список кнопок Delete: {len(chrome_delete_buttons)}")