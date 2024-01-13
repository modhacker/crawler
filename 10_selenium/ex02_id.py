from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.python.org/")
id_element = driver.find_element(By.ID, 'site-map')
time.sleep(5)

print(id_element)
print(id_element.text)