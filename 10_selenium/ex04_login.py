"""Login By XPath"""
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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
while True:
    try:
        pass
    except NoSuchWindowException:
        break
    finally:
        driver.close()
