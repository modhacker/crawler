# selenium 모듈 추가 
from selenium import webdriver
import time

# 브라우저(크롬) 실행
driver = webdriver.Chrome()
# 주소 입력(구글 홈페이지)
driver.get("https://www.google.com")
time.sleep(5)

