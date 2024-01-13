"""Access Tag By Class"""
import time
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.python.org/")
class_element = driver.find_elements(By.CLASS_NAME, 'main-content')
time.sleep(5)

for c in class_element:
    print(c.text)
