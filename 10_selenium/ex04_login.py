from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 브라우저 실행
driver = webdriver.Chrome()
# 접속
driver.get("https://www.naver.com")
# 브라우저 정보 가져오기 
title = driver.title
print(title)
# 로그인 버튼 클릭해보기
# 개발자 도구에서 로그인 버튼에 대한 xpath 복사 
login_button = driver.find_element(By.XPATH, '//*[@id="account"]/div/a')
login_button.click()
# 바로 닫히지 않게 대기(확인을 위해) 
time.sleep(5)