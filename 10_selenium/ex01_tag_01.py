from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.example.com")
# p 태그 요소 가져오기
p_element = driver.find_element(By.TAG_NAME, 'p')
time.sleep(5)
print(p_element)
# 텍스트만 출력
print(p_element.text)
