from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.example.com")
# p 태그 요소 모두 가져오기 
p_elements = driver.find_elements(By.TAG_NAME, 'p')
time.sleep(5)
print(p_elements)

# p_elements의 타입 확인
print(type(p_elements))
for p in p_elements:
    print(p)
    print(p.text)