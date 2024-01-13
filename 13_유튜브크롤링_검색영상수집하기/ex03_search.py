"""Crawled 뉴진스 with Youtube(2)"""
import time
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException
from webdriver_manager.chrome import ChromeDriverManager

q = input("검색어를 입력하세요: ")

# 브라우저 실행
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.youtube.com/results?search_query="+q)
time.sleep(5)
titles = driver.find_elements(By.ID, "video-title")
time.sleep(2)
for title in titles:
    print(title.text)

while True:
    try:
        pass
    except NoSuchWindowException:
        break
    finally:
        driver.close()
