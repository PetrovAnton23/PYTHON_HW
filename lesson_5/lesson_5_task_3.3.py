from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/classattr")
    for a in range(5):
        blue_button = driver.find_element(
            "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), 'btn-primary')]").click()
        blue_button
        sleep(2)
        driver.switch_to.alert.accept()
except Exception as ex:
    print(ex)
finally:
    driver.quit()