"""Get Titles on Youtube(1)"""
import time
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 실행
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.youtube.com/feed/trending")
time.sleep(2)
elements = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
time.sleep(2)
hits_list = []
title_list = []
for element in elements:
    # shorts를 제외하기 위한 조건문
    if element.get_attribute("aria-label"):
        # 제목, 조회수를 포함하는 전체 텍스트
        HIT_TEXT = element.get_attribute("aria-label")
        start_index = HIT_TEXT.rfind("조회수")+4
        end_index = HIT_TEXT.rfind("회")
        # 조회수 숫자값만 추출
        hits = HIT_TEXT[start_index:end_index]
        # , 부분 없애기
        hits = int(hits.replace(",", ""))
        # 제목은 제목 리스트에 추가
        title_list.append(element.text)
        # 조회수는 조회수 리스트에 추가
        hits_list.append(hits)
    else:
        print("조회수 데이터 없음")

for title, hits in zip(title_list, hits_list):
    print(title, hits)

while True:
    try:
        pass
    except NoSuchWindowException:
        break
    finally:
        driver.close()
