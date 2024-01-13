"""Crawled with Youtube"""
import time
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException
from webdriver_manager.chrome import ChromeDriverManager
# 브라우저 실행
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.youtube.com/")
titles = driver.find_elements(By.ID, "video-title")
# titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
time.sleep(5)
print(titles)
for title in titles:
    print(title.tag_name) # 태그 이름 가져오기
    print(title.text) # inner HTML 값 가져오기
    print(title.get_attribute("aria-label")) # 속성값 가져오기

while True:
    try:
        pass
    except NoSuchWindowException:
        break
    finally:
        driver.close()
        