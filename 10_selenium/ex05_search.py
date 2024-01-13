from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 브라우저 실행
driver = webdriver.Chrome()
# 접속
driver.get("https://www.naver.com")

# 검색창에 파이썬이라고 입력하고 검색버튼 클릭해보기 
search = driver.find_element(By.XPATH, '//*[@id="query"]')
search.send_keys("파이썬")
# 입력하는 것 까지 확인하고 검색 버튼 클릭
search_button = driver.find_element(By.XPATH, '//*[@id="search-btn"]')
search_button.click()
time.sleep(5)