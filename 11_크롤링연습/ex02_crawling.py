"""Crawled with Naver Comics"""
import time
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# 네이버 웹툰 페이지 접속
driver.get("https://comic.naver.com/webtoon")
time.sleep(3)
webtoon_titles = driver.find_elements(By.CLASS_NAME, 'text')
for name in webtoon_titles:
    print(name.text)
print(len(webtoon_titles))

while True:
    try:
        if len(driver.window_handles) == 0:
            raise NoSuchWindowException
    except NoSuchWindowException:
        break
