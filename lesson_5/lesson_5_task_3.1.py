from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
firefox.get("https://the-internet.herokuapp.com/add_remove_elements/")

for a in range(5):
    add_button = chrome.find_element(
        "xpath", "//button[text()='Add Element']").click()
    add_button = firefox.find_element(
        By.XPATH, "//button[text()='Add Element']").click()

chrome_delete_buttons = chrome.find_elements(
    "xpath", "//button[text()='Delete']")
firefox_delete_buttons = firefox.find_elements(
    "xpath", "//button[text()='Delete']")

print(
    f"Список кнопок Delete: {len(chrome_delete_buttons)}")
print(
    f"Список кнопок Delete: {len(firefox_delete_buttons)}")