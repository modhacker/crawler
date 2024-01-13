from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 브라우저 실행
driver = webdriver.Chrome()
# 네이버 웹툰 페이지 접속
driver.get("https://comic.naver.com/webtoon/weekday")
time.sleep(3)
webtoon_titles = driver.find_elements(By.CLASS_NAME, 'text')
for name in webtoon_titles:
    print(name.text)
print(len(webtoon_titles))