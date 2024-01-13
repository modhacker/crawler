"""Access Tag"""
import time
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.example.com")
# p 태그 요소 가져오기
p_element = driver.find_element(By.TAG_NAME, 'p')
time.sleep(5)
print(p_element)
# 텍스트만 출력
print(p_element.text)
