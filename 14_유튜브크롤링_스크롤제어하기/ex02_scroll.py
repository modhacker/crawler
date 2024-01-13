"""Infinite Scrollings"""
import time
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchWindowException
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 실행
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.youtube.com/")

# 처음 페이지 높이 가져오기 
h1 = driver.execute_script("return document.documentElement.scrollHeight")
print(h1)
# 페이지 높이 만큼 스크롤 내리기
driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
# 약간의 로딩시간
time.sleep(2)
# 스크롤을 한 번 내린 뒤의 페이지 높이 가져오기 
h2 = driver.execute_script("return document.documentElement.scrollHeight")
print(h2)
# 두번째 스크롤 내리는 동작
driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
time.sleep(2)
# 두 번 스크롤 내린 뒤의 페이지 높이 가져오기 
h3 = driver.execute_script("return document.documentElement.scrollHeight")
print(h3)
time.sleep(3)

while True:
    try:
        pass
    except NoSuchWindowException:
        break
    finally:
        driver.close()
