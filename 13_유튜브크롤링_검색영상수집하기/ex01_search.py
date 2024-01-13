"""Crawled 뉴진스 with Youtube(1)"""
import time
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchWindowException
from webdriver_manager.chrome import ChromeDriverManager
# 브라우저 실행
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.youtube.com/")
search_input = driver.find_element(By.CSS_SELECTOR, "input#search")
# print(search_input.tag_name)
search_input.send_keys("뉴진스")
# 검색버튼 클릭
# search_button = driver.find_element(By.CSS_SELECTOR, "button#search-icon-legacy")
# search_button.click()
time.sleep(2)
# 엔터키 입력
search_input.send_keys(Keys.RETURN)
time.sleep(2)
titles = driver.find_elements(By.ID, "video-title")
for title in titles:
    print(title.text)

while True:
    try:
        if len(driver.window_handles) == 0:
            raise NoSuchWindowException
    except NoSuchWindowException:
        break
    