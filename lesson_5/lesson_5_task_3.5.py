from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://the-internet.herokuapp.com/inputs")
    input_filed = driver.find_element(By.TAG_NAME, "input")
    input_filed.send_keys("1000")
    sleep(2)
    input_filed.clear()
    sleep(1)
    input_filed.send_keys("999")
    sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.quit()  