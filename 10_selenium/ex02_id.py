"""Access Tag By ID"""
import time
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.python.org/")
id_element = driver.find_element(By.ID, 'site-map')
time.sleep(5)

print(id_element)
print(id_element.text)
