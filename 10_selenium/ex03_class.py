from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.python.org/")
class_element = driver.find_elements(By.CLASS_NAME, 'main-content')
time.sleep(5)

for c in class_element:
    print(c.text)